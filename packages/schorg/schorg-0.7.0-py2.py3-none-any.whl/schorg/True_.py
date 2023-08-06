"""
The boolean value true.

https://schema.org/True
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class True_InheritedProperties(TypedDict):
    """The boolean value true.

    References:
        https://schema.org/True
    Note:
        Model Depth 6
    Attributes:
    """

    


class True_Properties(TypedDict):
    """The boolean value true.

    References:
        https://schema.org/True
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(True_InheritedProperties , True_Properties, TypedDict):
    pass


class True_BaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="True_",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[True_Properties, True_InheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "True_"
    return model
    

True_ = create_schema_org_model()


def create_true__model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_true__model(model=model)
    return pydantic_type(model).schema_json()


