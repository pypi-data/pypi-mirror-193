"""
The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants.

https://schema.org/DepartAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DepartActionInheritedProperties(TypedDict):
    """The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants.

    References:
        https://schema.org/DepartAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fromLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class DepartActionProperties(TypedDict):
    """The act of  departing from a place. An agent departs from a fromLocation for a destination, optionally with participants.

    References:
        https://schema.org/DepartAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(DepartActionInheritedProperties , DepartActionProperties, TypedDict):
    pass


class DepartActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DepartAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'toLocation': {'exclude': True}}
        fields = {'fromLocation': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DepartActionProperties, DepartActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DepartAction"
    return model
    

DepartAction = create_schema_org_model()


def create_departaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_departaction_model(model=model)
    return pydantic_type(model).schema_json()


