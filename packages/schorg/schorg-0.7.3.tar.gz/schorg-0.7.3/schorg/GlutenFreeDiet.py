"""
A diet exclusive of gluten.

https://schema.org/GlutenFreeDiet
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GlutenFreeDietInheritedProperties(TypedDict):
    """A diet exclusive of gluten.

    References:
        https://schema.org/GlutenFreeDiet
    Note:
        Model Depth 5
    Attributes:
    """


class GlutenFreeDietProperties(TypedDict):
    """A diet exclusive of gluten.

    References:
        https://schema.org/GlutenFreeDiet
    Note:
        Model Depth 5
    Attributes:
    """


class GlutenFreeDietAllProperties(
    GlutenFreeDietInheritedProperties, GlutenFreeDietProperties, TypedDict
):
    pass


class GlutenFreeDietBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GlutenFreeDiet", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        GlutenFreeDietProperties,
        GlutenFreeDietInheritedProperties,
        GlutenFreeDietAllProperties,
    ] = GlutenFreeDietAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GlutenFreeDiet"
    return model


GlutenFreeDiet = create_schema_org_model()


def create_glutenfreediet_model(
    model: Union[
        GlutenFreeDietProperties,
        GlutenFreeDietInheritedProperties,
        GlutenFreeDietAllProperties,
    ]
):
    _type = deepcopy(GlutenFreeDietAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GlutenFreeDietAllProperties):
    pydantic_type = create_glutenfreediet_model(model=model)
    return pydantic_type(model).schema_json()
