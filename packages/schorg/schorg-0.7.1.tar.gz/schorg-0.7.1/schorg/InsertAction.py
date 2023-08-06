"""
The act of adding at a specific location in an ordered collection.

https://schema.org/InsertAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InsertActionInheritedProperties(TypedDict):
    """The act of adding at a specific location in an ordered collection.

    References:
        https://schema.org/InsertAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class InsertActionProperties(TypedDict):
    """The act of adding at a specific location in an ordered collection.

    References:
        https://schema.org/InsertAction
    Note:
        Model Depth 5
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(InsertActionInheritedProperties , InsertActionProperties, TypedDict):
    pass


class InsertActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="InsertAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'toLocation': {'exclude': True}}
        


def create_schema_org_model(type_: Union[InsertActionProperties, InsertActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InsertAction"
    return model
    

InsertAction = create_schema_org_model()


def create_insertaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_insertaction_model(model=model)
    return pydantic_type(model).schema_json()


