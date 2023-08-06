"""
ParentalSupport: this is a benefit for parental support.

https://schema.org/ParentalSupport
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ParentalSupportInheritedProperties(TypedDict):
    """ParentalSupport: this is a benefit for parental support.

    References:
        https://schema.org/ParentalSupport
    Note:
        Model Depth 5
    Attributes:
    """

    


class ParentalSupportProperties(TypedDict):
    """ParentalSupport: this is a benefit for parental support.

    References:
        https://schema.org/ParentalSupport
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ParentalSupportInheritedProperties , ParentalSupportProperties, TypedDict):
    pass


class ParentalSupportBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ParentalSupport",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ParentalSupportProperties, ParentalSupportInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ParentalSupport"
    return model
    

ParentalSupport = create_schema_org_model()


def create_parentalsupport_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_parentalsupport_model(model=model)
    return pydantic_type(model).schema_json()


