"""
A diet conforming to Jewish dietary practices.

https://schema.org/KosherDiet
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class KosherDietInheritedProperties(TypedDict):
    """A diet conforming to Jewish dietary practices.

    References:
        https://schema.org/KosherDiet
    Note:
        Model Depth 5
    Attributes:
    """


class KosherDietProperties(TypedDict):
    """A diet conforming to Jewish dietary practices.

    References:
        https://schema.org/KosherDiet
    Note:
        Model Depth 5
    Attributes:
    """


class KosherDietAllProperties(
    KosherDietInheritedProperties, KosherDietProperties, TypedDict
):
    pass


class KosherDietBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="KosherDiet", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        KosherDietProperties, KosherDietInheritedProperties, KosherDietAllProperties
    ] = KosherDietAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "KosherDiet"
    return model


KosherDiet = create_schema_org_model()


def create_kosherdiet_model(
    model: Union[
        KosherDietProperties, KosherDietInheritedProperties, KosherDietAllProperties
    ]
):
    _type = deepcopy(KosherDietAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: KosherDietAllProperties):
    pydantic_type = create_kosherdiet_model(model=model)
    return pydantic_type(model).schema_json()
