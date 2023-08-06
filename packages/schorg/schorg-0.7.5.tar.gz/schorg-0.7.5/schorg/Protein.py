"""
Protein is here used in its widest possible definition, as classes of amino acid based molecules. Amyloid-beta Protein in human (UniProt P05067), eukaryota (e.g. an OrthoDB group) or even a single molecule that one can point to are all of type schema:Protein. A protein can thus be a subclass of another protein, e.g. schema:Protein as a UniProt record can have multiple isoforms inside it which would also be schema:Protein. They can be imagined, synthetic, hypothetical or naturally occurring.

https://schema.org/Protein
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ProteinInheritedProperties(TypedDict):
    """Protein is here used in its widest possible definition, as classes of amino acid based molecules. Amyloid-beta Protein in human (UniProt P05067), eukaryota (e.g. an OrthoDB group) or even a single molecule that one can point to are all of type schema:Protein. A protein can thus be a subclass of another protein, e.g. schema:Protein as a UniProt record can have multiple isoforms inside it which would also be schema:Protein. They can be imagined, synthetic, hypothetical or naturally occurring.

    References:
        https://schema.org/Protein
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

    hasBioChemEntityPart: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    isEncodedByBioChemEntity: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    taxonomicRange: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    isLocatedInSubcellularLocation: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    bioChemInteraction: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    funding: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    isPartOfBioChemEntity: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    bioChemSimilarity: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    hasRepresentation: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    biologicalRole: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    isInvolvedInBiologicalProcess: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    associatedDisease: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    hasMolecularFunction: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]


class ProteinProperties(TypedDict):
    """Protein is here used in its widest possible definition, as classes of amino acid based molecules. Amyloid-beta Protein in human (UniProt P05067), eukaryota (e.g. an OrthoDB group) or even a single molecule that one can point to are all of type schema:Protein. A protein can thus be a subclass of another protein, e.g. schema:Protein as a UniProt record can have multiple isoforms inside it which would also be schema:Protein. They can be imagined, synthetic, hypothetical or naturally occurring.

    References:
        https://schema.org/Protein
    Note:
        Model Depth 3
    Attributes:
        hasBioPolymerSequence: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A symbolic representation of a BioChemEntity. For example, a nucleotide sequence of a Gene or an amino acid sequence of a Protein.
    """

    hasBioPolymerSequence: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class ProteinAllProperties(ProteinInheritedProperties, ProteinProperties, TypedDict):
    pass


class ProteinBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Protein", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"hasBioChemEntityPart": {"exclude": True}}
        fields = {"isEncodedByBioChemEntity": {"exclude": True}}
        fields = {"taxonomicRange": {"exclude": True}}
        fields = {"isLocatedInSubcellularLocation": {"exclude": True}}
        fields = {"bioChemInteraction": {"exclude": True}}
        fields = {"funding": {"exclude": True}}
        fields = {"isPartOfBioChemEntity": {"exclude": True}}
        fields = {"bioChemSimilarity": {"exclude": True}}
        fields = {"hasRepresentation": {"exclude": True}}
        fields = {"biologicalRole": {"exclude": True}}
        fields = {"isInvolvedInBiologicalProcess": {"exclude": True}}
        fields = {"associatedDisease": {"exclude": True}}
        fields = {"hasMolecularFunction": {"exclude": True}}
        fields = {"hasBioPolymerSequence": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ProteinProperties, ProteinInheritedProperties, ProteinAllProperties
    ] = ProteinAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Protein"
    return model


Protein = create_schema_org_model()


def create_protein_model(
    model: Union[ProteinProperties, ProteinInheritedProperties, ProteinAllProperties]
):
    _type = deepcopy(ProteinAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Protein. Please see: https://schema.org/Protein"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ProteinAllProperties):
    pydantic_type = create_protein_model(model=model)
    return pydantic_type(model).schema_json()
