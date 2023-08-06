"""
Throat assessment with  clinical examination.

https://schema.org/Throat
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ThroatInheritedProperties(TypedDict):
    """Throat assessment with  clinical examination.

    References:
        https://schema.org/Throat
    Note:
        Model Depth 5
    Attributes:
    """


class ThroatProperties(TypedDict):
    """Throat assessment with  clinical examination.

    References:
        https://schema.org/Throat
    Note:
        Model Depth 5
    Attributes:
    """


class ThroatAllProperties(ThroatInheritedProperties, ThroatProperties, TypedDict):
    pass


class ThroatBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Throat", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ThroatProperties, ThroatInheritedProperties, ThroatAllProperties
    ] = ThroatAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Throat"
    return model


Throat = create_schema_org_model()


def create_throat_model(
    model: Union[ThroatProperties, ThroatInheritedProperties, ThroatAllProperties]
):
    _type = deepcopy(ThroatAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Throat. Please see: https://schema.org/Throat"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ThroatAllProperties):
    pydantic_type = create_throat_model(model=model)
    return pydantic_type(model).schema_json()
