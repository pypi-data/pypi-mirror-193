"""
Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.

https://schema.org/MolecularEntity
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MolecularEntityInheritedProperties(TypedDict):
    """Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.

    References:
        https://schema.org/MolecularEntity
    Note:
        Model Depth 3
    Attributes:
        hasBioChemEntityPart: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates a BioChemEntity that (in some sense) has this BioChemEntity as a part. 
        isEncodedByBioChemEntity: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Another BioChemEntity encoding by this one.
        taxonomicRange: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The taxonomic grouping of the organism that expresses, encodes, or in some way related to the BioChemEntity.
        isLocatedInSubcellularLocation: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Subcellular location where this BioChemEntity is located; please use PropertyValue if you want to include any evidence.
        bioChemInteraction: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A BioChemEntity that is known to interact with this item.
        funding: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        isPartOfBioChemEntity: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates a BioChemEntity that is (in some sense) a part of this BioChemEntity. 
        bioChemSimilarity: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A similar BioChemEntity, e.g., obtained by fingerprint similarity algorithms.
        hasRepresentation: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A common representation such as a protein sequence or chemical structure for this entity. For images use schema.org/image.
        biologicalRole: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A role played by the BioChemEntity within a biological context.
        isInvolvedInBiologicalProcess: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Biological process this BioChemEntity is involved in; please use PropertyValue if you want to include any evidence.
        associatedDisease: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Disease associated to this BioChemEntity. Such disease can be a MedicalCondition or a URL. If you want to add an evidence supporting the association, please use PropertyValue.
        hasMolecularFunction: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Molecular function performed by this BioChemEntity; please use PropertyValue if you want to include any evidence.
    """

    hasBioChemEntityPart: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    isEncodedByBioChemEntity: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    taxonomicRange: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    isLocatedInSubcellularLocation: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    bioChemInteraction: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    funding: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    isPartOfBioChemEntity: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    bioChemSimilarity: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasRepresentation: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    biologicalRole: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    isInvolvedInBiologicalProcess: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    associatedDisease: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    hasMolecularFunction: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    


class MolecularEntityProperties(TypedDict):
    """Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity.

    References:
        https://schema.org/MolecularEntity
    Note:
        Model Depth 3
    Attributes:
        chemicalRole: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A role played by the BioChemEntity within a chemical context.
        smiles: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A specification in form of a line notation for describing the structure of chemical species using short ASCII strings.  Double bond stereochemistry \ indicators may need to be escaped in the string in formats where the backslash is an escape character.
        potentialUse: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Intended use of the BioChemEntity by humans.
        monoisotopicMolecularWeight: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The monoisotopic mass is the sum of the masses of the atoms in a molecule using the unbound, ground-state, rest mass of the principal (most abundant) isotope for each element instead of the isotopic average mass. Please include the units in the form '&lt;Number&gt; &lt;unit&gt;', for example '770.230488 g/mol' or as '&lt;QuantitativeValue&gt;.
        molecularWeight: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This is the molecular weight of the entity being described, not of the parent. Units should be included in the form '&lt;Number&gt; &lt;unit&gt;', for example '12 amu' or as '&lt;QuantitativeValue&gt;.
        inChIKey: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): InChIKey is a hashed version of the full InChI (using the SHA-256 algorithm).
        iupacName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Systematic method of naming chemical compounds as recommended by the International Union of Pure and Applied Chemistry (IUPAC).
        molecularFormula: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The empirical formula is the simplest whole number ratio of all the atoms in a molecule.
        inChI: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Non-proprietary identifier for molecular entity that can be used in printed and electronic data sources thus enabling easier linking of diverse data compilations.
    """

    chemicalRole: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    smiles: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    potentialUse: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    monoisotopicMolecularWeight: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    molecularWeight: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    inChIKey: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    iupacName: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    molecularFormula: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    inChI: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(MolecularEntityInheritedProperties , MolecularEntityProperties, TypedDict):
    pass


class MolecularEntityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MolecularEntity",alias='@id')
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
        fields = {'smiles': {'exclude': True}}
        fields = {'potentialUse': {'exclude': True}}
        fields = {'monoisotopicMolecularWeight': {'exclude': True}}
        fields = {'molecularWeight': {'exclude': True}}
        fields = {'inChIKey': {'exclude': True}}
        fields = {'iupacName': {'exclude': True}}
        fields = {'molecularFormula': {'exclude': True}}
        fields = {'inChI': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MolecularEntityProperties, MolecularEntityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MolecularEntity"
    return model
    

MolecularEntity = create_schema_org_model()


def create_molecularentity_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_molecularentity_model(model=model)
    return pydantic_type(model).schema_json()


