"""
A mountain, like Mount Whitney or Mount Everest.

https://schema.org/Mountain
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MountainInheritedProperties(TypedDict):
    """A mountain, like Mount Whitney or Mount Everest.

    References:
        https://schema.org/Mountain
    Note:
        Model Depth 4
    Attributes:
    """


class MountainProperties(TypedDict):
    """A mountain, like Mount Whitney or Mount Everest.

    References:
        https://schema.org/Mountain
    Note:
        Model Depth 4
    Attributes:
    """


class MountainAllProperties(MountainInheritedProperties, MountainProperties, TypedDict):
    pass


class MountainBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Mountain", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MountainProperties, MountainInheritedProperties, MountainAllProperties
    ] = MountainAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Mountain"
    return model


Mountain = create_schema_org_model()


def create_mountain_model(
    model: Union[MountainProperties, MountainInheritedProperties, MountainAllProperties]
):
    _type = deepcopy(MountainAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MountainAllProperties):
    pydantic_type = create_mountain_model(model=model)
    return pydantic_type(model).schema_json()
