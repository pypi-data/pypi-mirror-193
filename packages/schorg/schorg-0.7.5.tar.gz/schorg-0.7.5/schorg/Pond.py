"""
A pond.

https://schema.org/Pond
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PondInheritedProperties(TypedDict):
    """A pond.

    References:
        https://schema.org/Pond
    Note:
        Model Depth 5
    Attributes:
    """


class PondProperties(TypedDict):
    """A pond.

    References:
        https://schema.org/Pond
    Note:
        Model Depth 5
    Attributes:
    """


class PondAllProperties(PondInheritedProperties, PondProperties, TypedDict):
    pass


class PondBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Pond", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PondProperties, PondInheritedProperties, PondAllProperties
    ] = PondAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Pond"
    return model


Pond = create_schema_org_model()


def create_pond_model(
    model: Union[PondProperties, PondInheritedProperties, PondAllProperties]
):
    _type = deepcopy(PondAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Pond. Please see: https://schema.org/Pond"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PondAllProperties):
    pydantic_type = create_pond_model(model=model)
    return pydantic_type(model).schema_json()
