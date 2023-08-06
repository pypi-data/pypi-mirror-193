"""
The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants.

https://schema.org/TravelAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TravelActionInheritedProperties(TypedDict):
    """The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants.

    References:
        https://schema.org/TravelAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fromLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class TravelActionProperties(TypedDict):
    """The act of traveling from a fromLocation to a destination by a specified mode of transport, optionally with participants.

    References:
        https://schema.org/TravelAction
    Note:
        Model Depth 4
    Attributes:
        distance: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The distance travelled, e.g. exercising or travelling.
    """

    distance: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class TravelActionAllProperties(
    TravelActionInheritedProperties, TravelActionProperties, TypedDict
):
    pass


class TravelActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TravelAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"toLocation": {"exclude": True}}
        fields = {"fromLocation": {"exclude": True}}
        fields = {"distance": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        TravelActionProperties,
        TravelActionInheritedProperties,
        TravelActionAllProperties,
    ] = TravelActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TravelAction"
    return model


TravelAction = create_schema_org_model()


def create_travelaction_model(
    model: Union[
        TravelActionProperties,
        TravelActionInheritedProperties,
        TravelActionAllProperties,
    ]
):
    _type = deepcopy(TravelActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TravelAction. Please see: https://schema.org/TravelAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TravelActionAllProperties):
    pydantic_type = create_travelaction_model(model=model)
    return pydantic_type(model).schema_json()
