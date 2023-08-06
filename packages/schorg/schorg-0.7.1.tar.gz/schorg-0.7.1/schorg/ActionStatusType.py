"""
The status of an Action.

https://schema.org/ActionStatusType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ActionStatusTypeInheritedProperties(TypedDict):
    """The status of an Action.

    References:
        https://schema.org/ActionStatusType
    Note:
        Model Depth 5
    Attributes:
    """

    


class ActionStatusTypeProperties(TypedDict):
    """The status of an Action.

    References:
        https://schema.org/ActionStatusType
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ActionStatusTypeInheritedProperties , ActionStatusTypeProperties, TypedDict):
    pass


class ActionStatusTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ActionStatusType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ActionStatusTypeProperties, ActionStatusTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ActionStatusType"
    return model
    

ActionStatusType = create_schema_org_model()


def create_actionstatustype_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_actionstatustype_model(model=model)
    return pydantic_type(model).schema_json()


