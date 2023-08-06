"""
Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached.

https://schema.org/OnlineFull
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OnlineFullInheritedProperties(TypedDict):
    """Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached.

    References:
        https://schema.org/OnlineFull
    Note:
        Model Depth 6
    Attributes:
    """

    


class OnlineFullProperties(TypedDict):
    """Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached.

    References:
        https://schema.org/OnlineFull
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(OnlineFullInheritedProperties , OnlineFullProperties, TypedDict):
    pass


class OnlineFullBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OnlineFull",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OnlineFullProperties, OnlineFullInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OnlineFull"
    return model
    

OnlineFull = create_schema_org_model()


def create_onlinefull_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_onlinefull_model(model=model)
    return pydantic_type(model).schema_json()


