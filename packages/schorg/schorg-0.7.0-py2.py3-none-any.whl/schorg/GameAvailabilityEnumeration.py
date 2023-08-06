"""
For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind of game availability offered. 

https://schema.org/GameAvailabilityEnumeration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GameAvailabilityEnumerationInheritedProperties(TypedDict):
    """For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind of game availability offered. 

    References:
        https://schema.org/GameAvailabilityEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class GameAvailabilityEnumerationProperties(TypedDict):
    """For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind of game availability offered. 

    References:
        https://schema.org/GameAvailabilityEnumeration
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(GameAvailabilityEnumerationInheritedProperties , GameAvailabilityEnumerationProperties, TypedDict):
    pass


class GameAvailabilityEnumerationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="GameAvailabilityEnumeration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[GameAvailabilityEnumerationProperties, GameAvailabilityEnumerationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GameAvailabilityEnumeration"
    return model
    

GameAvailabilityEnumeration = create_schema_org_model()


def create_gameavailabilityenumeration_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_gameavailabilityenumeration_model(model=model)
    return pydantic_type(model).schema_json()


