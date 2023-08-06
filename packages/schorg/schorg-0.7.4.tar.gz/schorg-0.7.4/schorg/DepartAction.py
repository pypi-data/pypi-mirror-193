"""
The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants.

https://schema.org/DepartAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DepartActionInheritedProperties(TypedDict):
    """The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants.

    References:
        https://schema.org/DepartAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fromLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class DepartActionProperties(TypedDict):
    """The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants.

    References:
        https://schema.org/DepartAction
    Note:
        Model Depth 4
    Attributes:
    """


class DepartActionAllProperties(
    DepartActionInheritedProperties, DepartActionProperties, TypedDict
):
    pass


class DepartActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DepartAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"toLocation": {"exclude": True}}
        fields = {"fromLocation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DepartActionProperties,
        DepartActionInheritedProperties,
        DepartActionAllProperties,
    ] = DepartActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DepartAction"
    return model


DepartAction = create_schema_org_model()


def create_departaction_model(
    model: Union[
        DepartActionProperties,
        DepartActionInheritedProperties,
        DepartActionAllProperties,
    ]
):
    _type = deepcopy(DepartActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DepartActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DepartActionAllProperties):
    pydantic_type = create_departaction_model(model=model)
    return pydantic_type(model).schema_json()
