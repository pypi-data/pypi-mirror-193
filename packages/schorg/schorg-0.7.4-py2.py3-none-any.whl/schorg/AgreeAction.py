"""
The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition, topic or theme) with participants.

https://schema.org/AgreeAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AgreeActionInheritedProperties(TypedDict):
    """The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition, topic or theme) with participants.

    References:
        https://schema.org/AgreeAction
    Note:
        Model Depth 5
    Attributes:
    """


class AgreeActionProperties(TypedDict):
    """The act of expressing a consistency of opinion with the object. An agent agrees to/about an object (a proposition, topic or theme) with participants.

    References:
        https://schema.org/AgreeAction
    Note:
        Model Depth 5
    Attributes:
    """


class AgreeActionAllProperties(
    AgreeActionInheritedProperties, AgreeActionProperties, TypedDict
):
    pass


class AgreeActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AgreeAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AgreeActionProperties, AgreeActionInheritedProperties, AgreeActionAllProperties
    ] = AgreeActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AgreeAction"
    return model


AgreeAction = create_schema_org_model()


def create_agreeaction_model(
    model: Union[
        AgreeActionProperties, AgreeActionInheritedProperties, AgreeActionAllProperties
    ]
):
    _type = deepcopy(AgreeActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AgreeActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AgreeActionAllProperties):
    pydantic_type = create_agreeaction_model(model=model)
    return pydantic_type(model).schema_json()
