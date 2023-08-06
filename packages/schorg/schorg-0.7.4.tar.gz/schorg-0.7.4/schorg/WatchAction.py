"""
The act of consuming dynamic/moving visual content.

https://schema.org/WatchAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WatchActionInheritedProperties(TypedDict):
    """The act of consuming dynamic/moving visual content.

    References:
        https://schema.org/WatchAction
    Note:
        Model Depth 4
    Attributes:
        actionAccessibilityRequirement: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A set of requirements that must be fulfilled in order to perform an Action. If more than one value is specified, fulfilling one set of requirements will allow the Action to be performed.
        expectsAcceptanceOf: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.
    """

    actionAccessibilityRequirement: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    expectsAcceptanceOf: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class WatchActionProperties(TypedDict):
    """The act of consuming dynamic/moving visual content.

    References:
        https://schema.org/WatchAction
    Note:
        Model Depth 4
    Attributes:
    """


class WatchActionAllProperties(
    WatchActionInheritedProperties, WatchActionProperties, TypedDict
):
    pass


class WatchActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WatchAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"actionAccessibilityRequirement": {"exclude": True}}
        fields = {"expectsAcceptanceOf": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        WatchActionProperties, WatchActionInheritedProperties, WatchActionAllProperties
    ] = WatchActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WatchAction"
    return model


WatchAction = create_schema_org_model()


def create_watchaction_model(
    model: Union[
        WatchActionProperties, WatchActionInheritedProperties, WatchActionAllProperties
    ]
):
    _type = deepcopy(WatchActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WatchActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WatchActionAllProperties):
    pydantic_type = create_watchaction_model(model=model)
    return pydantic_type(model).schema_json()
