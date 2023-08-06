"""
The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.

https://schema.org/DrawAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DrawActionInheritedProperties(TypedDict):
    """The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.

    References:
        https://schema.org/DrawAction
    Note:
        Model Depth 4
    Attributes:
    """


class DrawActionProperties(TypedDict):
    """The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.

    References:
        https://schema.org/DrawAction
    Note:
        Model Depth 4
    Attributes:
    """


class DrawActionAllProperties(
    DrawActionInheritedProperties, DrawActionProperties, TypedDict
):
    pass


class DrawActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DrawAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DrawActionProperties, DrawActionInheritedProperties, DrawActionAllProperties
    ] = DrawActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DrawAction"
    return model


DrawAction = create_schema_org_model()


def create_drawaction_model(
    model: Union[
        DrawActionProperties, DrawActionInheritedProperties, DrawActionAllProperties
    ]
):
    _type = deepcopy(DrawActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DrawAction. Please see: https://schema.org/DrawAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DrawActionAllProperties):
    pydantic_type = create_drawaction_model(model=model)
    return pydantic_type(model).schema_json()
