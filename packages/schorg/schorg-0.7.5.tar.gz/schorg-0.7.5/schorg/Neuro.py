"""
Neurological system clinical examination.

https://schema.org/Neuro
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NeuroInheritedProperties(TypedDict):
    """Neurological system clinical examination.

    References:
        https://schema.org/Neuro
    Note:
        Model Depth 5
    Attributes:
    """


class NeuroProperties(TypedDict):
    """Neurological system clinical examination.

    References:
        https://schema.org/Neuro
    Note:
        Model Depth 5
    Attributes:
    """


class NeuroAllProperties(NeuroInheritedProperties, NeuroProperties, TypedDict):
    pass


class NeuroBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Neuro", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NeuroProperties, NeuroInheritedProperties, NeuroAllProperties
    ] = NeuroAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Neuro"
    return model


Neuro = create_schema_org_model()


def create_neuro_model(
    model: Union[NeuroProperties, NeuroInheritedProperties, NeuroAllProperties]
):
    _type = deepcopy(NeuroAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Neuro. Please see: https://schema.org/Neuro"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: NeuroAllProperties):
    pydantic_type = create_neuro_model(model=model)
    return pydantic_type(model).schema_json()
