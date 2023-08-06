"""
Specifies that product returns must be made at a kiosk.

https://schema.org/ReturnAtKiosk
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnAtKioskInheritedProperties(TypedDict):
    """Specifies that product returns must be made at a kiosk.

    References:
        https://schema.org/ReturnAtKiosk
    Note:
        Model Depth 5
    Attributes:
    """


class ReturnAtKioskProperties(TypedDict):
    """Specifies that product returns must be made at a kiosk.

    References:
        https://schema.org/ReturnAtKiosk
    Note:
        Model Depth 5
    Attributes:
    """


class ReturnAtKioskAllProperties(
    ReturnAtKioskInheritedProperties, ReturnAtKioskProperties, TypedDict
):
    pass


class ReturnAtKioskBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReturnAtKiosk", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReturnAtKioskProperties,
        ReturnAtKioskInheritedProperties,
        ReturnAtKioskAllProperties,
    ] = ReturnAtKioskAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnAtKiosk"
    return model


ReturnAtKiosk = create_schema_org_model()


def create_returnatkiosk_model(
    model: Union[
        ReturnAtKioskProperties,
        ReturnAtKioskInheritedProperties,
        ReturnAtKioskAllProperties,
    ]
):
    _type = deepcopy(ReturnAtKioskAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ReturnAtKioskAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReturnAtKioskAllProperties):
    pydantic_type = create_returnatkiosk_model(model=model)
    return pydantic_type(model).schema_json()
