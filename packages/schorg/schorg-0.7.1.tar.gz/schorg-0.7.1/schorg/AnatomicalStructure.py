"""
Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures.

https://schema.org/AnatomicalStructure
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AnatomicalStructureInheritedProperties(TypedDict):
    """Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures.

    References:
        https://schema.org/AnatomicalStructure
    Note:
        Model Depth 3
    Attributes:
        recognizingAuthority: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): If applicable, the organization that officially recognizes this entity as part of its endorsed system of medicine.
        relevantSpecialty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): If applicable, a medical specialty in which this entity is relevant.
        medicineSystem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc.
        funding: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        legalStatus: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The drug or supplement's legal status, including any controlled substance schedules that apply.
        study: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical study or trial related to this entity.
        guideline: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical guideline related to this entity.
        code: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.
    """

    recognizingAuthority: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    relevantSpecialty: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    medicineSystem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    funding: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    legalStatus: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    study: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    guideline: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    code: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AnatomicalStructureProperties(TypedDict):
    """Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures.

    References:
        https://schema.org/AnatomicalStructure
    Note:
        Model Depth 3
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
    


class AllProperties(AnatomicalStructureInheritedProperties , AnatomicalStructureProperties, TypedDict):
    pass


class AnatomicalStructureBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AnatomicalStructure",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'recognizingAuthority': {'exclude': True}}
        fields = {'relevantSpecialty': {'exclude': True}}
        fields = {'medicineSystem': {'exclude': True}}
        fields = {'funding': {'exclude': True}}
        fields = {'legalStatus': {'exclude': True}}
        fields = {'study': {'exclude': True}}
        fields = {'guideline': {'exclude': True}}
        fields = {'code': {'exclude': True}}
        fields = {'connectedTo': {'exclude': True}}
        fields = {'partOfSystem': {'exclude': True}}
        fields = {'associatedPathophysiology': {'exclude': True}}
        fields = {'bodyLocation': {'exclude': True}}
        fields = {'relatedTherapy': {'exclude': True}}
        fields = {'subStructure': {'exclude': True}}
        fields = {'relatedCondition': {'exclude': True}}
        fields = {'diagram': {'exclude': True}}
        


def create_schema_org_model(type_: Union[AnatomicalStructureProperties, AnatomicalStructureInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AnatomicalStructure"
    return model
    

AnatomicalStructure = create_schema_org_model()


def create_anatomicalstructure_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_anatomicalstructure_model(model=model)
    return pydantic_type(model).schema_json()


