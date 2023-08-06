"""
EPRelease.

https://schema.org/EPRelease
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EPReleaseInheritedProperties(TypedDict):
    """EPRelease.

    References:
        https://schema.org/EPRelease
    Note:
        Model Depth 5
    Attributes:
    """


class EPReleaseProperties(TypedDict):
    """EPRelease.

    References:
        https://schema.org/EPRelease
    Note:
        Model Depth 5
    Attributes:
    """


class EPReleaseAllProperties(
    EPReleaseInheritedProperties, EPReleaseProperties, TypedDict
):
    pass


class EPReleaseBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EPRelease", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EPReleaseProperties, EPReleaseInheritedProperties, EPReleaseAllProperties
    ] = EPReleaseAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EPRelease"
    return model


EPRelease = create_schema_org_model()


def create_eprelease_model(
    model: Union[
        EPReleaseProperties, EPReleaseInheritedProperties, EPReleaseAllProperties
    ]
):
    _type = deepcopy(EPReleaseAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of EPRelease. Please see: https://schema.org/EPRelease"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: EPReleaseAllProperties):
    pydantic_type = create_eprelease_model(model=model)
    return pydantic_type(model).schema_json()
