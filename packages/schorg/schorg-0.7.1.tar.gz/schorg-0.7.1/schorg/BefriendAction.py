"""
The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically.Related actions:* [[FollowAction]]: Unlike FollowAction, BefriendAction implies that the connection is reciprocal.

https://schema.org/BefriendAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(BefriendActionInheritedProperties , BefriendActionProperties, TypedDict):
    pass


class BefriendActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BefriendAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BefriendActionProperties, BefriendActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BefriendAction"
    return model
    

BefriendAction = create_schema_org_model()


def create_befriendaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_befriendaction_model(model=model)
    return pydantic_type(model).schema_json()


