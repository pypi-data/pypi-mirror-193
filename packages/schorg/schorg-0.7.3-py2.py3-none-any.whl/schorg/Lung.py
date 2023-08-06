"""
Lung and respiratory system clinical examination.

https://schema.org/Lung
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LungInheritedProperties(TypedDict):
    """Lung and respiratory system clinical examination.

    References:
        https://schema.org/Lung
    Note:
        Model Depth 5
    Attributes:
    """


class LungProperties(TypedDict):
    """Lung and respiratory system clinical examination.

    References:
        https://schema.org/Lung
    Note:
        Model Depth 5
    Attributes:
    """


class LungAllProperties(LungInheritedProperties, LungProperties, TypedDict):
    pass


class LungBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Lung", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LungProperties, LungInheritedProperties, LungAllProperties
    ] = LungAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Lung"
    return model


Lung = create_schema_org_model()


def create_lung_model(
    model: Union[LungProperties, LungInheritedProperties, LungAllProperties]
):
    _type = deepcopy(LungAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LungAllProperties):
    pydantic_type = create_lung_model(model=model)
    return pydantic_type(model).schema_json()
