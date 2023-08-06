"""
The act of asserting that a future event/action is no longer going to happen.Related actions:* [[ConfirmAction]]: The antonym of CancelAction.

https://schema.org/CancelAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CancelActionInheritedProperties(TypedDict):
    """The act of asserting that a future event/action is no longer going to happen.Related actions:* [[ConfirmAction]]: The antonym of CancelAction.

    References:
        https://schema.org/CancelAction
    Note:
        Model Depth 5
    Attributes:
        scheduledTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The time the object is scheduled to.
    """

    scheduledTime: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    


class CancelActionProperties(TypedDict):
    """The act of asserting that a future event/action is no longer going to happen.Related actions:* [[ConfirmAction]]: The antonym of CancelAction.

    References:
        https://schema.org/CancelAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(CancelActionInheritedProperties , CancelActionProperties, TypedDict):
    pass


class CancelActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CancelAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'scheduledTime': {'exclude': True}}
        


def create_schema_org_model(type_: Union[CancelActionProperties, CancelActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CancelAction"
    return model
    

CancelAction = create_schema_org_model()


def create_cancelaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_cancelaction_model(model=model)
    return pydantic_type(model).schema_json()


