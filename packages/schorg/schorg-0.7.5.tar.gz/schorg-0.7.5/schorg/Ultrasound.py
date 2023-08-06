"""
Ultrasound imaging.

https://schema.org/Ultrasound
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UltrasoundInheritedProperties(TypedDict):
    """Ultrasound imaging.

    References:
        https://schema.org/Ultrasound
    Note:
        Model Depth 6
    Attributes:
    """


class UltrasoundProperties(TypedDict):
    """Ultrasound imaging.

    References:
        https://schema.org/Ultrasound
    Note:
        Model Depth 6
    Attributes:
    """


class UltrasoundAllProperties(
    UltrasoundInheritedProperties, UltrasoundProperties, TypedDict
):
    pass


class UltrasoundBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Ultrasound", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UltrasoundProperties, UltrasoundInheritedProperties, UltrasoundAllProperties
    ] = UltrasoundAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Ultrasound"
    return model


Ultrasound = create_schema_org_model()


def create_ultrasound_model(
    model: Union[
        UltrasoundProperties, UltrasoundInheritedProperties, UltrasoundAllProperties
    ]
):
    _type = deepcopy(UltrasoundAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Ultrasound. Please see: https://schema.org/Ultrasound"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: UltrasoundAllProperties):
    pydantic_type = create_ultrasound_model(model=model)
    return pydantic_type(model).schema_json()
