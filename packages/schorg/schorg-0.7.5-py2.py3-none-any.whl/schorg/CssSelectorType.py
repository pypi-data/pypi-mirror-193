"""
Text representing a CSS selector.

https://schema.org/CssSelectorType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CssSelectorTypeInheritedProperties(TypedDict):
    """Text representing a CSS selector.

    References:
        https://schema.org/CssSelectorType
    Note:
        Model Depth 6
    Attributes:
    """


class CssSelectorTypeProperties(TypedDict):
    """Text representing a CSS selector.

    References:
        https://schema.org/CssSelectorType
    Note:
        Model Depth 6
    Attributes:
    """


class CssSelectorTypeAllProperties(
    CssSelectorTypeInheritedProperties, CssSelectorTypeProperties, TypedDict
):
    pass


class CssSelectorTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CssSelectorType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CssSelectorTypeProperties,
        CssSelectorTypeInheritedProperties,
        CssSelectorTypeAllProperties,
    ] = CssSelectorTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CssSelectorType"
    return model


CssSelectorType = create_schema_org_model()


def create_cssselectortype_model(
    model: Union[
        CssSelectorTypeProperties,
        CssSelectorTypeInheritedProperties,
        CssSelectorTypeAllProperties,
    ]
):
    _type = deepcopy(CssSelectorTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of CssSelectorType. Please see: https://schema.org/CssSelectorType"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CssSelectorTypeAllProperties):
    pydantic_type = create_cssselectortype_model(model=model)
    return pydantic_type(model).schema_json()
