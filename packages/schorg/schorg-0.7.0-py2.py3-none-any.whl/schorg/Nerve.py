"""
A common pathway for the electrochemical nerve impulses that are transmitted along each of the axons.

https://schema.org/Nerve
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NerveInheritedProperties(TypedDict):
    """A common pathway for the electrochemical nerve impulses that are transmitted along each of the axons.

    References:
        https://schema.org/Nerve
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
    associatedPathophysiology: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    bodyLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    relatedTherapy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    subStructure: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    relatedCondition: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    diagram: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class NerveProperties(TypedDict):
    """A common pathway for the electrochemical nerve impulses that are transmitted along each of the axons.

    References:
        https://schema.org/Nerve
    Note:
        Model Depth 4
    Attributes:
        nerveMotor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The neurological pathway extension that involves muscle control.
        branch: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The branches that delineate from the nerve bundle. Not to be confused with [[branchOf]].
        sourcedFrom: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The neurological pathway that originates the neurons.
        sensoryUnit: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The neurological pathway extension that inputs and sends information to the brain or spinal cord.
    """

    nerveMotor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    branch: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sourcedFrom: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sensoryUnit: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(NerveInheritedProperties , NerveProperties, TypedDict):
    pass


class NerveBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Nerve",alias='@id')
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
        fields = {'nerveMotor': {'exclude': True}}
        fields = {'branch': {'exclude': True}}
        fields = {'sourcedFrom': {'exclude': True}}
        fields = {'sensoryUnit': {'exclude': True}}
        


def create_schema_org_model(type_: Union[NerveProperties, NerveInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nerve"
    return model
    

Nerve = create_schema_org_model()


def create_nerve_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nerve_model(model=model)
    return pydantic_type(model).schema_json()


