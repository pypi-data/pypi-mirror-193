"""
The day of the week between Tuesday and Thursday.

https://schema.org/Wednesday
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WednesdayInheritedProperties(TypedDict):
    """The day of the week between Tuesday and Thursday.

    References:
        https://schema.org/Wednesday
    Note:
        Model Depth 5
    Attributes:
    """

    


class WednesdayProperties(TypedDict):
    """The day of the week between Tuesday and Thursday.

    References:
        https://schema.org/Wednesday
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(WednesdayInheritedProperties , WednesdayProperties, TypedDict):
    pass


class WednesdayBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Wednesday",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WednesdayProperties, WednesdayInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Wednesday"
    return model
    

Wednesday = create_schema_org_model()


def create_wednesday_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wednesday_model(model=model)
    return pydantic_type(model).schema_json()


