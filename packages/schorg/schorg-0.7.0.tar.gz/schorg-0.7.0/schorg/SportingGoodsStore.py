"""
A sporting goods store.

https://schema.org/SportingGoodsStore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SportingGoodsStoreInheritedProperties(TypedDict):
    """A sporting goods store.

    References:
        https://schema.org/SportingGoodsStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class SportingGoodsStoreProperties(TypedDict):
    """A sporting goods store.

    References:
        https://schema.org/SportingGoodsStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(SportingGoodsStoreInheritedProperties , SportingGoodsStoreProperties, TypedDict):
    pass


class SportingGoodsStoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SportingGoodsStore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SportingGoodsStoreProperties, SportingGoodsStoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SportingGoodsStore"
    return model
    

SportingGoodsStore = create_schema_org_model()


def create_sportinggoodsstore_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_sportinggoodsstore_model(model=model)
    return pydantic_type(model).schema_json()


