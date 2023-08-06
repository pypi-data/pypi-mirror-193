"""
Indicates that the item has been discontinued.

https://schema.org/Discontinued
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DiscontinuedInheritedProperties(TypedDict):
    """Indicates that the item has been discontinued.

    References:
        https://schema.org/Discontinued
    Note:
        Model Depth 5
    Attributes:
    """


class DiscontinuedProperties(TypedDict):
    """Indicates that the item has been discontinued.

    References:
        https://schema.org/Discontinued
    Note:
        Model Depth 5
    Attributes:
    """


class DiscontinuedAllProperties(
    DiscontinuedInheritedProperties, DiscontinuedProperties, TypedDict
):
    pass


class DiscontinuedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Discontinued", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DiscontinuedProperties,
        DiscontinuedInheritedProperties,
        DiscontinuedAllProperties,
    ] = DiscontinuedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Discontinued"
    return model


Discontinued = create_schema_org_model()


def create_discontinued_model(
    model: Union[
        DiscontinuedProperties,
        DiscontinuedInheritedProperties,
        DiscontinuedAllProperties,
    ]
):
    _type = deepcopy(DiscontinuedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Discontinued. Please see: https://schema.org/Discontinued"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DiscontinuedAllProperties):
    pydantic_type = create_discontinued_model(model=model)
    return pydantic_type(model).schema_json()
