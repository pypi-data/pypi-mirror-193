"""
UKTrust: Non-profit type referring to a UK trust.

https://schema.org/UKTrust
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class UKTrustAllProperties(UKTrustInheritedProperties, UKTrustProperties, TypedDict):
    pass


class UKTrustBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UKTrust", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UKTrustProperties, UKTrustInheritedProperties, UKTrustAllProperties
    ] = UKTrustAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UKTrust"
    return model


UKTrust = create_schema_org_model()


def create_uktrust_model(
    model: Union[UKTrustProperties, UKTrustInheritedProperties, UKTrustAllProperties]
):
    _type = deepcopy(UKTrustAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of UKTrustAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UKTrustAllProperties):
    pydantic_type = create_uktrust_model(model=model)
    return pydantic_type(model).schema_json()
