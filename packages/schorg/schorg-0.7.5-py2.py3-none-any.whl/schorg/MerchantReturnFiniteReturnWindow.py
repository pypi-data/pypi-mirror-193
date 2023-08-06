"""
Specifies that there is a finite window for product returns.

https://schema.org/MerchantReturnFiniteReturnWindow
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MerchantReturnFiniteReturnWindowInheritedProperties(TypedDict):
    """Specifies that there is a finite window for product returns.

    References:
        https://schema.org/MerchantReturnFiniteReturnWindow
    Note:
        Model Depth 5
    Attributes:
    """


class MerchantReturnFiniteReturnWindowProperties(TypedDict):
    """Specifies that there is a finite window for product returns.

    References:
        https://schema.org/MerchantReturnFiniteReturnWindow
    Note:
        Model Depth 5
    Attributes:
    """


class MerchantReturnFiniteReturnWindowAllProperties(
    MerchantReturnFiniteReturnWindowInheritedProperties,
    MerchantReturnFiniteReturnWindowProperties,
    TypedDict,
):
    pass


class MerchantReturnFiniteReturnWindowBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MerchantReturnFiniteReturnWindow", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MerchantReturnFiniteReturnWindowProperties,
        MerchantReturnFiniteReturnWindowInheritedProperties,
        MerchantReturnFiniteReturnWindowAllProperties,
    ] = MerchantReturnFiniteReturnWindowAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MerchantReturnFiniteReturnWindow"
    return model


MerchantReturnFiniteReturnWindow = create_schema_org_model()


def create_merchantreturnfinitereturnwindow_model(
    model: Union[
        MerchantReturnFiniteReturnWindowProperties,
        MerchantReturnFiniteReturnWindowInheritedProperties,
        MerchantReturnFiniteReturnWindowAllProperties,
    ]
):
    _type = deepcopy(MerchantReturnFiniteReturnWindowAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MerchantReturnFiniteReturnWindow. Please see: https://schema.org/MerchantReturnFiniteReturnWindow"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MerchantReturnFiniteReturnWindowAllProperties):
    pydantic_type = create_merchantreturnfinitereturnwindow_model(model=model)
    return pydantic_type(model).schema_json()
