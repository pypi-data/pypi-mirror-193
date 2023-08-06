"""
A class, also often called a 'Type'; equivalent to rdfs:Class.

https://schema.org/Class
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ClassInheritedProperties(TypedDict):
    """A class, also often called a 'Type'; equivalent to rdfs:Class.

    References:
        https://schema.org/Class
    Note:
        Model Depth 3
    Attributes:
    """

    


class ClassProperties(TypedDict):
    """A class, also often called a 'Type'; equivalent to rdfs:Class.

    References:
        https://schema.org/Class
    Note:
        Model Depth 3
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(ClassInheritedProperties , ClassProperties, TypedDict):
    pass


class ClassBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Class",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ClassProperties, ClassInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Class"
    return model
    

Class = create_schema_org_model()


def create_class_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_class_model(model=model)
    return pydantic_type(model).schema_json()


