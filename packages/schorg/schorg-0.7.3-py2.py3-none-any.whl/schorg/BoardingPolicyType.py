"""
A type of boarding policy used by an airline.

https://schema.org/BoardingPolicyType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BoardingPolicyTypeInheritedProperties(TypedDict):
    """A type of boarding policy used by an airline.

    References:
        https://schema.org/BoardingPolicyType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class BoardingPolicyTypeProperties(TypedDict):
    """A type of boarding policy used by an airline.

    References:
        https://schema.org/BoardingPolicyType
    Note:
        Model Depth 4
    Attributes:
    """


class BoardingPolicyTypeAllProperties(
    BoardingPolicyTypeInheritedProperties, BoardingPolicyTypeProperties, TypedDict
):
    pass


class BoardingPolicyTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BoardingPolicyType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BoardingPolicyTypeProperties,
        BoardingPolicyTypeInheritedProperties,
        BoardingPolicyTypeAllProperties,
    ] = BoardingPolicyTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BoardingPolicyType"
    return model


BoardingPolicyType = create_schema_org_model()


def create_boardingpolicytype_model(
    model: Union[
        BoardingPolicyTypeProperties,
        BoardingPolicyTypeInheritedProperties,
        BoardingPolicyTypeAllProperties,
    ]
):
    _type = deepcopy(BoardingPolicyTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BoardingPolicyTypeAllProperties):
    pydantic_type = create_boardingpolicytype_model(model=model)
    return pydantic_type(model).schema_json()
