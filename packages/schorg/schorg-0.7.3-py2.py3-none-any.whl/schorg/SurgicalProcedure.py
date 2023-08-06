"""
A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes.

https://schema.org/SurgicalProcedure
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SurgicalProcedureInheritedProperties(TypedDict):
    """A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes.

    References:
        https://schema.org/SurgicalProcedure
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


class SurgicalProcedureProperties(TypedDict):
    """A medical procedure involving an incision with instruments; performed for diagnose, or therapeutic purposes.

    References:
        https://schema.org/SurgicalProcedure
    Note:
        Model Depth 4
    Attributes:
    """


class SurgicalProcedureAllProperties(
    SurgicalProcedureInheritedProperties, SurgicalProcedureProperties, TypedDict
):
    pass


class SurgicalProcedureBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SurgicalProcedure", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"howPerformed": {"exclude": True}}
        fields = {"procedureType": {"exclude": True}}
        fields = {"status": {"exclude": True}}
        fields = {"bodyLocation": {"exclude": True}}
        fields = {"followup": {"exclude": True}}
        fields = {"preparation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        SurgicalProcedureProperties,
        SurgicalProcedureInheritedProperties,
        SurgicalProcedureAllProperties,
    ] = SurgicalProcedureAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SurgicalProcedure"
    return model


SurgicalProcedure = create_schema_org_model()


def create_surgicalprocedure_model(
    model: Union[
        SurgicalProcedureProperties,
        SurgicalProcedureInheritedProperties,
        SurgicalProcedureAllProperties,
    ]
):
    _type = deepcopy(SurgicalProcedureAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SurgicalProcedureAllProperties):
    pydantic_type = create_surgicalprocedure_model(model=model)
    return pydantic_type(model).schema_json()
