"""
CDFormat.

https://schema.org/CDFormat
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CDFormatInheritedProperties(TypedDict):
    """CDFormat.

    References:
        https://schema.org/CDFormat
    Note:
        Model Depth 5
    Attributes:
    """


class CDFormatProperties(TypedDict):
    """CDFormat.

    References:
        https://schema.org/CDFormat
    Note:
        Model Depth 5
    Attributes:
    """


class CDFormatAllProperties(CDFormatInheritedProperties, CDFormatProperties, TypedDict):
    pass


class CDFormatBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CDFormat", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CDFormatProperties, CDFormatInheritedProperties, CDFormatAllProperties
    ] = CDFormatAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CDFormat"
    return model


CDFormat = create_schema_org_model()


def create_cdformat_model(
    model: Union[CDFormatProperties, CDFormatInheritedProperties, CDFormatAllProperties]
):
    _type = deepcopy(CDFormatAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of CDFormat. Please see: https://schema.org/CDFormat"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CDFormatAllProperties):
    pydantic_type = create_cdformat_model(model=model)
    return pydantic_type(model).schema_json()
