"""
The act of achieving victory in a competitive activity.

https://schema.org/WinAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WinActionInheritedProperties(TypedDict):
    """The act of achieving victory in a competitive activity.

    References:
        https://schema.org/WinAction
    Note:
        Model Depth 4
    Attributes:
    """


class WinActionProperties(TypedDict):
    """The act of achieving victory in a competitive activity.

    References:
        https://schema.org/WinAction
    Note:
        Model Depth 4
    Attributes:
        loser: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of participant. The loser of the action.
    """

    loser: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class WinActionAllProperties(
    WinActionInheritedProperties, WinActionProperties, TypedDict
):
    pass


class WinActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WinAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"loser": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        WinActionProperties, WinActionInheritedProperties, WinActionAllProperties
    ] = WinActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WinAction"
    return model


WinAction = create_schema_org_model()


def create_winaction_model(
    model: Union[
        WinActionProperties, WinActionInheritedProperties, WinActionAllProperties
    ]
):
    _type = deepcopy(WinActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WinActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WinActionAllProperties):
    pydantic_type = create_winaction_model(model=model)
    return pydantic_type(model).schema_json()
