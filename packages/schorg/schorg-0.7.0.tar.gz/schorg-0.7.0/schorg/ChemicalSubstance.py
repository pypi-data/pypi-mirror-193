"""
A chemical substance is 'a portion of matter of constant composition, composed of molecular entities of the same type or of different types' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999)).

https://schema.org/ChemicalSubstance
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ChemicalSubstanceInheritedProperties(TypedDict):
    """A chemical substance is 'a portion of matter of constant composition, composed of molecular entities of the same type or of different types' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999)).

    References:
        https://schema.org/ChemicalSubstance
    Note:
        Model Depth 3
    Attributes:
        hasBioChemEntityPart: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates a BioChemEntity that (in some sense) has this BioChemEntity as a part. 
        isEncodedByBioChemEntity: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Another BioChemEntity encoding by this one.
        taxonomicRange: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The taxonomic grouping of the organism that expresses, encodes, or in some way related to the BioChemEntity.
        isLocatedInSubcellularLocation: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Subcellular location where this BioChemEntity is located; please use PropertyValue if you want to include any evidence.
        bioChemInteraction: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A BioChemEntity that is known to interact with this item.
        funding: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        isPartOfBioChemEntity: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates a BioChemEntity that is (in some sense) a part of this BioChemEntity. 
        bioChemSimilarity: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A similar BioChemEntity, e.g., obtained by fingerprint similarity algorithms.
        hasRepresentation: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A common representation such as a protein sequence or chemical structure for this entity. For images use schema.org/image.
        biologicalRole: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A role played by the BioChemEntity within a biological context.
        isInvolvedInBiologicalProcess: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Biological process this BioChemEntity is involved in; please use PropertyValue if you want to include any evidence.
        associatedDisease: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Disease associated to this BioChemEntity. Such disease can be a MedicalCondition or a URL. If you want to add an evidence supporting the association, please use PropertyValue.
        hasMolecularFunction: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Molecular function performed by this BioChemEntity; please use PropertyValue if you want to include any evidence.
    """

    hasBioChemEntityPart: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isEncodedByBioChemEntity: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    taxonomicRange: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    isLocatedInSubcellularLocation: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    bioChemInteraction: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    funding: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isPartOfBioChemEntity: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    bioChemSimilarity: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    hasRepresentation: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    biologicalRole: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isInvolvedInBiologicalProcess: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    associatedDisease: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    hasMolecularFunction: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    


class ChemicalSubstanceProperties(TypedDict):
    """A chemical substance is 'a portion of matter of constant composition, composed of molecular entities of the same type or of different types' (source: [ChEBI:59999](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=59999)).

    References:
        https://schema.org/ChemicalSubstance
    Note:
        Model Depth 3
    Attributes:
        chemicalRole: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A role played by the BioChemEntity within a chemical context.
        potentialUse: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Intended use of the BioChemEntity by humans.
        chemicalComposition: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The chemical composition describes the identity and relative ratio of the chemical elements that make up the substance.
    """

    chemicalRole: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    potentialUse: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    chemicalComposition: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(ChemicalSubstanceInheritedProperties , ChemicalSubstanceProperties, TypedDict):
    pass


class ChemicalSubstanceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ChemicalSubstance",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'hasBioChemEntityPart': {'exclude': True}}
        fields = {'isEncodedByBioChemEntity': {'exclude': True}}
        fields = {'taxonomicRange': {'exclude': True}}
        fields = {'isLocatedInSubcellularLocation': {'exclude': True}}
        fields = {'bioChemInteraction': {'exclude': True}}
        fields = {'funding': {'exclude': True}}
        fields = {'isPartOfBioChemEntity': {'exclude': True}}
        fields = {'bioChemSimilarity': {'exclude': True}}
        fields = {'hasRepresentation': {'exclude': True}}
        fields = {'biologicalRole': {'exclude': True}}
        fields = {'isInvolvedInBiologicalProcess': {'exclude': True}}
        fields = {'associatedDisease': {'exclude': True}}
        fields = {'hasMolecularFunction': {'exclude': True}}
        fields = {'chemicalRole': {'exclude': True}}
        fields = {'potentialUse': {'exclude': True}}
        fields = {'chemicalComposition': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ChemicalSubstanceProperties, ChemicalSubstanceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ChemicalSubstance"
    return model
    

ChemicalSubstance = create_schema_org_model()


def create_chemicalsubstance_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_chemicalsubstance_model(model=model)
    return pydantic_type(model).schema_json()


