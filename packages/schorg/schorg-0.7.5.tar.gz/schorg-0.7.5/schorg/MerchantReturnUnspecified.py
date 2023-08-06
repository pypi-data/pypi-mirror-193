"""
Specifies that a product return policy is not provided.

https://schema.org/MerchantReturnUnspecified
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MerchantReturnUnspecifiedInheritedProperties(TypedDict):
    """Specifies that a product return policy is not provided.

    References:
        https://schema.org/MerchantReturnUnspecified
    Note:
        Model Depth 5
    Attributes:
    """


class MerchantReturnUnspecifiedProperties(TypedDict):
    """Specifies that a product return policy is not provided.

    References:
        https://schema.org/MerchantReturnUnspecified
    Note:
        Model Depth 5
    Attributes:
    """


class MerchantReturnUnspecifiedAllProperties(
    MerchantReturnUnspecifiedInheritedProperties,
    MerchantReturnUnspecifiedProperties,
    TypedDict,
):
    pass


class MerchantReturnUnspecifiedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MerchantReturnUnspecified", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MerchantReturnUnspecifiedProperties,
        MerchantReturnUnspecifiedInheritedProperties,
        MerchantReturnUnspecifiedAllProperties,
    ] = MerchantReturnUnspecifiedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MerchantReturnUnspecified"
    return model


MerchantReturnUnspecified = create_schema_org_model()


def create_merchantreturnunspecified_model(
    model: Union[
        MerchantReturnUnspecifiedProperties,
        MerchantReturnUnspecifiedInheritedProperties,
        MerchantReturnUnspecifiedAllProperties,
    ]
):
    _type = deepcopy(MerchantReturnUnspecifiedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MerchantReturnUnspecified. Please see: https://schema.org/MerchantReturnUnspecified"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MerchantReturnUnspecifiedAllProperties):
    pydantic_type = create_merchantreturnunspecified_model(model=model)
    return pydantic_type(model).schema_json()
