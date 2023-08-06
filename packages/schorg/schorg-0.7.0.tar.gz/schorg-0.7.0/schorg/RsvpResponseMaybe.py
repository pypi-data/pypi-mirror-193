"""
The invitee may or may not attend.

https://schema.org/RsvpResponseMaybe
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RsvpResponseMaybeInheritedProperties(TypedDict):
    """The invitee may or may not attend.

    References:
        https://schema.org/RsvpResponseMaybe
    Note:
        Model Depth 5
    Attributes:
    """

    


class RsvpResponseMaybeProperties(TypedDict):
    """The invitee may or may not attend.

    References:
        https://schema.org/RsvpResponseMaybe
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(RsvpResponseMaybeInheritedProperties , RsvpResponseMaybeProperties, TypedDict):
    pass


class RsvpResponseMaybeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RsvpResponseMaybe",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RsvpResponseMaybeProperties, RsvpResponseMaybeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RsvpResponseMaybe"
    return model
    

RsvpResponseMaybe = create_schema_org_model()


def create_rsvpresponsemaybe_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_rsvpresponsemaybe_model(model=model)
    return pydantic_type(model).schema_json()


