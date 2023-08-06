"""
The act of producing a painting, typically with paint and canvas as instruments.

https://schema.org/PaintAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaintActionInheritedProperties(TypedDict):
    """The act of producing a painting, typically with paint and canvas as instruments.

    References:
        https://schema.org/PaintAction
    Note:
        Model Depth 4
    Attributes:
    """


class PaintActionProperties(TypedDict):
    """The act of producing a painting, typically with paint and canvas as instruments.

    References:
        https://schema.org/PaintAction
    Note:
        Model Depth 4
    Attributes:
    """


class PaintActionAllProperties(
    PaintActionInheritedProperties, PaintActionProperties, TypedDict
):
    pass


class PaintActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PaintAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PaintActionProperties, PaintActionInheritedProperties, PaintActionAllProperties
    ] = PaintActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaintAction"
    return model


PaintAction = create_schema_org_model()


def create_paintaction_model(
    model: Union[
        PaintActionProperties, PaintActionInheritedProperties, PaintActionAllProperties
    ]
):
    _type = deepcopy(PaintActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of PaintAction. Please see: https://schema.org/PaintAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PaintActionAllProperties):
    pydantic_type = create_paintaction_model(model=model)
    return pydantic_type(model).schema_json()
