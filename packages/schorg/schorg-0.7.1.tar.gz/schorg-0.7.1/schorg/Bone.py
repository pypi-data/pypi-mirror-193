"""
Rigid connective tissue that comprises up the skeletal structure of the human body.

https://schema.org/Bone
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BoneInheritedProperties(TypedDict):
    """Rigid connective tissue that comprises up the skeletal structure of the human body.

    References:
        https://schema.org/Bone
    Note:
        Model Depth 4
    Attributes:
        connectedTo: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Other anatomical structures to which this structure is connected.
        partOfSystem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The anatomical or organ system that this structure is part of.
        associatedPathophysiology: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.
        bodyLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Location in the body of the anatomical structure.
        relatedTherapy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical therapy related to this anatomy.
        subStructure: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Component (sub-)structure(s) that comprise this anatomical structure.
        relatedCondition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical condition associated with this anatomy.
        diagram: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An image containing a diagram that illustrates the structure and/or its component substructures and/or connections with other structures.
    """

    connectedTo: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    partOfSystem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    associatedPathophysiology: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    bodyLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    relatedTherapy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    subStructure: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    relatedCondition: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    diagram: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class BoneProperties(TypedDict):
    """Rigid connective tissue that comprises up the skeletal structure of the human body.

    References:
        https://schema.org/Bone
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(BoneInheritedProperties , BoneProperties, TypedDict):
    pass


class BoneBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Bone",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'connectedTo': {'exclude': True}}
        fields = {'partOfSystem': {'exclude': True}}
        fields = {'associatedPathophysiology': {'exclude': True}}
        fields = {'bodyLocation': {'exclude': True}}
        fields = {'relatedTherapy': {'exclude': True}}
        fields = {'subStructure': {'exclude': True}}
        fields = {'relatedCondition': {'exclude': True}}
        fields = {'diagram': {'exclude': True}}
        


def create_schema_org_model(type_: Union[BoneProperties, BoneInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Bone"
    return model
    

Bone = create_schema_org_model()


def create_bone_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bone_model(model=model)
    return pydantic_type(model).schema_json()


