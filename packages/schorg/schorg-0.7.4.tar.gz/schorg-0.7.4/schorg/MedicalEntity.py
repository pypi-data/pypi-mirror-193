"""
The most generic type of entity related to health and the practice of medicine.

https://schema.org/MedicalEntity
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalEntityInheritedProperties(TypedDict):
    """The most generic type of entity related to health and the practice of medicine.

    References:
        https://schema.org/MedicalEntity
    Note:
        Model Depth 2
    Attributes:
        potentialAction: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.
        mainEntityOfPage: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See [background notes](/docs/datamodel.html#mainEntityBackground) for details.
        subjectOf: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A CreativeWork or Event about this Thing.
        url: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): URL of the item.
        alternateName: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An alias for the item.
        sameAs: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or official website.
        description: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A description of the item.
        disambiguatingDescription: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.
        identifier: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The identifier property represents any kind of identifier for any kind of [[Thing]], such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See [background notes](/docs/datamodel.html#identifierBg) for more details.
        image: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].
        name: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The name of the item.
        additionalType: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.
    """

    potentialAction: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    mainEntityOfPage: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    subjectOf: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    url: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    alternateName: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sameAs: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    description: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    disambiguatingDescription: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    identifier: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    image: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    name: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    additionalType: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]


class MedicalEntityProperties(TypedDict):
    """The most generic type of entity related to health and the practice of medicine.

    References:
        https://schema.org/MedicalEntity
    Note:
        Model Depth 2
    Attributes:
        recognizingAuthority: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): If applicable, the organization that officially recognizes this entity as part of its endorsed system of medicine.
        relevantSpecialty: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): If applicable, a medical specialty in which this entity is relevant.
        medicineSystem: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc.
        funding: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        legalStatus: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The drug or supplement's legal status, including any controlled substance schedules that apply.
        study: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical study or trial related to this entity.
        guideline: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical guideline related to this entity.
        code: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.
    """

    recognizingAuthority: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    relevantSpecialty: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    medicineSystem: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    funding: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    legalStatus: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    study: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    guideline: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    code: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class MedicalEntityAllProperties(
    MedicalEntityInheritedProperties, MedicalEntityProperties, TypedDict
):
    pass


class MedicalEntityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalEntity", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"potentialAction": {"exclude": True}}
        fields = {"mainEntityOfPage": {"exclude": True}}
        fields = {"subjectOf": {"exclude": True}}
        fields = {"url": {"exclude": True}}
        fields = {"alternateName": {"exclude": True}}
        fields = {"sameAs": {"exclude": True}}
        fields = {"description": {"exclude": True}}
        fields = {"disambiguatingDescription": {"exclude": True}}
        fields = {"identifier": {"exclude": True}}
        fields = {"image": {"exclude": True}}
        fields = {"name": {"exclude": True}}
        fields = {"additionalType": {"exclude": True}}
        fields = {"recognizingAuthority": {"exclude": True}}
        fields = {"relevantSpecialty": {"exclude": True}}
        fields = {"medicineSystem": {"exclude": True}}
        fields = {"funding": {"exclude": True}}
        fields = {"legalStatus": {"exclude": True}}
        fields = {"study": {"exclude": True}}
        fields = {"guideline": {"exclude": True}}
        fields = {"code": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalEntityProperties,
        MedicalEntityInheritedProperties,
        MedicalEntityAllProperties,
    ] = MedicalEntityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalEntity"
    return model


MedicalEntity = create_schema_org_model()


def create_medicalentity_model(
    model: Union[
        MedicalEntityProperties,
        MedicalEntityInheritedProperties,
        MedicalEntityAllProperties,
    ]
):
    _type = deepcopy(MedicalEntityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MedicalEntityAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalEntityAllProperties):
    pydantic_type = create_medicalentity_model(model=model)
    return pydantic_type(model).schema_json()
