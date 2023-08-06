"""
A nurse-like health profession that deals with pregnancy, childbirth, and the postpartum period (including care of the newborn), besides sexual and reproductive health of women throughout their lives.

https://schema.org/Midwifery
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MidwiferyInheritedProperties(TypedDict):
    """A nurse-like health profession that deals with pregnancy, childbirth, and the postpartum period (including care of the newborn), besides sexual and reproductive health of women throughout their lives.

    References:
        https://schema.org/Midwifery
    Note:
        Model Depth 5
    Attributes:
    """


class MidwiferyProperties(TypedDict):
    """A nurse-like health profession that deals with pregnancy, childbirth, and the postpartum period (including care of the newborn), besides sexual and reproductive health of women throughout their lives.

    References:
        https://schema.org/Midwifery
    Note:
        Model Depth 5
    Attributes:
    """


class MidwiferyAllProperties(
    MidwiferyInheritedProperties, MidwiferyProperties, TypedDict
):
    pass


class MidwiferyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Midwifery", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MidwiferyProperties, MidwiferyInheritedProperties, MidwiferyAllProperties
    ] = MidwiferyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Midwifery"
    return model


Midwifery = create_schema_org_model()


def create_midwifery_model(
    model: Union[
        MidwiferyProperties, MidwiferyInheritedProperties, MidwiferyAllProperties
    ]
):
    _type = deepcopy(MidwiferyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MidwiferyAllProperties):
    pydantic_type = create_midwifery_model(model=model)
    return pydantic_type(model).schema_json()
