"""
A type of boarding policy used by an airline.

https://schema.org/BoardingPolicyType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BoardingPolicyTypeInheritedProperties(TypedDict):
    """A type of boarding policy used by an airline.

    References:
        https://schema.org/BoardingPolicyType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class BoardingPolicyTypeProperties(TypedDict):
    """A type of boarding policy used by an airline.

    References:
        https://schema.org/BoardingPolicyType
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(BoardingPolicyTypeInheritedProperties , BoardingPolicyTypeProperties, TypedDict):
    pass


class BoardingPolicyTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BoardingPolicyType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[BoardingPolicyTypeProperties, BoardingPolicyTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BoardingPolicyType"
    return model
    

BoardingPolicyType = create_schema_org_model()


def create_boardingpolicytype_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_boardingpolicytype_model(model=model)
    return pydantic_type(model).schema_json()


