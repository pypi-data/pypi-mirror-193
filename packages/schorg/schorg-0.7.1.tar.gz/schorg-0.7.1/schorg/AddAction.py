"""
The act of editing by adding an object to a collection.

https://schema.org/AddAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AddActionInheritedProperties(TypedDict):
    """The act of editing by adding an object to a collection.

    References:
        https://schema.org/AddAction
    Note:
        Model Depth 4
    Attributes:
        collection: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of object. The collection target of the action.
        targetCollection: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of object. The collection target of the action.
    """

    collection: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    targetCollection: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AddActionProperties(TypedDict):
    """The act of editing by adding an object to a collection.

    References:
        https://schema.org/AddAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(AddActionInheritedProperties , AddActionProperties, TypedDict):
    pass


class AddActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AddAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'collection': {'exclude': True}}
        fields = {'targetCollection': {'exclude': True}}
        


def create_schema_org_model(type_: Union[AddActionProperties, AddActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AddAction"
    return model
    

AddAction = create_schema_org_model()


def create_addaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_addaction_model(model=model)
    return pydantic_type(model).schema_json()


