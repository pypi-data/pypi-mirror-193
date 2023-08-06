"""
USNonprofitType: Non-profit organization type originating from the United States.

https://schema.org/USNonprofitType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class USNonprofitTypeInheritedProperties(TypedDict):
    """USNonprofitType: Non-profit organization type originating from the United States.

    References:
        https://schema.org/USNonprofitType
    Note:
        Model Depth 5
    Attributes:
    """

    


class USNonprofitTypeProperties(TypedDict):
    """USNonprofitType: Non-profit organization type originating from the United States.

    References:
        https://schema.org/USNonprofitType
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(USNonprofitTypeInheritedProperties , USNonprofitTypeProperties, TypedDict):
    pass


class USNonprofitTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="USNonprofitType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[USNonprofitTypeProperties, USNonprofitTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "USNonprofitType"
    return model
    

USNonprofitType = create_schema_org_model()


def create_usnonprofittype_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_usnonprofittype_model(model=model)
    return pydantic_type(model).schema_json()


