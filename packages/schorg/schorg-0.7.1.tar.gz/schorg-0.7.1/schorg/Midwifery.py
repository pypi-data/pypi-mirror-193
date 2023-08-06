"""
A nurse-like health profession that deals with pregnancy, childbirth, and the postpartum period (including care of the newborn), besides sexual and reproductive health of women throughout their lives.

https://schema.org/Midwifery
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(MidwiferyInheritedProperties , MidwiferyProperties, TypedDict):
    pass


class MidwiferyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Midwifery",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MidwiferyProperties, MidwiferyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Midwifery"
    return model
    

Midwifery = create_schema_org_model()


def create_midwifery_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_midwifery_model(model=model)
    return pydantic_type(model).schema_json()


