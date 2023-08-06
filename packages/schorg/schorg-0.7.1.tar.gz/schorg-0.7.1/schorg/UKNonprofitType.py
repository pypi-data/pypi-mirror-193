"""
UKNonprofitType: Non-profit organization type originating from the United Kingdom.

https://schema.org/UKNonprofitType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UKNonprofitTypeInheritedProperties(TypedDict):
    """UKNonprofitType: Non-profit organization type originating from the United Kingdom.

    References:
        https://schema.org/UKNonprofitType
    Note:
        Model Depth 5
    Attributes:
    """

    


class UKNonprofitTypeProperties(TypedDict):
    """UKNonprofitType: Non-profit organization type originating from the United Kingdom.

    References:
        https://schema.org/UKNonprofitType
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(UKNonprofitTypeInheritedProperties , UKNonprofitTypeProperties, TypedDict):
    pass


class UKNonprofitTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="UKNonprofitType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[UKNonprofitTypeProperties, UKNonprofitTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UKNonprofitType"
    return model
    

UKNonprofitType = create_schema_org_model()


def create_uknonprofittype_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_uknonprofittype_model(model=model)
    return pydantic_type(model).schema_json()


