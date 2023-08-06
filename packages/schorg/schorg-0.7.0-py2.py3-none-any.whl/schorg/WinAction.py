"""
The act of achieving victory in a competitive activity.

https://schema.org/WinAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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
    


class AllProperties(WinActionInheritedProperties , WinActionProperties, TypedDict):
    pass


class WinActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WinAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'loser': {'exclude': True}}
        


def create_schema_org_model(type_: Union[WinActionProperties, WinActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WinAction"
    return model
    

WinAction = create_schema_org_model()


def create_winaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_winaction_model(model=model)
    return pydantic_type(model).schema_json()


