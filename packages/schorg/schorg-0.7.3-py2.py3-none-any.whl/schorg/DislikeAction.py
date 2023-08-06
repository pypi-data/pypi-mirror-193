"""
The act of expressing a negative sentiment about the object. An agent dislikes an object (a proposition, topic or theme) with participants.

https://schema.org/DislikeAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DislikeActionInheritedProperties(TypedDict):
    """The act of expressing a negative sentiment about the object. An agent dislikes an object (a proposition, topic or theme) with participants.

    References:
        https://schema.org/DislikeAction
    Note:
        Model Depth 5
    Attributes:
    """


class DislikeActionProperties(TypedDict):
    """The act of expressing a negative sentiment about the object. An agent dislikes an object (a proposition, topic or theme) with participants.

    References:
        https://schema.org/DislikeAction
    Note:
        Model Depth 5
    Attributes:
    """


class DislikeActionAllProperties(
    DislikeActionInheritedProperties, DislikeActionProperties, TypedDict
):
    pass


class DislikeActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DislikeAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DislikeActionProperties,
        DislikeActionInheritedProperties,
        DislikeActionAllProperties,
    ] = DislikeActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DislikeAction"
    return model


DislikeAction = create_schema_org_model()


def create_dislikeaction_model(
    model: Union[
        DislikeActionProperties,
        DislikeActionInheritedProperties,
        DislikeActionAllProperties,
    ]
):
    _type = deepcopy(DislikeActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DislikeActionAllProperties):
    pydantic_type = create_dislikeaction_model(model=model)
    return pydantic_type(model).schema_json()
