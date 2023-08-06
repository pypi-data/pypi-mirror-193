"""
Indicates that a document has no particular or special standing (e.g. a republication of a law by a private publisher).

https://schema.org/UnofficialLegalValue
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UnofficialLegalValueInheritedProperties(TypedDict):
    """Indicates that a document has no particular or special standing (e.g. a republication of a law by a private publisher).

    References:
        https://schema.org/UnofficialLegalValue
    Note:
        Model Depth 5
    Attributes:
    """


class UnofficialLegalValueProperties(TypedDict):
    """Indicates that a document has no particular or special standing (e.g. a republication of a law by a private publisher).

    References:
        https://schema.org/UnofficialLegalValue
    Note:
        Model Depth 5
    Attributes:
    """


class UnofficialLegalValueAllProperties(
    UnofficialLegalValueInheritedProperties, UnofficialLegalValueProperties, TypedDict
):
    pass


class UnofficialLegalValueBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UnofficialLegalValue", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UnofficialLegalValueProperties,
        UnofficialLegalValueInheritedProperties,
        UnofficialLegalValueAllProperties,
    ] = UnofficialLegalValueAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UnofficialLegalValue"
    return model


UnofficialLegalValue = create_schema_org_model()


def create_unofficiallegalvalue_model(
    model: Union[
        UnofficialLegalValueProperties,
        UnofficialLegalValueInheritedProperties,
        UnofficialLegalValueAllProperties,
    ]
):
    _type = deepcopy(UnofficialLegalValueAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of UnofficialLegalValue. Please see: https://schema.org/UnofficialLegalValue"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: UnofficialLegalValueAllProperties):
    pydantic_type = create_unofficiallegalvalue_model(model=model)
    return pydantic_type(model).schema_json()
