"""
Data type: Floating number.

https://schema.org/Float
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FloatInheritedProperties(TypedDict):
    """Data type: Floating number.

    References:
        https://schema.org/Float
    Note:
        Model Depth 6
    Attributes:
    """

    


class FloatProperties(TypedDict):
    """Data type: Floating number.

    References:
        https://schema.org/Float
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(FloatInheritedProperties , FloatProperties, TypedDict):
    pass


class FloatBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Float",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[FloatProperties, FloatInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Float"
    return model
    

Float = create_schema_org_model()


def create_float_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_float_model(model=model)
    return pydantic_type(model).schema_json()


