"""
Physical activity that is engaged in to improve muscle and bone strength. Also referred to as resistance training.

https://schema.org/StrengthTraining
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class StrengthTrainingInheritedProperties(TypedDict):
    """Physical activity that is engaged in to improve muscle and bone strength. Also referred to as resistance training.

    References:
        https://schema.org/StrengthTraining
    Note:
        Model Depth 5
    Attributes:
    """


class StrengthTrainingProperties(TypedDict):
    """Physical activity that is engaged in to improve muscle and bone strength. Also referred to as resistance training.

    References:
        https://schema.org/StrengthTraining
    Note:
        Model Depth 5
    Attributes:
    """


class StrengthTrainingAllProperties(
    StrengthTrainingInheritedProperties, StrengthTrainingProperties, TypedDict
):
    pass


class StrengthTrainingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="StrengthTraining", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        StrengthTrainingProperties,
        StrengthTrainingInheritedProperties,
        StrengthTrainingAllProperties,
    ] = StrengthTrainingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "StrengthTraining"
    return model


StrengthTraining = create_schema_org_model()


def create_strengthtraining_model(
    model: Union[
        StrengthTrainingProperties,
        StrengthTrainingInheritedProperties,
        StrengthTrainingAllProperties,
    ]
):
    _type = deepcopy(StrengthTrainingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of StrengthTraining. Please see: https://schema.org/StrengthTraining"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: StrengthTrainingAllProperties):
    pydantic_type = create_strengthtraining_model(model=model)
    return pydantic_type(model).schema_json()
