"""
Data type: Integer.

https://schema.org/Integer
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class IntegerInheritedProperties(TypedDict):
    """Data type: Integer.

    References:
        https://schema.org/Integer
    Note:
        Model Depth 6
    Attributes:
    """

    


class IntegerProperties(TypedDict):
    """Data type: Integer.

    References:
        https://schema.org/Integer
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(IntegerInheritedProperties , IntegerProperties, TypedDict):
    pass


class IntegerBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Integer",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[IntegerProperties, IntegerInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Integer"
    return model
    

Integer = create_schema_org_model()


def create_integer_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_integer_model(model=model)
    return pydantic_type(model).schema_json()


