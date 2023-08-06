"""
Beauty salon.

https://schema.org/BeautySalon
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BeautySalonInheritedProperties(TypedDict):
    """Beauty salon.

    References:
        https://schema.org/BeautySalon
    Note:
        Model Depth 5
    Attributes:
    """


class BeautySalonProperties(TypedDict):
    """Beauty salon.

    References:
        https://schema.org/BeautySalon
    Note:
        Model Depth 5
    Attributes:
    """


class BeautySalonAllProperties(
    BeautySalonInheritedProperties, BeautySalonProperties, TypedDict
):
    pass


class BeautySalonBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BeautySalon", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BeautySalonProperties, BeautySalonInheritedProperties, BeautySalonAllProperties
    ] = BeautySalonAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BeautySalon"
    return model


BeautySalon = create_schema_org_model()


def create_beautysalon_model(
    model: Union[
        BeautySalonProperties, BeautySalonInheritedProperties, BeautySalonAllProperties
    ]
):
    _type = deepcopy(BeautySalonAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BeautySalon. Please see: https://schema.org/BeautySalon"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BeautySalonAllProperties):
    pydantic_type = create_beautysalon_model(model=model)
    return pydantic_type(model).schema_json()
