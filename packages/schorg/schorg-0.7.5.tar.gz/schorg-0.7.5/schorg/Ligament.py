"""
A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints.

https://schema.org/Ligament
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LigamentInheritedProperties(TypedDict):
    """A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints.

    References:
        https://schema.org/Ligament
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
    associatedPathophysiology: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    bodyLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    relatedTherapy: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    subStructure: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    relatedCondition: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    diagram: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class LigamentProperties(TypedDict):
    """A short band of tough, flexible, fibrous connective tissue that functions to connect multiple bones, cartilages, and structurally support joints.

    References:
        https://schema.org/Ligament
    Note:
        Model Depth 4
    Attributes:
    """


class LigamentAllProperties(LigamentInheritedProperties, LigamentProperties, TypedDict):
    pass


class LigamentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Ligament", alias="@id")
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
        LigamentProperties, LigamentInheritedProperties, LigamentAllProperties
    ] = LigamentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Ligament"
    return model


Ligament = create_schema_org_model()


def create_ligament_model(
    model: Union[LigamentProperties, LigamentInheritedProperties, LigamentAllProperties]
):
    _type = deepcopy(LigamentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Ligament. Please see: https://schema.org/Ligament"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: LigamentAllProperties):
    pydantic_type = create_ligament_model(model=model)
    return pydantic_type(model).schema_json()
