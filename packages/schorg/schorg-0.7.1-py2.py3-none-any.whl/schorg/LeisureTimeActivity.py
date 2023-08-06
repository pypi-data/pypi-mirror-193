"""
Any physical activity engaged in for recreational purposes. Examples may include ballroom dancing, roller skating, canoeing, fishing, etc.

https://schema.org/LeisureTimeActivity
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LeisureTimeActivityInheritedProperties(TypedDict):
    """Any physical activity engaged in for recreational purposes. Examples may include ballroom dancing, roller skating, canoeing, fishing, etc.

    References:
        https://schema.org/LeisureTimeActivity
    Note:
        Model Depth 5
    Attributes:
    """

    


class LeisureTimeActivityProperties(TypedDict):
    """Any physical activity engaged in for recreational purposes. Examples may include ballroom dancing, roller skating, canoeing, fishing, etc.

    References:
        https://schema.org/LeisureTimeActivity
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(LeisureTimeActivityInheritedProperties , LeisureTimeActivityProperties, TypedDict):
    pass


class LeisureTimeActivityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LeisureTimeActivity",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[LeisureTimeActivityProperties, LeisureTimeActivityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LeisureTimeActivity"
    return model
    

LeisureTimeActivity = create_schema_org_model()


def create_leisuretimeactivity_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_leisuretimeactivity_model(model=model)
    return pydantic_type(model).schema_json()


