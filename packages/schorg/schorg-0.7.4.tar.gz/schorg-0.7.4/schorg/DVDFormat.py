"""
DVDFormat.

https://schema.org/DVDFormat
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DVDFormatInheritedProperties(TypedDict):
    """DVDFormat.

    References:
        https://schema.org/DVDFormat
    Note:
        Model Depth 5
    Attributes:
    """


class DVDFormatProperties(TypedDict):
    """DVDFormat.

    References:
        https://schema.org/DVDFormat
    Note:
        Model Depth 5
    Attributes:
    """


class DVDFormatAllProperties(
    DVDFormatInheritedProperties, DVDFormatProperties, TypedDict
):
    pass


class DVDFormatBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DVDFormat", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DVDFormatProperties, DVDFormatInheritedProperties, DVDFormatAllProperties
    ] = DVDFormatAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DVDFormat"
    return model


DVDFormat = create_schema_org_model()


def create_dvdformat_model(
    model: Union[
        DVDFormatProperties, DVDFormatInheritedProperties, DVDFormatAllProperties
    ]
):
    _type = deepcopy(DVDFormatAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DVDFormatAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DVDFormatAllProperties):
    pydantic_type = create_dvdformat_model(model=model)
    return pydantic_type(model).schema_json()
