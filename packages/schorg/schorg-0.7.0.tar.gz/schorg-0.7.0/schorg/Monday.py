"""
The day of the week between Sunday and Tuesday.

https://schema.org/Monday
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MondayInheritedProperties(TypedDict):
    """The day of the week between Sunday and Tuesday.

    References:
        https://schema.org/Monday
    Note:
        Model Depth 5
    Attributes:
    """

    


class MondayProperties(TypedDict):
    """The day of the week between Sunday and Tuesday.

    References:
        https://schema.org/Monday
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MondayInheritedProperties , MondayProperties, TypedDict):
    pass


class MondayBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Monday",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MondayProperties, MondayInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Monday"
    return model
    

Monday = create_schema_org_model()


def create_monday_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_monday_model(model=model)
    return pydantic_type(model).schema_json()


