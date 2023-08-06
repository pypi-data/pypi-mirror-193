"""
The act of un-registering from a service.Related actions:* [[RegisterAction]]: antonym of UnRegisterAction.* [[LeaveAction]]: Unlike LeaveAction, UnRegisterAction implies that you are unregistering from a service you were previously registered, rather than leaving a team/group of people.

https://schema.org/UnRegisterAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UnRegisterActionInheritedProperties(TypedDict):
    """The act of un-registering from a service.Related actions:* [[RegisterAction]]: antonym of UnRegisterAction.* [[LeaveAction]]: Unlike LeaveAction, UnRegisterAction implies that you are unregistering from a service you were previously registered, rather than leaving a team/group of people.

    References:
        https://schema.org/UnRegisterAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class UnRegisterActionProperties(TypedDict):
    """The act of un-registering from a service.Related actions:* [[RegisterAction]]: antonym of UnRegisterAction.* [[LeaveAction]]: Unlike LeaveAction, UnRegisterAction implies that you are unregistering from a service you were previously registered, rather than leaving a team/group of people.

    References:
        https://schema.org/UnRegisterAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(UnRegisterActionInheritedProperties , UnRegisterActionProperties, TypedDict):
    pass


class UnRegisterActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="UnRegisterAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[UnRegisterActionProperties, UnRegisterActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UnRegisterAction"
    return model
    

UnRegisterAction = create_schema_org_model()


def create_unregisteraction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_unregisteraction_model(model=model)
    return pydantic_type(model).schema_json()


