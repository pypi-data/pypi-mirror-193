"""
The day of the week between Monday and Wednesday.

https://schema.org/Tuesday
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TuesdayInheritedProperties(TypedDict):
    """The day of the week between Monday and Wednesday.

    References:
        https://schema.org/Tuesday
    Note:
        Model Depth 5
    Attributes:
    """

    


class TuesdayProperties(TypedDict):
    """The day of the week between Monday and Wednesday.

    References:
        https://schema.org/Tuesday
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(TuesdayInheritedProperties , TuesdayProperties, TypedDict):
    pass


class TuesdayBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Tuesday",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TuesdayProperties, TuesdayInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Tuesday"
    return model
    

Tuesday = create_schema_org_model()


def create_tuesday_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_tuesday_model(model=model)
    return pydantic_type(model).schema_json()


