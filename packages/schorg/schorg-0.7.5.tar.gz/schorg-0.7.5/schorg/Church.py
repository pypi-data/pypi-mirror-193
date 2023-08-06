"""
A church.

https://schema.org/Church
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ChurchInheritedProperties(TypedDict):
    """A church.

    References:
        https://schema.org/Church
    Note:
        Model Depth 5
    Attributes:
    """


class ChurchProperties(TypedDict):
    """A church.

    References:
        https://schema.org/Church
    Note:
        Model Depth 5
    Attributes:
    """


class ChurchAllProperties(ChurchInheritedProperties, ChurchProperties, TypedDict):
    pass


class ChurchBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Church", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ChurchProperties, ChurchInheritedProperties, ChurchAllProperties
    ] = ChurchAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Church"
    return model


Church = create_schema_org_model()


def create_church_model(
    model: Union[ChurchProperties, ChurchInheritedProperties, ChurchAllProperties]
):
    _type = deepcopy(ChurchAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Church. Please see: https://schema.org/Church"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ChurchAllProperties):
    pydantic_type = create_church_model(model=model)
    return pydantic_type(model).schema_json()
