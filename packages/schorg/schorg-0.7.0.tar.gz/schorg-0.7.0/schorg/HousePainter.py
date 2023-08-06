"""
A house painting service.

https://schema.org/HousePainter
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HousePainterInheritedProperties(TypedDict):
    """A house painting service.

    References:
        https://schema.org/HousePainter
    Note:
        Model Depth 5
    Attributes:
    """

    


class HousePainterProperties(TypedDict):
    """A house painting service.

    References:
        https://schema.org/HousePainter
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HousePainterInheritedProperties , HousePainterProperties, TypedDict):
    pass


class HousePainterBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HousePainter",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HousePainterProperties, HousePainterInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HousePainter"
    return model
    

HousePainter = create_schema_org_model()


def create_housepainter_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_housepainter_model(model=model)
    return pydantic_type(model).schema_json()


