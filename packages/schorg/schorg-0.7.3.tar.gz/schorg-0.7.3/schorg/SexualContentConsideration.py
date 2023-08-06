"""
The item contains sexually oriented content such as nudity, suggestive or explicit material, or related online services, or is intended to enhance sexual activity. Examples: Erotic videos or magazine, sexual enhancement devices, sex toys.

https://schema.org/SexualContentConsideration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SexualContentConsiderationInheritedProperties(TypedDict):
    """The item contains sexually oriented content such as nudity, suggestive or explicit material, or related online services, or is intended to enhance sexual activity. Examples: Erotic videos or magazine, sexual enhancement devices, sex toys.

    References:
        https://schema.org/SexualContentConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class SexualContentConsiderationProperties(TypedDict):
    """The item contains sexually oriented content such as nudity, suggestive or explicit material, or related online services, or is intended to enhance sexual activity. Examples: Erotic videos or magazine, sexual enhancement devices, sex toys.

    References:
        https://schema.org/SexualContentConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class SexualContentConsiderationAllProperties(
    SexualContentConsiderationInheritedProperties,
    SexualContentConsiderationProperties,
    TypedDict,
):
    pass


class SexualContentConsiderationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SexualContentConsideration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SexualContentConsiderationProperties,
        SexualContentConsiderationInheritedProperties,
        SexualContentConsiderationAllProperties,
    ] = SexualContentConsiderationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SexualContentConsideration"
    return model


SexualContentConsideration = create_schema_org_model()


def create_sexualcontentconsideration_model(
    model: Union[
        SexualContentConsiderationProperties,
        SexualContentConsiderationInheritedProperties,
        SexualContentConsiderationAllProperties,
    ]
):
    _type = deepcopy(SexualContentConsiderationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SexualContentConsiderationAllProperties):
    pydantic_type = create_sexualcontentconsideration_model(model=model)
    return pydantic_type(model).schema_json()
