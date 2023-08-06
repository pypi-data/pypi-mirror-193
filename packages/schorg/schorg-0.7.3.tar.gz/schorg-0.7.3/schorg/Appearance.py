"""
Appearance assessment with clinical examination.

https://schema.org/Appearance
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AppearanceInheritedProperties(TypedDict):
    """Appearance assessment with clinical examination.

    References:
        https://schema.org/Appearance
    Note:
        Model Depth 5
    Attributes:
    """


class AppearanceProperties(TypedDict):
    """Appearance assessment with clinical examination.

    References:
        https://schema.org/Appearance
    Note:
        Model Depth 5
    Attributes:
    """


class AppearanceAllProperties(
    AppearanceInheritedProperties, AppearanceProperties, TypedDict
):
    pass


class AppearanceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Appearance", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AppearanceProperties, AppearanceInheritedProperties, AppearanceAllProperties
    ] = AppearanceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Appearance"
    return model


Appearance = create_schema_org_model()


def create_appearance_model(
    model: Union[
        AppearanceProperties, AppearanceInheritedProperties, AppearanceAllProperties
    ]
):
    _type = deepcopy(AppearanceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AppearanceAllProperties):
    pydantic_type = create_appearance_model(model=model)
    return pydantic_type(model).schema_json()
