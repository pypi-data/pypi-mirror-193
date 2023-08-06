"""
The act of editing a recipient by removing one of its objects.

https://schema.org/DeleteAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DeleteActionInheritedProperties(TypedDict):
    """The act of editing a recipient by removing one of its objects.

    References:
        https://schema.org/DeleteAction
    Note:
        Model Depth 4
    Attributes:
        collection: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of object. The collection target of the action.
        targetCollection: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of object. The collection target of the action.
    """

    collection: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    targetCollection: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class DeleteActionProperties(TypedDict):
    """The act of editing a recipient by removing one of its objects.

    References:
        https://schema.org/DeleteAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(DeleteActionInheritedProperties , DeleteActionProperties, TypedDict):
    pass


class DeleteActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DeleteAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'collection': {'exclude': True}}
        fields = {'targetCollection': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DeleteActionProperties, DeleteActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DeleteAction"
    return model
    

DeleteAction = create_schema_org_model()


def create_deleteaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_deleteaction_model(model=model)
    return pydantic_type(model).schema_json()


