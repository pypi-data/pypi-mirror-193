"""
A patient is any person recipient of health care services.

https://schema.org/Patient
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PatientInheritedProperties(TypedDict):
    """A patient is any person recipient of health care services.

    References:
        https://schema.org/Patient
    Note:
        Model Depth 3
    Attributes:
        sibling: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sibling of the person.
        isicV4: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.
        hasPOS: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Points-of-Sales operated by the organization or person.
        globalLocationNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.
        spouse: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The person's spouse.
        knowsAbout: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that is known about - suggesting possible expertise but not implying it. We do not distinguish skill levels here, or relate this to educational content, events, objectives or [[JobPosting]] descriptions.
        makesOffer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A pointer to products or services offered by the organization or person.
        colleague: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A colleague of the person.
        honorificSuffix: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An honorific suffix following a Person's name such as M.D./PhD/MSCSW.
        nationality: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Nationality of the person.
        affiliation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An organization that this person is affiliated with. For example, a school/university, a club, or a team.
        memberOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An Organization (or ProgramMembership) to which this Person or Organization belongs.
        publishingPrinciples: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The publishingPrinciples property indicates (typically via [[URL]]) a document describing the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]] writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles are those of the party primarily responsible for the creation of the [[CreativeWork]].While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.
        height: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The height of the item.
        knows: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The most generic bi-directional social/work relation.
        relatedTo: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The most generic familial relation.
        worksFor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Organizations that the person works for.
        award: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An award won by or for this item.
        email: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Email address.
        givenName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Given name. In the U.S., the first name of a Person.
        workLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A contact location for a person's place of work.
        contactPoints: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A contact point for a person or organization.
        jobTitle: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The job title of the person (for example, Financial Manager).
        owns: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Products owned by the organization or person.
        awards: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Awards won by or for this item.
        children: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A child of the person.
        parent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A parent of this person.
        funding: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        interactionStatistic: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of interactions for the CreativeWork using the WebSite or SoftwareApplication. The most specific child type of InteractionCounter should be used.
        seeks: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A pointer to products or services sought by the organization or person (demand).
        weight: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The weight of the product or person.
        funder: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person or organization that supports (sponsors) something through some kind of financial contribution.
        birthDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): Date of birth.
        deathDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): Date of death.
        additionalName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An additional name for a Person, can be used for a middle name.
        duns: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Dun & Bradstreet DUNS number for identifying an organization or business person.
        performerIn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Event that this person is a performer or participant in.
        vatID: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Value-added Tax ID of the organization or person.
        knowsLanguage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Of a [[Person]], and less typically of an [[Organization]], to indicate a known language. We do not distinguish skill levels or reading/writing/speaking/signing here. Use language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).
        honorificPrefix: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.
        parents: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A parents of the person.
        familyName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Family name. In the U.S., the last name of a Person.
        siblings: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sibling of the person.
        hasCredential: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A credential awarded to the Person or Organization.
        address: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Physical address of the item.
        brand: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.
        hasOccupation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Person's occupation. For past professions, use Role for expressing dates.
        netWorth: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The total financial value of the person as calculated by subtracting assets from liabilities.
        contactPoint: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A contact point for a person or organization.
        homeLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A contact location for a person's residence.
        gender: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Gender of something, typically a [[Person]], but possibly also fictional characters, animals, etc. While https://schema.org/Male and https://schema.org/Female may be used, text strings are also acceptable for people who do not identify as a binary gender. The [[gender]] property can also be used in an extended sense to cover e.g. the gender of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities. A mixed-gender [[SportsTeam]] can be indicated with a text value of "Mixed".
        hasOfferCatalog: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates an OfferCatalog listing for this Organization, Person, or Service.
        follows: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The most generic uni-directional social relation.
        birthPlace: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The place where the person was born.
        faxNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The fax number.
        telephone: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The telephone number.
        taxID: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.
        callSign: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles.
        naics: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The North American Industry Classification System (NAICS) code for a particular organization or business person.
        deathPlace: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The place where the person died.
        alumniOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An organization that the person is an alumni of.
        colleagues: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A colleague of the person.
        sponsor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
    """

    sibling: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    isicV4: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasPOS: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    globalLocationNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    spouse: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    knowsAbout: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    makesOffer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    colleague: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    honorificSuffix: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    nationality: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    affiliation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    memberOf: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    publishingPrinciples: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    height: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    knows: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    relatedTo: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    worksFor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    award: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    email: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    givenName: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    workLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    contactPoints: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    jobTitle: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    owns: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    awards: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    children: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    parent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    funding: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    interactionStatistic: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    seeks: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    weight: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    funder: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    birthDate: NotRequired[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]
    deathDate: NotRequired[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]
    additionalName: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    duns: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    performerIn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    vatID: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    knowsLanguage: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    honorificPrefix: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    parents: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    familyName: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    siblings: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasCredential: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    address: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    brand: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasOccupation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    netWorth: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    contactPoint: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    homeLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gender: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasOfferCatalog: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    follows: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    birthPlace: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    faxNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    telephone: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    taxID: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    callSign: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    naics: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    deathPlace: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    alumniOf: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    colleagues: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sponsor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class PatientProperties(TypedDict):
    """A patient is any person recipient of health care services.

    References:
        https://schema.org/Patient
    Note:
        Model Depth 3
    Attributes:
        healthCondition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifying the health condition(s) of a patient, medical study, or other target audience.
        diagnosis: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): One or more alternative conditions considered in the differential diagnosis process as output of a diagnosis process.
        drug: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifying a drug or medicine used in a medication procedure.
    """

    healthCondition: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    diagnosis: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    drug: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(PatientInheritedProperties , PatientProperties, TypedDict):
    pass


class PatientBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Patient",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'sibling': {'exclude': True}}
        fields = {'isicV4': {'exclude': True}}
        fields = {'hasPOS': {'exclude': True}}
        fields = {'globalLocationNumber': {'exclude': True}}
        fields = {'spouse': {'exclude': True}}
        fields = {'knowsAbout': {'exclude': True}}
        fields = {'makesOffer': {'exclude': True}}
        fields = {'colleague': {'exclude': True}}
        fields = {'honorificSuffix': {'exclude': True}}
        fields = {'nationality': {'exclude': True}}
        fields = {'affiliation': {'exclude': True}}
        fields = {'memberOf': {'exclude': True}}
        fields = {'publishingPrinciples': {'exclude': True}}
        fields = {'height': {'exclude': True}}
        fields = {'knows': {'exclude': True}}
        fields = {'relatedTo': {'exclude': True}}
        fields = {'worksFor': {'exclude': True}}
        fields = {'award': {'exclude': True}}
        fields = {'email': {'exclude': True}}
        fields = {'givenName': {'exclude': True}}
        fields = {'workLocation': {'exclude': True}}
        fields = {'contactPoints': {'exclude': True}}
        fields = {'jobTitle': {'exclude': True}}
        fields = {'owns': {'exclude': True}}
        fields = {'awards': {'exclude': True}}
        fields = {'children': {'exclude': True}}
        fields = {'parent': {'exclude': True}}
        fields = {'funding': {'exclude': True}}
        fields = {'interactionStatistic': {'exclude': True}}
        fields = {'seeks': {'exclude': True}}
        fields = {'weight': {'exclude': True}}
        fields = {'funder': {'exclude': True}}
        fields = {'birthDate': {'exclude': True}}
        fields = {'deathDate': {'exclude': True}}
        fields = {'additionalName': {'exclude': True}}
        fields = {'duns': {'exclude': True}}
        fields = {'performerIn': {'exclude': True}}
        fields = {'vatID': {'exclude': True}}
        fields = {'knowsLanguage': {'exclude': True}}
        fields = {'honorificPrefix': {'exclude': True}}
        fields = {'parents': {'exclude': True}}
        fields = {'familyName': {'exclude': True}}
        fields = {'siblings': {'exclude': True}}
        fields = {'hasCredential': {'exclude': True}}
        fields = {'address': {'exclude': True}}
        fields = {'brand': {'exclude': True}}
        fields = {'hasOccupation': {'exclude': True}}
        fields = {'netWorth': {'exclude': True}}
        fields = {'contactPoint': {'exclude': True}}
        fields = {'homeLocation': {'exclude': True}}
        fields = {'gender': {'exclude': True}}
        fields = {'hasOfferCatalog': {'exclude': True}}
        fields = {'follows': {'exclude': True}}
        fields = {'birthPlace': {'exclude': True}}
        fields = {'faxNumber': {'exclude': True}}
        fields = {'telephone': {'exclude': True}}
        fields = {'taxID': {'exclude': True}}
        fields = {'callSign': {'exclude': True}}
        fields = {'naics': {'exclude': True}}
        fields = {'deathPlace': {'exclude': True}}
        fields = {'alumniOf': {'exclude': True}}
        fields = {'colleagues': {'exclude': True}}
        fields = {'sponsor': {'exclude': True}}
        fields = {'healthCondition': {'exclude': True}}
        fields = {'diagnosis': {'exclude': True}}
        fields = {'drug': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PatientProperties, PatientInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Patient"
    return model
    

Patient = create_schema_org_model()


def create_patient_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_patient_model(model=model)
    return pydantic_type(model).schema_json()


