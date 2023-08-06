"""
Specifies that there is an unlimited window for product returns.

https://schema.org/MerchantReturnUnlimitedWindow
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MerchantReturnUnlimitedWindowInheritedProperties(TypedDict):
    """Specifies that there is an unlimited window for product returns.

    References:
        https://schema.org/MerchantReturnUnlimitedWindow
    Note:
        Model Depth 5
    Attributes:
    """

    


class MerchantReturnUnlimitedWindowProperties(TypedDict):
    """Specifies that there is an unlimited window for product returns.

    References:
        https://schema.org/MerchantReturnUnlimitedWindow
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MerchantReturnUnlimitedWindowInheritedProperties , MerchantReturnUnlimitedWindowProperties, TypedDict):
    pass


class MerchantReturnUnlimitedWindowBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MerchantReturnUnlimitedWindow",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MerchantReturnUnlimitedWindowProperties, MerchantReturnUnlimitedWindowInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MerchantReturnUnlimitedWindow"
    return model
    

MerchantReturnUnlimitedWindow = create_schema_org_model()


def create_merchantreturnunlimitedwindow_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_merchantreturnunlimitedwindow_model(model=model)
    return pydantic_type(model).schema_json()


