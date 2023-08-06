"""
An international trial.

https://schema.org/InternationalTrial
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InternationalTrialInheritedProperties(TypedDict):
    """An international trial.

    References:
        https://schema.org/InternationalTrial
    Note:
        Model Depth 6
    Attributes:
    """


class InternationalTrialProperties(TypedDict):
    """An international trial.

    References:
        https://schema.org/InternationalTrial
    Note:
        Model Depth 6
    Attributes:
    """


class InternationalTrialAllProperties(
    InternationalTrialInheritedProperties, InternationalTrialProperties, TypedDict
):
    pass


class InternationalTrialBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="InternationalTrial", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        InternationalTrialProperties,
        InternationalTrialInheritedProperties,
        InternationalTrialAllProperties,
    ] = InternationalTrialAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InternationalTrial"
    return model


InternationalTrial = create_schema_org_model()


def create_internationaltrial_model(
    model: Union[
        InternationalTrialProperties,
        InternationalTrialInheritedProperties,
        InternationalTrialAllProperties,
    ]
):
    _type = deepcopy(InternationalTrialAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of InternationalTrial. Please see: https://schema.org/InternationalTrial"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: InternationalTrialAllProperties):
    pydantic_type = create_internationaltrial_model(model=model)
    return pydantic_type(model).schema_json()
