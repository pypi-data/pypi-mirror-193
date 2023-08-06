"""
The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.

https://schema.org/LikeAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LikeActionInheritedProperties(TypedDict):
    """The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.

    References:
        https://schema.org/LikeAction
    Note:
        Model Depth 5
    Attributes:
    """


class LikeActionProperties(TypedDict):
    """The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.

    References:
        https://schema.org/LikeAction
    Note:
        Model Depth 5
    Attributes:
    """


class LikeActionAllProperties(
    LikeActionInheritedProperties, LikeActionProperties, TypedDict
):
    pass


class LikeActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LikeAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LikeActionProperties, LikeActionInheritedProperties, LikeActionAllProperties
    ] = LikeActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LikeAction"
    return model


LikeAction = create_schema_org_model()


def create_likeaction_model(
    model: Union[
        LikeActionProperties, LikeActionInheritedProperties, LikeActionAllProperties
    ]
):
    _type = deepcopy(LikeActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of LikeActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LikeActionAllProperties):
    pydantic_type = create_likeaction_model(model=model)
    return pydantic_type(model).schema_json()
