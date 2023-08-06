"""
A specific branch of medical science that pertains to the study of the kidneys and its respective disease states.

https://schema.org/Renal
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RenalInheritedProperties(TypedDict):
    """A specific branch of medical science that pertains to the study of the kidneys and its respective disease states.

    References:
        https://schema.org/Renal
    Note:
        Model Depth 6
    Attributes:
    """


class RenalProperties(TypedDict):
    """A specific branch of medical science that pertains to the study of the kidneys and its respective disease states.

    References:
        https://schema.org/Renal
    Note:
        Model Depth 6
    Attributes:
    """


class RenalAllProperties(RenalInheritedProperties, RenalProperties, TypedDict):
    pass


class RenalBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Renal", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RenalProperties, RenalInheritedProperties, RenalAllProperties
    ] = RenalAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Renal"
    return model


Renal = create_schema_org_model()


def create_renal_model(
    model: Union[RenalProperties, RenalInheritedProperties, RenalAllProperties]
):
    _type = deepcopy(RenalAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RenalAllProperties):
    pydantic_type = create_renal_model(model=model)
    return pydantic_type(model).schema_json()
