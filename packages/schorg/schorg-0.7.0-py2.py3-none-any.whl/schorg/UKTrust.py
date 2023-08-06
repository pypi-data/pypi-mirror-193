"""
UKTrust: Non-profit type referring to a UK trust.

https://schema.org/UKTrust
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UKTrustInheritedProperties(TypedDict):
    """UKTrust: Non-profit type referring to a UK trust.

    References:
        https://schema.org/UKTrust
    Note:
        Model Depth 6
    Attributes:
    """

    


class UKTrustProperties(TypedDict):
    """UKTrust: Non-profit type referring to a UK trust.

    References:
        https://schema.org/UKTrust
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(UKTrustInheritedProperties , UKTrustProperties, TypedDict):
    pass


class UKTrustBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="UKTrust",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[UKTrustProperties, UKTrustInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UKTrust"
    return model
    

UKTrust = create_schema_org_model()


def create_uktrust_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_uktrust_model(model=model)
    return pydantic_type(model).schema_json()


