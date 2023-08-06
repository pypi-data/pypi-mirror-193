"""
Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations.

https://schema.org/Nonprofit501e
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501eInheritedProperties(TypedDict):
    """Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations.

    References:
        https://schema.org/Nonprofit501e
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501eProperties(TypedDict):
    """Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations.

    References:
        https://schema.org/Nonprofit501e
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501eAllProperties(
    Nonprofit501eInheritedProperties, Nonprofit501eProperties, TypedDict
):
    pass


class Nonprofit501eBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501e", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501eProperties,
        Nonprofit501eInheritedProperties,
        Nonprofit501eAllProperties,
    ] = Nonprofit501eAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501e"
    return model


Nonprofit501e = create_schema_org_model()


def create_nonprofit501e_model(
    model: Union[
        Nonprofit501eProperties,
        Nonprofit501eInheritedProperties,
        Nonprofit501eAllProperties,
    ]
):
    _type = deepcopy(Nonprofit501eAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Nonprofit501e. Please see: https://schema.org/Nonprofit501e"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: Nonprofit501eAllProperties):
    pydantic_type = create_nonprofit501e_model(model=model)
    return pydantic_type(model).schema_json()
