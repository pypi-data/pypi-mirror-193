"""
A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see [XML schema for details](http://www.w3.org/TR/xmlschema-2/#time)).

https://schema.org/Time
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TimeInheritedProperties(TypedDict):
    """A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see [XML schema for details](http://www.w3.org/TR/xmlschema-2/#time)).

    References:
        https://schema.org/Time
    Note:
        Model Depth 5
    Attributes:
    """

    


class TimeProperties(TypedDict):
    """A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see [XML schema for details](http://www.w3.org/TR/xmlschema-2/#time)).

    References:
        https://schema.org/Time
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(TimeInheritedProperties , TimeProperties, TypedDict):
    pass


class TimeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Time",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TimeProperties, TimeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Time"
    return model
    

Time = create_schema_org_model()


def create_time_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_time_model(model=model)
    return pydantic_type(model).schema_json()


