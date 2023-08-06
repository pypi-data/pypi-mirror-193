"""
Physical activity that is of high-intensity which utilizes the anaerobic metabolism of the body.

https://schema.org/AnaerobicActivity
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AnaerobicActivityInheritedProperties(TypedDict):
    """Physical activity that is of high-intensity which utilizes the anaerobic metabolism of the body.

    References:
        https://schema.org/AnaerobicActivity
    Note:
        Model Depth 5
    Attributes:
    """


class AnaerobicActivityProperties(TypedDict):
    """Physical activity that is of high-intensity which utilizes the anaerobic metabolism of the body.

    References:
        https://schema.org/AnaerobicActivity
    Note:
        Model Depth 5
    Attributes:
    """


class AnaerobicActivityAllProperties(
    AnaerobicActivityInheritedProperties, AnaerobicActivityProperties, TypedDict
):
    pass


class AnaerobicActivityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AnaerobicActivity", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AnaerobicActivityProperties,
        AnaerobicActivityInheritedProperties,
        AnaerobicActivityAllProperties,
    ] = AnaerobicActivityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AnaerobicActivity"
    return model


AnaerobicActivity = create_schema_org_model()


def create_anaerobicactivity_model(
    model: Union[
        AnaerobicActivityProperties,
        AnaerobicActivityInheritedProperties,
        AnaerobicActivityAllProperties,
    ]
):
    _type = deepcopy(AnaerobicActivityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AnaerobicActivityAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AnaerobicActivityAllProperties):
    pydantic_type = create_anaerobicactivity_model(model=model)
    return pydantic_type(model).schema_json()
