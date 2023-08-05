import json
from .models import (
    SignList,
    TransitionManager,
    Action,
    workevents,
    workflowitems,
    Flowmodel,
)
from django.core import serializers as core_serializers
from .middleware import get_current_user
from .exception import (
    ModelNotFound,
    TransitionNotAllowed,
    ReturnModelNotFound,
)
from django.db.models import Q
from django.conf import settings
from collections import deque
from django.apps import apps
from django.forms.models import model_to_dict
from dataclasses import dataclass
from typing import Optional
import contextlib

####################################################
#############       CORE     #######################
####################################################

@dataclass
class FinFlotransition:

    # BASE CONSTRUCTORS #

    type: str
    source: str
    target: str
    interim: Optional[str] = None
    action : Optional[str] = None
    party : Optional[str] = None
    from_party: Optional[str] = None
    to_party : Optional[str] = None
    record_datas : Optional[None] = None
    gets_return_action = self.gets_default_return_action()


    def __post_init__(self):
        if self.action:
            if self.action == self.gets_default_return_action().description:
                self.return_transition()
            self.transition()
        self.manualtransitions()
    


    def __repr__(self):
        return f"the id is {self.t_id} and type is {self.type}"

    def __str__(self):
        return f"the id is {self.t_id} and type is {self.type}"

    # GETS THE ALL MODEL VALUE FOR TRANSITION #

    def gets_base_action(self):
        with contextlib.suppress(ModelNotFound):
            return Action.objects.get(description=self.action, model__description=self.type)
    

    # RETURN ACTION
    def gets_default_return_action(self):
        with contextlib.suppress(ReturnModelNotFound):
            return Action.objects.get(id=1)
        

    # GETS WORKFLOW MODEL ID #
    def gets_wf_item(self, model):
        with contextlib.suppress(ModelNotFound):
            return workflowitems.objects.get(transitionmanager=model)
        

    # GETS TRANSITION MANAGER
    def gets_base_model(self):
        with contextlib.suppress(ModelNotFound):
            return TransitionManager.objects.get(type=self.type, t_id=self.t_id)
    

    def sign_reset(self, overall_model):
        overall_model[0].sub_sign = 0
        overall_model[0].in_progress = False
        overall_model[0].save()

    # GETS ALL ACTION
    def gets_all_models(self):
        with contextlib.suppress(ModelNotFound):
            gets_model = TransitionManager.objects.get(type__icontains=self.type, t_id=self.t_id)
            gets_flows = Flowmodel.objects.get(description__icontains=self.type)
            gets_action = Action.objects.get(
                Q(model=gets_flows.id) | Q(model=None),
                description=self.action,
                party=self.party or None,
            )
            gets_wf = self.gets_wf_item(gets_model.id)
            sign_lists = []
            try:
                for item in SignList.objects.all():
                    sign_lists.append(item.name)
                    if item.name == gets_action.stage_required.name:
                        break
                next_avail_trans = sign_lists[gets_model.sub_sign :]
                next_avail_trans_value = deque(next_avail_trans)
                next_avail_trans_value.popleft()
                next_states = list(next_avail_trans_value)
                next_avail_Transition = {"values": next_states}
            except Exception:
                next_avail_Transition = None
            return (
                gets_model,
                gets_action,
                gets_flows,
                gets_wf,
                sign_lists,
                next_avail_Transition,
            )


    def return_transition(self):

        overall_model = self.gets_all_models()
        obj, created = workflowitems.objects.update_or_create(
            transitionmanager=overall_model[0] or overall_model[0].id,
            defaults={
                "initial_state": overall_model[1].from_state.description
                if overall_model[1].from_state
                else overall_model[3].initial_state,
                "interim_state": overall_model[1].to_state.description,
                "final_state": overall_model[1].to_state.description,
                "action": self.action,
                "record_datas": self.get_record_datas(),
                "subaction": self.action,
                "previous_action": overall_model[3].action,
                "next_available_transitions": None,
                "model_type": self.type,
                "event_user": get_current_user(),
                "final_value": True,
                "current_from_party": overall_model[1].from_party or self.from_party,
                "current_to_party": overall_model[1].to_party or self.to_party,
            },
        )
        workevents.objects.create(
            workflowitems=overall_model[3],
            event_user=get_current_user(),
            initial_state=overall_model[1].from_state.description
            if overall_model[1].from_state
            else overall_model[3].initial_state,
            final_value=True,
            record_datas=self.get_record_datas(),
            interim_state=overall_model[1].to_state.description,
            final_state=overall_model[1].to_state.description,
            action=self.action,
            subaction=self.action,
            model_type=self.type,
            from_party=overall_model[1].from_party or self.from_party,
            to_party=overall_model[1].to_party or self.to_party,
        )
        self.sign_reset(overall_model)



    def get_record_datas(self):
        overall_model = self.gets_base_model()
        try:
            work_model = settings.FINFLO["WORK_MODEL"]
            for iter in work_model:
                gets_model = apps.get_model(iter)
                query_data = gets_model.objects.filter(id=overall_model.t_id)
                base_serialized_Data = core_serializers.serialize("json", query_data)
                if query_data.exists() and (gets_model._meta.db_table == overall_model.type):
                    break
                continue
            return {"values": json.loads(base_serialized_Data)}
        except Exception:
            return {"values": None}




    # MANUAL TRANSITION WITH SOURCE , INTERIM , AND TARGET STATES

    def manualtransitions(self):
        with contextlib.suppress(TransitionNotAllowed):
            queryset = self.gets_base_model()
            obj, created = workflowitems.objects.update_or_create(
                transitionmanager=queryset,
                defaults={
                    "initial_state": self.source,
                    "interim_state": self.interim,
                    "final_state": self.target,
                    "next_available_transitions": None,
                    "record_datas": self.record_datas or self.get_record_datas(),
                    "model_type": self.type,
                    "event_user": get_current_user(),
                    "current_from_party": self.from_party,
                    "current_to_party": self.to_party,
                    "final_value": True,
                },
            )
            workevents.objects.create(
                workflowitems=obj,
                event_user=get_current_user(),
                initial_state=self.source,
                interim_state=self.interim,
                final_state=self.target,
                model_type=self.type,
                record_datas=self.record_datas or self.get_record_datas(),
                from_party=self.from_party,
                to_party=self.to_party,
                final_value=True,
            )





    ## CORE TRANSITION ###

    def transition(self):
        with contextlib.suppress(TransitionNotAllowed):
            overall_model = self.gets_all_models()
            try:
                ws = workflowitems.objects.update_or_create(
                    transitionmanager=overall_model[0] or overall_model[0].id,
                    defaults={
                        "initial_state": overall_model[1].from_state.description,
                        "interim_state": overall_model[4][
                            1 + overall_model[0].sub_sign
                        ],
                        "final_state": overall_model[1].to_state.description,
                        "next_available_transitions": overall_model[5],
                        "action": self.action,
                        "subaction": overall_model[4][overall_model[0].sub_sign],
                        "model_type": self.type,
                        "record_datas": self.get_record_datas(),
                        "event_user": get_current_user(),
                        "current_from_party": overall_model[1].from_party or self.from_party,
                        "current_to_party": overall_model[1].to_party or self.to_party,
                    },
                )
                workevents.objects.create(
                    workflowitems=overall_model[3],
                    event_user=get_current_user(),
                    initial_state=overall_model[1].from_state.description,
                    interim_state=overall_model[4][1 + overall_model[0].sub_sign],
                    record_datas=self.get_record_datas(),
                    final_state=overall_model[1].to_state.description,
                    action=self.action,
                    subaction=self.action,
                    model_type=self.type,
                    from_party=overall_model[1].from_party or self.from_party,
                    to_party=overall_model[1].to_party or self.to_party,
                )
                overall_model[0].sub_sign += 1
                overall_model[0].in_progress = True
                overall_model[0].save()
            except Exception:
                ws = workflowitems.objects.update_or_create(
                    transitionmanager=overall_model[0] or overall_model[0].id,
                    defaults={
                        "initial_state": overall_model[1].from_state.description,
                        "interim_state": overall_model[1].to_state.description,
                        "final_state": overall_model[1].to_state.description,
                        "action": self.action,
                        "next_available_transitions": None,
                        "subaction": self.action,
                        "model_type": self.type,
                        "record_datas": self.get_record_datas(),
                        "event_user": get_current_user(),
                        "current_from_party": overall_model[1].from_party or self.from_party,
                        "current_to_party": overall_model[1].to_party or self.to_party,
                        "final_value": True,
                    },
                )
                workevents.objects.create(
                    workflowitems=overall_model[3],
                    event_user=get_current_user(),
                    initial_state=overall_model[1].from_state.description,
                    interim_state=overall_model[1].to_state.description,
                    record_datas=self.get_record_datas(),
                    final_state=overall_model[1].to_state.description,
                    action=self.action,
                    subaction=self.action,
                    model_type=self.type,
                    from_party=overall_model[1].from_party or self.from_party,
                    to_party=overall_model[1].to_party or self.to_party,
                    final_value=True,
                )
                self.sign_reset(overall_model)

    
@dataclass
class DefaultModelValues:

    type : str
    id : str
    
    def get_record_Datas(self):
        with contextlib.suppress(ModelNotFound):
            gets_model = apps.get_model(self.type)
            query_data = gets_model.objects.filter(id=self.id)
            base_serialized_Data = core_serializers.serialize("json", query_data)
            if query_data.exists():
                return {"values": json.loads(base_serialized_Data)}