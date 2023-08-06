"""
Head assessment with clinical examination.

https://schema.org/Head
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HeadInheritedProperties(TypedDict):
    """Head assessment with clinical examination.

    References:
        https://schema.org/Head
    Note:
        Model Depth 5
    Attributes:
    """


class HeadProperties(TypedDict):
    """Head assessment with clinical examination.

    References:
        https://schema.org/Head
    Note:
        Model Depth 5
    Attributes:
    """


class HeadAllProperties(HeadInheritedProperties, HeadProperties, TypedDict):
    pass


class HeadBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Head", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HeadProperties, HeadInheritedProperties, HeadAllProperties
    ] = HeadAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Head"
    return model


Head = create_schema_org_model()


def create_head_model(
    model: Union[HeadProperties, HeadInheritedProperties, HeadAllProperties]
):
    _type = deepcopy(HeadAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Head. Please see: https://schema.org/Head"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: HeadAllProperties):
    pydantic_type = create_head_model(model=model)
    return pydantic_type(model).schema_json()
