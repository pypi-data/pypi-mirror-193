"""
USNonprofitType: Non-profit organization type originating from the United States.

https://schema.org/USNonprofitType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class USNonprofitTypeAllProperties(
    USNonprofitTypeInheritedProperties, USNonprofitTypeProperties, TypedDict
):
    pass


class USNonprofitTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="USNonprofitType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        USNonprofitTypeProperties,
        USNonprofitTypeInheritedProperties,
        USNonprofitTypeAllProperties,
    ] = USNonprofitTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "USNonprofitType"
    return model


USNonprofitType = create_schema_org_model()


def create_usnonprofittype_model(
    model: Union[
        USNonprofitTypeProperties,
        USNonprofitTypeInheritedProperties,
        USNonprofitTypeAllProperties,
    ]
):
    _type = deepcopy(USNonprofitTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of USNonprofitTypeAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: USNonprofitTypeAllProperties):
    pydantic_type = create_usnonprofittype_model(model=model)
    return pydantic_type(model).schema_json()
