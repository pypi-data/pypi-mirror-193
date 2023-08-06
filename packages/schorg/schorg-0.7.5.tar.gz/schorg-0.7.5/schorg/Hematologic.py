"""
A specific branch of medical science that pertains to diagnosis and treatment of disorders of blood and blood producing organs.

https://schema.org/Hematologic
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HematologicInheritedProperties(TypedDict):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of blood and blood producing organs.

    References:
        https://schema.org/Hematologic
    Note:
        Model Depth 6
    Attributes:
    """


class HematologicProperties(TypedDict):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of blood and blood producing organs.

    References:
        https://schema.org/Hematologic
    Note:
        Model Depth 6
    Attributes:
    """


class HematologicAllProperties(
    HematologicInheritedProperties, HematologicProperties, TypedDict
):
    pass


class HematologicBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Hematologic", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HematologicProperties, HematologicInheritedProperties, HematologicAllProperties
    ] = HematologicAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Hematologic"
    return model


Hematologic = create_schema_org_model()


def create_hematologic_model(
    model: Union[
        HematologicProperties, HematologicInheritedProperties, HematologicAllProperties
    ]
):
    _type = deepcopy(HematologicAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Hematologic. Please see: https://schema.org/Hematologic"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: HematologicAllProperties):
    pydantic_type = create_hematologic_model(model=model)
    return pydantic_type(model).schema_json()
