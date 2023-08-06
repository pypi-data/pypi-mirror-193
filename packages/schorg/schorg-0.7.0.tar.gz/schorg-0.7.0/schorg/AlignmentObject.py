"""
An intangible item that describes an alignment between a learning resource and a node in an educational framework.Should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.

https://schema.org/AlignmentObject
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AlignmentObjectInheritedProperties(TypedDict):
    """An intangible item that describes an alignment between a learning resource and a node in an educational framework.Should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.

    References:
        https://schema.org/AlignmentObject
    Note:
        Model Depth 3
    Attributes:
    """

    


class AlignmentObjectProperties(TypedDict):
    """An intangible item that describes an alignment between a learning resource and a node in an educational framework.Should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.

    References:
        https://schema.org/AlignmentObject
    Note:
        Model Depth 3
    Attributes:
        targetName: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The name of a node in an established educational framework.
        targetUrl: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The URL of a node in an established educational framework.
        alignmentType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A category of alignment between the learning resource and the framework node. Recommended values include: 'requires', 'textComplexity', 'readingLevel', and 'educationalSubject'.
        targetDescription: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The description of a node in an established educational framework.
        educationalFramework: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The framework to which the resource being described is aligned.
    """

    targetName: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    targetUrl: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    alignmentType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    targetDescription: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    educationalFramework: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(AlignmentObjectInheritedProperties , AlignmentObjectProperties, TypedDict):
    pass


class AlignmentObjectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AlignmentObject",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'targetName': {'exclude': True}}
        fields = {'targetUrl': {'exclude': True}}
        fields = {'alignmentType': {'exclude': True}}
        fields = {'targetDescription': {'exclude': True}}
        fields = {'educationalFramework': {'exclude': True}}
        


def create_schema_org_model(type_: Union[AlignmentObjectProperties, AlignmentObjectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AlignmentObject"
    return model
    

AlignmentObject = create_schema_org_model()


def create_alignmentobject_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_alignmentobject_model(model=model)
    return pydantic_type(model).schema_json()


