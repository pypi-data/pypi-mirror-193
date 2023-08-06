"""
A home goods store.

https://schema.org/HomeGoodsStore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HomeGoodsStoreInheritedProperties(TypedDict):
    """A home goods store.

    References:
        https://schema.org/HomeGoodsStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class HomeGoodsStoreProperties(TypedDict):
    """A home goods store.

    References:
        https://schema.org/HomeGoodsStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HomeGoodsStoreInheritedProperties , HomeGoodsStoreProperties, TypedDict):
    pass


class HomeGoodsStoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HomeGoodsStore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HomeGoodsStoreProperties, HomeGoodsStoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HomeGoodsStore"
    return model
    

HomeGoodsStore = create_schema_org_model()


def create_homegoodsstore_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_homegoodsstore_model(model=model)
    return pydantic_type(model).schema_json()


