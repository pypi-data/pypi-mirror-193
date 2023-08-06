"""
The day of the week between Wednesday and Friday.

https://schema.org/Thursday
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ThursdayInheritedProperties(TypedDict):
    """The day of the week between Wednesday and Friday.

    References:
        https://schema.org/Thursday
    Note:
        Model Depth 5
    Attributes:
    """

    


class ThursdayProperties(TypedDict):
    """The day of the week between Wednesday and Friday.

    References:
        https://schema.org/Thursday
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ThursdayInheritedProperties , ThursdayProperties, TypedDict):
    pass


class ThursdayBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Thursday",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ThursdayProperties, ThursdayInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Thursday"
    return model
    

Thursday = create_schema_org_model()


def create_thursday_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_thursday_model(model=model)
    return pydantic_type(model).schema_json()


