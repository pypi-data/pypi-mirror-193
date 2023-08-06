"""
For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind of game availability offered. 

https://schema.org/GameAvailabilityEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GameAvailabilityEnumerationInheritedProperties(TypedDict):
    """For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind of game availability offered.

    References:
        https://schema.org/GameAvailabilityEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class GameAvailabilityEnumerationProperties(TypedDict):
    """For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind of game availability offered.

    References:
        https://schema.org/GameAvailabilityEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class GameAvailabilityEnumerationAllProperties(
    GameAvailabilityEnumerationInheritedProperties,
    GameAvailabilityEnumerationProperties,
    TypedDict,
):
    pass


class GameAvailabilityEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GameAvailabilityEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        GameAvailabilityEnumerationProperties,
        GameAvailabilityEnumerationInheritedProperties,
        GameAvailabilityEnumerationAllProperties,
    ] = GameAvailabilityEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GameAvailabilityEnumeration"
    return model


GameAvailabilityEnumeration = create_schema_org_model()


def create_gameavailabilityenumeration_model(
    model: Union[
        GameAvailabilityEnumerationProperties,
        GameAvailabilityEnumerationInheritedProperties,
        GameAvailabilityEnumerationAllProperties,
    ]
):
    _type = deepcopy(GameAvailabilityEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of GameAvailabilityEnumeration. Please see: https://schema.org/GameAvailabilityEnumeration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: GameAvailabilityEnumerationAllProperties):
    pydantic_type = create_gameavailabilityenumeration_model(model=model)
    return pydantic_type(model).schema_json()
