"""
A specific branch of medical science that is concerned with the diagnosis and treatment of diseases, debilities and provision of care to the aged.

https://schema.org/Geriatric
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GeriatricInheritedProperties(TypedDict):
    """A specific branch of medical science that is concerned with the diagnosis and treatment of diseases, debilities and provision of care to the aged.

    References:
        https://schema.org/Geriatric
    Note:
        Model Depth 5
    Attributes:
    """


class GeriatricProperties(TypedDict):
    """A specific branch of medical science that is concerned with the diagnosis and treatment of diseases, debilities and provision of care to the aged.

    References:
        https://schema.org/Geriatric
    Note:
        Model Depth 5
    Attributes:
    """


class GeriatricAllProperties(
    GeriatricInheritedProperties, GeriatricProperties, TypedDict
):
    pass


class GeriatricBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Geriatric", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        GeriatricProperties, GeriatricInheritedProperties, GeriatricAllProperties
    ] = GeriatricAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Geriatric"
    return model


Geriatric = create_schema_org_model()


def create_geriatric_model(
    model: Union[
        GeriatricProperties, GeriatricInheritedProperties, GeriatricAllProperties
    ]
):
    _type = deepcopy(GeriatricAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of GeriatricAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GeriatricAllProperties):
    pydantic_type = create_geriatric_model(model=model)
    return pydantic_type(model).schema_json()
