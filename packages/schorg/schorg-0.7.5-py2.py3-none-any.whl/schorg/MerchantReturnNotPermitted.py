"""
Specifies that product returns are not permitted.

https://schema.org/MerchantReturnNotPermitted
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MerchantReturnNotPermittedInheritedProperties(TypedDict):
    """Specifies that product returns are not permitted.

    References:
        https://schema.org/MerchantReturnNotPermitted
    Note:
        Model Depth 5
    Attributes:
    """


class MerchantReturnNotPermittedProperties(TypedDict):
    """Specifies that product returns are not permitted.

    References:
        https://schema.org/MerchantReturnNotPermitted
    Note:
        Model Depth 5
    Attributes:
    """


class MerchantReturnNotPermittedAllProperties(
    MerchantReturnNotPermittedInheritedProperties,
    MerchantReturnNotPermittedProperties,
    TypedDict,
):
    pass


class MerchantReturnNotPermittedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MerchantReturnNotPermitted", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MerchantReturnNotPermittedProperties,
        MerchantReturnNotPermittedInheritedProperties,
        MerchantReturnNotPermittedAllProperties,
    ] = MerchantReturnNotPermittedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MerchantReturnNotPermitted"
    return model


MerchantReturnNotPermitted = create_schema_org_model()


def create_merchantreturnnotpermitted_model(
    model: Union[
        MerchantReturnNotPermittedProperties,
        MerchantReturnNotPermittedInheritedProperties,
        MerchantReturnNotPermittedAllProperties,
    ]
):
    _type = deepcopy(MerchantReturnNotPermittedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MerchantReturnNotPermitted. Please see: https://schema.org/MerchantReturnNotPermitted"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MerchantReturnNotPermittedAllProperties):
    pydantic_type = create_merchantreturnnotpermitted_model(model=model)
    return pydantic_type(model).schema_json()
