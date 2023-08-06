"""
The act of being defeated in a competitive activity.

https://schema.org/LoseAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LoseActionInheritedProperties(TypedDict):
    """The act of being defeated in a competitive activity.

    References:
        https://schema.org/LoseAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class LoseActionProperties(TypedDict):
    """The act of being defeated in a competitive activity.

    References:
        https://schema.org/LoseAction
    Note:
        Model Depth 4
    Attributes:
        winner: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of participant. The winner of the action.
    """

    winner: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(LoseActionInheritedProperties , LoseActionProperties, TypedDict):
    pass


class LoseActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LoseAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'winner': {'exclude': True}}
        


def create_schema_org_model(type_: Union[LoseActionProperties, LoseActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LoseAction"
    return model
    

LoseAction = create_schema_org_model()


def create_loseaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_loseaction_model(model=model)
    return pydantic_type(model).schema_json()


