"""
Physical activity of relatively low intensity that depends primarily on the aerobic energy-generating process; during activity, the aerobic metabolism uses oxygen to adequately meet energy demands during exercise.

https://schema.org/AerobicActivity
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AerobicActivityInheritedProperties(TypedDict):
    """Physical activity of relatively low intensity that depends primarily on the aerobic energy-generating process; during activity, the aerobic metabolism uses oxygen to adequately meet energy demands during exercise.

    References:
        https://schema.org/AerobicActivity
    Note:
        Model Depth 5
    Attributes:
    """


class AerobicActivityProperties(TypedDict):
    """Physical activity of relatively low intensity that depends primarily on the aerobic energy-generating process; during activity, the aerobic metabolism uses oxygen to adequately meet energy demands during exercise.

    References:
        https://schema.org/AerobicActivity
    Note:
        Model Depth 5
    Attributes:
    """


class AerobicActivityAllProperties(
    AerobicActivityInheritedProperties, AerobicActivityProperties, TypedDict
):
    pass


class AerobicActivityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AerobicActivity", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AerobicActivityProperties,
        AerobicActivityInheritedProperties,
        AerobicActivityAllProperties,
    ] = AerobicActivityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AerobicActivity"
    return model


AerobicActivity = create_schema_org_model()


def create_aerobicactivity_model(
    model: Union[
        AerobicActivityProperties,
        AerobicActivityInheritedProperties,
        AerobicActivityAllProperties,
    ]
):
    _type = deepcopy(AerobicActivityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AerobicActivityAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AerobicActivityAllProperties):
    pydantic_type = create_aerobicactivity_model(model=model)
    return pydantic_type(model).schema_json()
