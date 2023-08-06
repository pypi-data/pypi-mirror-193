"""
Item is a narcotic as defined by the [1961 UN convention](https://www.incb.org/incb/en/narcotic-drugs/Yellowlist/yellow-list.html), for example marijuana or heroin.

https://schema.org/NarcoticConsideration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NarcoticConsiderationInheritedProperties(TypedDict):
    """Item is a narcotic as defined by the [1961 UN convention](https://www.incb.org/incb/en/narcotic-drugs/Yellowlist/yellow-list.html), for example marijuana or heroin.

    References:
        https://schema.org/NarcoticConsideration
    Note:
        Model Depth 5
    Attributes:
    """

    


class NarcoticConsiderationProperties(TypedDict):
    """Item is a narcotic as defined by the [1961 UN convention](https://www.incb.org/incb/en/narcotic-drugs/Yellowlist/yellow-list.html), for example marijuana or heroin.

    References:
        https://schema.org/NarcoticConsideration
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(NarcoticConsiderationInheritedProperties , NarcoticConsiderationProperties, TypedDict):
    pass


class NarcoticConsiderationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="NarcoticConsideration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[NarcoticConsiderationProperties, NarcoticConsiderationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NarcoticConsideration"
    return model
    

NarcoticConsideration = create_schema_org_model()


def create_narcoticconsideration_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_narcoticconsideration_model(model=model)
    return pydantic_type(model).schema_json()


