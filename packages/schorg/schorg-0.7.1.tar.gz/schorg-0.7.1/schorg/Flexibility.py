"""
Physical activity that is engaged in to improve joint and muscle flexibility.

https://schema.org/Flexibility
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FlexibilityInheritedProperties(TypedDict):
    """Physical activity that is engaged in to improve joint and muscle flexibility.

    References:
        https://schema.org/Flexibility
    Note:
        Model Depth 5
    Attributes:
    """

    


class FlexibilityProperties(TypedDict):
    """Physical activity that is engaged in to improve joint and muscle flexibility.

    References:
        https://schema.org/Flexibility
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(FlexibilityInheritedProperties , FlexibilityProperties, TypedDict):
    pass


class FlexibilityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Flexibility",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[FlexibilityProperties, FlexibilityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Flexibility"
    return model
    

Flexibility = create_schema_org_model()


def create_flexibility_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_flexibility_model(model=model)
    return pydantic_type(model).schema_json()


