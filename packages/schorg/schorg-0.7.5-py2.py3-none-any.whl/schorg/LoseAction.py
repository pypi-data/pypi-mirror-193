"""
The act of being defeated in a competitive activity.

https://schema.org/LoseAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LoseActionInheritedProperties(TypedDict):
    """The act of being defeated in a competitive activity.

    References:
        https://schema.org/LoseAction
    Note:
        Model Depth 4
    Attributes:
    """


class LoseActionProperties(TypedDict):
    """The act of being defeated in a competitive activity.

    References:
        https://schema.org/LoseAction
    Note:
        Model Depth 4
    Attributes:
        winner: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The winner of the action.
    """

    winner: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class LoseActionAllProperties(
    LoseActionInheritedProperties, LoseActionProperties, TypedDict
):
    pass


class LoseActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LoseAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"winner": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        LoseActionProperties, LoseActionInheritedProperties, LoseActionAllProperties
    ] = LoseActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LoseAction"
    return model


LoseAction = create_schema_org_model()


def create_loseaction_model(
    model: Union[
        LoseActionProperties, LoseActionInheritedProperties, LoseActionAllProperties
    ]
):
    _type = deepcopy(LoseActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of LoseAction. Please see: https://schema.org/LoseAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: LoseActionAllProperties):
    pydantic_type = create_loseaction_model(model=model)
    return pydantic_type(model).schema_json()
