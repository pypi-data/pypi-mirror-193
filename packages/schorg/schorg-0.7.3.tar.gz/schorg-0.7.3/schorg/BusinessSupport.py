"""
BusinessSupport: this is a benefit for supporting businesses.

https://schema.org/BusinessSupport
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BusinessSupportInheritedProperties(TypedDict):
    """BusinessSupport: this is a benefit for supporting businesses.

    References:
        https://schema.org/BusinessSupport
    Note:
        Model Depth 5
    Attributes:
    """


class BusinessSupportProperties(TypedDict):
    """BusinessSupport: this is a benefit for supporting businesses.

    References:
        https://schema.org/BusinessSupport
    Note:
        Model Depth 5
    Attributes:
    """


class BusinessSupportAllProperties(
    BusinessSupportInheritedProperties, BusinessSupportProperties, TypedDict
):
    pass


class BusinessSupportBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BusinessSupport", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BusinessSupportProperties,
        BusinessSupportInheritedProperties,
        BusinessSupportAllProperties,
    ] = BusinessSupportAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BusinessSupport"
    return model


BusinessSupport = create_schema_org_model()


def create_businesssupport_model(
    model: Union[
        BusinessSupportProperties,
        BusinessSupportInheritedProperties,
        BusinessSupportAllProperties,
    ]
):
    _type = deepcopy(BusinessSupportAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BusinessSupportAllProperties):
    pydantic_type = create_businesssupport_model(model=model)
    return pydantic_type(model).schema_json()
