"""
Indicates that the item is available only at physical locations.

https://schema.org/InStoreOnly
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InStoreOnlyInheritedProperties(TypedDict):
    """Indicates that the item is available only at physical locations.

    References:
        https://schema.org/InStoreOnly
    Note:
        Model Depth 5
    Attributes:
    """

    


class InStoreOnlyProperties(TypedDict):
    """Indicates that the item is available only at physical locations.

    References:
        https://schema.org/InStoreOnly
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(InStoreOnlyInheritedProperties , InStoreOnlyProperties, TypedDict):
    pass


class InStoreOnlyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="InStoreOnly",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[InStoreOnlyProperties, InStoreOnlyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InStoreOnly"
    return model
    

InStoreOnly = create_schema_org_model()


def create_instoreonly_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_instoreonly_model(model=model)
    return pydantic_type(model).schema_json()


