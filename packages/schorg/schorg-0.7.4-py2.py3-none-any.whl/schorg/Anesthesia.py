"""
A specific branch of medical science that pertains to study of anesthetics and their application.

https://schema.org/Anesthesia
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AnesthesiaInheritedProperties(TypedDict):
    """A specific branch of medical science that pertains to study of anesthetics and their application.

    References:
        https://schema.org/Anesthesia
    Note:
        Model Depth 6
    Attributes:
    """


class AnesthesiaProperties(TypedDict):
    """A specific branch of medical science that pertains to study of anesthetics and their application.

    References:
        https://schema.org/Anesthesia
    Note:
        Model Depth 6
    Attributes:
    """


class AnesthesiaAllProperties(
    AnesthesiaInheritedProperties, AnesthesiaProperties, TypedDict
):
    pass


class AnesthesiaBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Anesthesia", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AnesthesiaProperties, AnesthesiaInheritedProperties, AnesthesiaAllProperties
    ] = AnesthesiaAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Anesthesia"
    return model


Anesthesia = create_schema_org_model()


def create_anesthesia_model(
    model: Union[
        AnesthesiaProperties, AnesthesiaInheritedProperties, AnesthesiaAllProperties
    ]
):
    _type = deepcopy(AnesthesiaAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AnesthesiaAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AnesthesiaAllProperties):
    pydantic_type = create_anesthesia_model(model=model)
    return pydantic_type(model).schema_json()
