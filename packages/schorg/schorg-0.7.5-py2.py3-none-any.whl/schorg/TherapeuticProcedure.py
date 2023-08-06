"""
A medical procedure intended primarily for therapeutic purposes, aimed at improving a health condition.

https://schema.org/TherapeuticProcedure
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TherapeuticProcedureInheritedProperties(TypedDict):
    """A medical procedure intended primarily for therapeutic purposes, aimed at improving a health condition.

    References:
        https://schema.org/TherapeuticProcedure
    Note:
        Model Depth 4
    Attributes:
        howPerformed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): How the procedure is performed.
        procedureType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type of procedure, for example Surgical, Noninvasive, or Percutaneous.
        status: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The status of the study (enumerated).
        bodyLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Location in the body of the anatomical structure.
        followup: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Typical or recommended followup care after the procedure is performed.
        preparation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Typical preparation that a patient must undergo before having the procedure performed.
    """

    howPerformed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    procedureType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    status: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    bodyLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    followup: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    preparation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class TherapeuticProcedureProperties(TypedDict):
    """A medical procedure intended primarily for therapeutic purposes, aimed at improving a health condition.

    References:
        https://schema.org/TherapeuticProcedure
    Note:
        Model Depth 4
    Attributes:
        doseSchedule: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.
        drug: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifying a drug or medicine used in a medication procedure.
        adverseOutcome: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or otherwise life-threatening or requiring immediate medical attention), tag it as a seriousAdverseOutcome instead.
    """

    doseSchedule: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    drug: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    adverseOutcome: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class TherapeuticProcedureAllProperties(
    TherapeuticProcedureInheritedProperties, TherapeuticProcedureProperties, TypedDict
):
    pass


class TherapeuticProcedureBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TherapeuticProcedure", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"howPerformed": {"exclude": True}}
        fields = {"procedureType": {"exclude": True}}
        fields = {"status": {"exclude": True}}
        fields = {"bodyLocation": {"exclude": True}}
        fields = {"followup": {"exclude": True}}
        fields = {"preparation": {"exclude": True}}
        fields = {"doseSchedule": {"exclude": True}}
        fields = {"drug": {"exclude": True}}
        fields = {"adverseOutcome": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        TherapeuticProcedureProperties,
        TherapeuticProcedureInheritedProperties,
        TherapeuticProcedureAllProperties,
    ] = TherapeuticProcedureAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TherapeuticProcedure"
    return model


TherapeuticProcedure = create_schema_org_model()


def create_therapeuticprocedure_model(
    model: Union[
        TherapeuticProcedureProperties,
        TherapeuticProcedureInheritedProperties,
        TherapeuticProcedureAllProperties,
    ]
):
    _type = deepcopy(TherapeuticProcedureAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TherapeuticProcedure. Please see: https://schema.org/TherapeuticProcedure"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TherapeuticProcedureAllProperties):
    pydantic_type = create_therapeuticprocedure_model(model=model)
    return pydantic_type(model).schema_json()
