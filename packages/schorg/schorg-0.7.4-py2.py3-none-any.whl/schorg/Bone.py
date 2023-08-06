"""
Rigid connective tissue that comprises up the skeletal structure of the human body.

https://schema.org/Bone
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BoneInheritedProperties(TypedDict):
    """Rigid connective tissue that comprises up the skeletal structure of the human body.

    References:
        https://schema.org/Bone
    Note:
        Model Depth 4
    Attributes:
        connectedTo: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Other anatomical structures to which this structure is connected.
        partOfSystem: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The anatomical or organ system that this structure is part of.
        associatedPathophysiology: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.
        bodyLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Location in the body of the anatomical structure.
        relatedTherapy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical therapy related to this anatomy.
        subStructure: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Component (sub-)structure(s) that comprise this anatomical structure.
        relatedCondition: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical condition associated with this anatomy.
        diagram: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An image containing a diagram that illustrates the structure and/or its component substructures and/or connections with other structures.
    """

    connectedTo: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    partOfSystem: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    associatedPathophysiology: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    bodyLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    relatedTherapy: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    subStructure: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    relatedCondition: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    diagram: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class BoneProperties(TypedDict):
    """Rigid connective tissue that comprises up the skeletal structure of the human body.

    References:
        https://schema.org/Bone
    Note:
        Model Depth 4
    Attributes:
    """


class BoneAllProperties(BoneInheritedProperties, BoneProperties, TypedDict):
    pass


class BoneBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Bone", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"connectedTo": {"exclude": True}}
        fields = {"partOfSystem": {"exclude": True}}
        fields = {"associatedPathophysiology": {"exclude": True}}
        fields = {"bodyLocation": {"exclude": True}}
        fields = {"relatedTherapy": {"exclude": True}}
        fields = {"subStructure": {"exclude": True}}
        fields = {"relatedCondition": {"exclude": True}}
        fields = {"diagram": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BoneProperties, BoneInheritedProperties, BoneAllProperties
    ] = BoneAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Bone"
    return model


Bone = create_schema_org_model()


def create_bone_model(
    model: Union[BoneProperties, BoneInheritedProperties, BoneAllProperties]
):
    _type = deepcopy(BoneAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of BoneAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BoneAllProperties):
    pydantic_type = create_bone_model(model=model)
    return pydantic_type(model).schema_json()
