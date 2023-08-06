"""
The act of responding instinctively and emotionally to an object, expressing a sentiment.

https://schema.org/ReactAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReactActionInheritedProperties(TypedDict):
    """The act of responding instinctively and emotionally to an object, expressing a sentiment.

    References:
        https://schema.org/ReactAction
    Note:
        Model Depth 4
    Attributes:
    """


class ReactActionProperties(TypedDict):
    """The act of responding instinctively and emotionally to an object, expressing a sentiment.

    References:
        https://schema.org/ReactAction
    Note:
        Model Depth 4
    Attributes:
    """


class ReactActionAllProperties(
    ReactActionInheritedProperties, ReactActionProperties, TypedDict
):
    pass


class ReactActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReactAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReactActionProperties, ReactActionInheritedProperties, ReactActionAllProperties
    ] = ReactActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReactAction"
    return model


ReactAction = create_schema_org_model()


def create_reactaction_model(
    model: Union[
        ReactActionProperties, ReactActionInheritedProperties, ReactActionAllProperties
    ]
):
    _type = deepcopy(ReactActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ReactAction. Please see: https://schema.org/ReactAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ReactActionAllProperties):
    pydantic_type = create_reactaction_model(model=model)
    return pydantic_type(model).schema_json()
