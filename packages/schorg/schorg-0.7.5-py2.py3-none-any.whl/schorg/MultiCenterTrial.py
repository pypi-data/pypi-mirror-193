"""
A trial that takes place at multiple centers.

https://schema.org/MultiCenterTrial
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MultiCenterTrialInheritedProperties(TypedDict):
    """A trial that takes place at multiple centers.

    References:
        https://schema.org/MultiCenterTrial
    Note:
        Model Depth 6
    Attributes:
    """


class MultiCenterTrialProperties(TypedDict):
    """A trial that takes place at multiple centers.

    References:
        https://schema.org/MultiCenterTrial
    Note:
        Model Depth 6
    Attributes:
    """


class MultiCenterTrialAllProperties(
    MultiCenterTrialInheritedProperties, MultiCenterTrialProperties, TypedDict
):
    pass


class MultiCenterTrialBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MultiCenterTrial", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MultiCenterTrialProperties,
        MultiCenterTrialInheritedProperties,
        MultiCenterTrialAllProperties,
    ] = MultiCenterTrialAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MultiCenterTrial"
    return model


MultiCenterTrial = create_schema_org_model()


def create_multicentertrial_model(
    model: Union[
        MultiCenterTrialProperties,
        MultiCenterTrialInheritedProperties,
        MultiCenterTrialAllProperties,
    ]
):
    _type = deepcopy(MultiCenterTrialAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MultiCenterTrial. Please see: https://schema.org/MultiCenterTrial"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MultiCenterTrialAllProperties):
    pydantic_type = create_multicentertrial_model(model=model)
    return pydantic_type(model).schema_json()
