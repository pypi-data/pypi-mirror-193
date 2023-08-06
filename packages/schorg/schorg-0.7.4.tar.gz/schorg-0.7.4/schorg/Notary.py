"""
A notary.

https://schema.org/Notary
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NotaryInheritedProperties(TypedDict):
    """A notary.

    References:
        https://schema.org/Notary
    Note:
        Model Depth 5
    Attributes:
    """


class NotaryProperties(TypedDict):
    """A notary.

    References:
        https://schema.org/Notary
    Note:
        Model Depth 5
    Attributes:
    """


class NotaryAllProperties(NotaryInheritedProperties, NotaryProperties, TypedDict):
    pass


class NotaryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Notary", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NotaryProperties, NotaryInheritedProperties, NotaryAllProperties
    ] = NotaryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Notary"
    return model


Notary = create_schema_org_model()


def create_notary_model(
    model: Union[NotaryProperties, NotaryInheritedProperties, NotaryAllProperties]
):
    _type = deepcopy(NotaryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of NotaryAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NotaryAllProperties):
    pydantic_type = create_notary_model(model=model)
    return pydantic_type(model).schema_json()
