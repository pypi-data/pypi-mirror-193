"""
Uses devices to support users with hearing impairments.

https://schema.org/HearingImpairedSupported
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HearingImpairedSupportedInheritedProperties(TypedDict):
    """Uses devices to support users with hearing impairments.

    References:
        https://schema.org/HearingImpairedSupported
    Note:
        Model Depth 5
    Attributes:
    """

    


class HearingImpairedSupportedProperties(TypedDict):
    """Uses devices to support users with hearing impairments.

    References:
        https://schema.org/HearingImpairedSupported
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HearingImpairedSupportedInheritedProperties , HearingImpairedSupportedProperties, TypedDict):
    pass


class HearingImpairedSupportedBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HearingImpairedSupported",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HearingImpairedSupportedProperties, HearingImpairedSupportedInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HearingImpairedSupported"
    return model
    

HearingImpairedSupported = create_schema_org_model()


def create_hearingimpairedsupported_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_hearingimpairedsupported_model(model=model)
    return pydantic_type(model).schema_json()


