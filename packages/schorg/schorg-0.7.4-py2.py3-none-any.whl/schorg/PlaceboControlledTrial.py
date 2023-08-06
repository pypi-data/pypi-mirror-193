"""
A placebo-controlled trial design.

https://schema.org/PlaceboControlledTrial
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PlaceboControlledTrialInheritedProperties(TypedDict):
    """A placebo-controlled trial design.

    References:
        https://schema.org/PlaceboControlledTrial
    Note:
        Model Depth 6
    Attributes:
    """


class PlaceboControlledTrialProperties(TypedDict):
    """A placebo-controlled trial design.

    References:
        https://schema.org/PlaceboControlledTrial
    Note:
        Model Depth 6
    Attributes:
    """


class PlaceboControlledTrialAllProperties(
    PlaceboControlledTrialInheritedProperties,
    PlaceboControlledTrialProperties,
    TypedDict,
):
    pass


class PlaceboControlledTrialBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PlaceboControlledTrial", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PlaceboControlledTrialProperties,
        PlaceboControlledTrialInheritedProperties,
        PlaceboControlledTrialAllProperties,
    ] = PlaceboControlledTrialAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PlaceboControlledTrial"
    return model


PlaceboControlledTrial = create_schema_org_model()


def create_placebocontrolledtrial_model(
    model: Union[
        PlaceboControlledTrialProperties,
        PlaceboControlledTrialInheritedProperties,
        PlaceboControlledTrialAllProperties,
    ]
):
    _type = deepcopy(PlaceboControlledTrialAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PlaceboControlledTrialAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PlaceboControlledTrialAllProperties):
    pydantic_type = create_placebocontrolledtrial_model(model=model)
    return pydantic_type(model).schema_json()
