"""
A store that sells mobile phones and related accessories.

https://schema.org/MobilePhoneStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MobilePhoneStoreInheritedProperties(TypedDict):
    """A store that sells mobile phones and related accessories.

    References:
        https://schema.org/MobilePhoneStore
    Note:
        Model Depth 5
    Attributes:
    """


class MobilePhoneStoreProperties(TypedDict):
    """A store that sells mobile phones and related accessories.

    References:
        https://schema.org/MobilePhoneStore
    Note:
        Model Depth 5
    Attributes:
    """


class MobilePhoneStoreAllProperties(
    MobilePhoneStoreInheritedProperties, MobilePhoneStoreProperties, TypedDict
):
    pass


class MobilePhoneStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MobilePhoneStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MobilePhoneStoreProperties,
        MobilePhoneStoreInheritedProperties,
        MobilePhoneStoreAllProperties,
    ] = MobilePhoneStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MobilePhoneStore"
    return model


MobilePhoneStore = create_schema_org_model()


def create_mobilephonestore_model(
    model: Union[
        MobilePhoneStoreProperties,
        MobilePhoneStoreInheritedProperties,
        MobilePhoneStoreAllProperties,
    ]
):
    _type = deepcopy(MobilePhoneStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MobilePhoneStoreAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MobilePhoneStoreAllProperties):
    pydantic_type = create_mobilephonestore_model(model=model)
    return pydantic_type(model).schema_json()
