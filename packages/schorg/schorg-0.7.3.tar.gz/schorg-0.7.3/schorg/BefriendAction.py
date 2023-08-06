"""
The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically.Related actions:* [[FollowAction]]: Unlike FollowAction, BefriendAction implies that the connection is reciprocal.

https://schema.org/BefriendAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BefriendActionInheritedProperties(TypedDict):
    """The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically.Related actions:* [[FollowAction]]: Unlike FollowAction, BefriendAction implies that the connection is reciprocal.

    References:
        https://schema.org/BefriendAction
    Note:
        Model Depth 4
    Attributes:
    """


class BefriendActionProperties(TypedDict):
    """The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically.Related actions:* [[FollowAction]]: Unlike FollowAction, BefriendAction implies that the connection is reciprocal.

    References:
        https://schema.org/BefriendAction
    Note:
        Model Depth 4
    Attributes:
    """


class BefriendActionAllProperties(
    BefriendActionInheritedProperties, BefriendActionProperties, TypedDict
):
    pass


class BefriendActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BefriendAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BefriendActionProperties,
        BefriendActionInheritedProperties,
        BefriendActionAllProperties,
    ] = BefriendActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BefriendAction"
    return model


BefriendAction = create_schema_org_model()


def create_befriendaction_model(
    model: Union[
        BefriendActionProperties,
        BefriendActionInheritedProperties,
        BefriendActionAllProperties,
    ]
):
    _type = deepcopy(BefriendActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BefriendActionAllProperties):
    pydantic_type = create_befriendaction_model(model=model)
    return pydantic_type(model).schema_json()
