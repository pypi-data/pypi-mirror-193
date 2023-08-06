"""
A gym.

https://schema.org/ExerciseGym
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ExerciseGymInheritedProperties(TypedDict):
    """A gym.

    References:
        https://schema.org/ExerciseGym
    Note:
        Model Depth 5
    Attributes:
    """


class ExerciseGymProperties(TypedDict):
    """A gym.

    References:
        https://schema.org/ExerciseGym
    Note:
        Model Depth 5
    Attributes:
    """


class ExerciseGymAllProperties(
    ExerciseGymInheritedProperties, ExerciseGymProperties, TypedDict
):
    pass


class ExerciseGymBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ExerciseGym", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ExerciseGymProperties, ExerciseGymInheritedProperties, ExerciseGymAllProperties
    ] = ExerciseGymAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ExerciseGym"
    return model


ExerciseGym = create_schema_org_model()


def create_exercisegym_model(
    model: Union[
        ExerciseGymProperties, ExerciseGymInheritedProperties, ExerciseGymAllProperties
    ]
):
    _type = deepcopy(ExerciseGymAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ExerciseGym. Please see: https://schema.org/ExerciseGym"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ExerciseGymAllProperties):
    pydantic_type = create_exercisegym_model(model=model)
    return pydantic_type(model).schema_json()
