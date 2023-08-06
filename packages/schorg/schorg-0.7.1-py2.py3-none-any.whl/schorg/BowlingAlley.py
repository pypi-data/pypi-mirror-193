"""
A bowling alley.

https://schema.org/BowlingAlley
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BowlingAlleyInheritedProperties(TypedDict):
    """A bowling alley.

    References:
        https://schema.org/BowlingAlley
    Note:
        Model Depth 5
    Attributes:
    """

    


class BowlingAlleyProperties(TypedDict):
    """A bowling alley.

    References:
        https://schema.org/BowlingAlley
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(BowlingAlleyInheritedProperties , BowlingAlleyProperties, TypedDict):
    pass


class BowlingAlleyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BowlingAlley",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BowlingAlleyProperties, BowlingAlleyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BowlingAlley"
    return model
    

BowlingAlley = create_schema_org_model()


def create_bowlingalley_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bowlingalley_model(model=model)
    return pydantic_type(model).schema_json()


