"""
A radio channel that uses AM.

https://schema.org/AMRadioChannel
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AMRadioChannelInheritedProperties(TypedDict):
    """A radio channel that uses AM.

    References:
        https://schema.org/AMRadioChannel
    Note:
        Model Depth 5
    Attributes:
    """

    


class AMRadioChannelProperties(TypedDict):
    """A radio channel that uses AM.

    References:
        https://schema.org/AMRadioChannel
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(AMRadioChannelInheritedProperties , AMRadioChannelProperties, TypedDict):
    pass


class AMRadioChannelBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AMRadioChannel",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[AMRadioChannelProperties, AMRadioChannelInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AMRadioChannel"
    return model
    

AMRadioChannel = create_schema_org_model()


def create_amradiochannel_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_amradiochannel_model(model=model)
    return pydantic_type(model).schema_json()


