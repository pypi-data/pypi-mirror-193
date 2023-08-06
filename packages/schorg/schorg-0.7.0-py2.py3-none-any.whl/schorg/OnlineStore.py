"""
An eCommerce site.

https://schema.org/OnlineStore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OnlineStoreInheritedProperties(TypedDict):
    """An eCommerce site.

    References:
        https://schema.org/OnlineStore
    Note:
        Model Depth 4
    Attributes:
    """

    


class OnlineStoreProperties(TypedDict):
    """An eCommerce site.

    References:
        https://schema.org/OnlineStore
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(OnlineStoreInheritedProperties , OnlineStoreProperties, TypedDict):
    pass


class OnlineStoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OnlineStore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OnlineStoreProperties, OnlineStoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OnlineStore"
    return model
    

OnlineStore = create_schema_org_model()


def create_onlinestore_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_onlinestore_model(model=model)
    return pydantic_type(model).schema_json()


