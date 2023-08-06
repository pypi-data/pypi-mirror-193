"""
The conventional Western system of medicine, that aims to apply the best available evidence gained from the scientific method to clinical decision making. Also known as conventional or Western medicine.

https://schema.org/WesternConventional
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WesternConventionalInheritedProperties(TypedDict):
    """The conventional Western system of medicine, that aims to apply the best available evidence gained from the scientific method to clinical decision making. Also known as conventional or Western medicine.

    References:
        https://schema.org/WesternConventional
    Note:
        Model Depth 6
    Attributes:
    """


class WesternConventionalProperties(TypedDict):
    """The conventional Western system of medicine, that aims to apply the best available evidence gained from the scientific method to clinical decision making. Also known as conventional or Western medicine.

    References:
        https://schema.org/WesternConventional
    Note:
        Model Depth 6
    Attributes:
    """


class WesternConventionalAllProperties(
    WesternConventionalInheritedProperties, WesternConventionalProperties, TypedDict
):
    pass


class WesternConventionalBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WesternConventional", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WesternConventionalProperties,
        WesternConventionalInheritedProperties,
        WesternConventionalAllProperties,
    ] = WesternConventionalAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WesternConventional"
    return model


WesternConventional = create_schema_org_model()


def create_westernconventional_model(
    model: Union[
        WesternConventionalProperties,
        WesternConventionalInheritedProperties,
        WesternConventionalAllProperties,
    ]
):
    _type = deepcopy(WesternConventionalAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WesternConventionalAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WesternConventionalAllProperties):
    pydantic_type = create_westernconventional_model(model=model)
    return pydantic_type(model).schema_json()
