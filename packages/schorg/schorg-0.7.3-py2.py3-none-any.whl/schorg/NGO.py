"""
Organization: Non-governmental Organization.

https://schema.org/NGO
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NGOInheritedProperties(TypedDict):
    """Organization: Non-governmental Organization.

    References:
        https://schema.org/NGO
    Note:
        Model Depth 3
    Attributes:
        serviceArea: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area where the service is provided.
        founder: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person who founded this organization.
        isicV4: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.
        hasPOS: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Points-of-Sales operated by the organization or person.
        globalLocationNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.
        member: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals.
        knowsAbout: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that is known about - suggesting possible expertise but not implying it. We do not distinguish skill levels here, or relate this to educational content, events, objectives or [[JobPosting]] descriptions.
        makesOffer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A pointer to products or services offered by the organization or person.
        ownershipFundingInfo: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]), a description of organizational ownership structure; funding and grants. In a news/media setting, this is with particular reference to editorial independence.   Note that the [[funder]] is also available and can be used to make basic funder information machine-readable.
        founders: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person who founded this organization.
        legalName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The official name of the organization, e.g. the registered company name.
        actionableFeedbackPolicy: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement about public engagement activities (for news media, the newsroom’s), including involving the public - digitally or otherwise -- in coverage decisions, reporting and activities after publication.
        areaServed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area where a service or offered item is provided.
        parentOrganization: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The larger organization that this organization is a [[subOrganization]] of, if any.
        slogan: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A slogan or motto associated with the item.
        department: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A relationship between an organization and a department of that organization, also described as an organization (allowing different urls, logos, opening hours). For example: a store with a pharmacy, or a bakery with a cafe.
        keywords: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.
        reviews: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Review of the item.
        memberOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An Organization (or ProgramMembership) to which this Person or Organization belongs.
        publishingPrinciples: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The publishingPrinciples property indicates (typically via [[URL]]) a document describing the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]] writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles are those of the party primarily responsible for the creation of the [[CreativeWork]].While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.
        employee: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Someone working for this organization.
        award: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An award won by or for this item.
        email: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Email address.
        contactPoints: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A contact point for a person or organization.
        diversityStaffingReport: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]), a report on staffing diversity issues. In a news context this might be for example ASNE or RTDNA (US) reports, or self-reported.
        foundingDate: (Optional[Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]]): The date that this organization was founded.
        owns: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Products owned by the organization or person.
        awards: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Awards won by or for this item.
        review: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A review of the item.
        dissolutionDate: (Optional[Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]]): The date that this organization was dissolved.
        funding: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        interactionStatistic: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of interactions for the CreativeWork using the WebSite or SoftwareApplication. The most specific child type of InteractionCounter should be used.
        events: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Upcoming or past events associated with this place or organization.
        seeks: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A pointer to products or services sought by the organization or person (demand).
        employees: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): People working for this organization.
        unnamedSourcesPolicy: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): For an [[Organization]] (typically a [[NewsMediaOrganization]]), a statement about policy on use of unnamed sources and the decision process required.
        subOrganization: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A relationship between two organizations where the first includes the second, e.g., as a subsidiary. See also: the more specific 'department' property.
        foundingLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The place where the Organization was founded.
        funder: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person or organization that supports (sponsors) something through some kind of financial contribution.
        iso6523Code: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An organization identifier as defined in ISO 6523(-1). Note that many existing organization identifiers such as [leiCode](https://schema.org/leiCode), [duns](https://schema.org/duns) and [vatID](https://schema.org/vatID) can be expressed as an ISO 6523 identifier by setting the ICD part of the ISO 6523 identifier accordingly.
        diversityPolicy: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Statement on diversity policy by an [[Organization]] e.g. a [[NewsMediaOrganization]]. For a [[NewsMediaOrganization]], a statement describing the newsroom’s diversity policy on both staffing and sources, typically providing staffing data.
        hasMerchantReturnPolicy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifies a MerchantReturnPolicy that may be applicable.
        event: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Upcoming or past event associated with this place, organization, or action.
        duns: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Dun & Bradstreet DUNS number for identifying an organization or business person.
        alumni: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Alumni of an organization.
        ethicsPolicy: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Statement about ethics policy, e.g. of a [[NewsMediaOrganization]] regarding journalistic and publishing practices, or of a [[Restaurant]], a page describing food source policies. In the case of a [[NewsMediaOrganization]], an ethicsPolicy is typically a statement describing the personal, organizational, and corporate standards of behavior expected by the organization.
        leiCode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An organization identifier that uniquely identifies a legal entity as defined in ISO 17442.
        vatID: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Value-added Tax ID of the organization or person.
        knowsLanguage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Of a [[Person]], and less typically of an [[Organization]], to indicate a known language. We do not distinguish skill levels or reading/writing/speaking/signing here. Use language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).
        correctionsPolicy: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): For an [[Organization]] (e.g. [[NewsMediaOrganization]]), a statement describing (in news media, the newsroom’s) disclosure and correction policy for errors.
        logo: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): An associated logo.
        hasCredential: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A credential awarded to the Person or Organization.
        address: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Physical address of the item.
        brand: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.
        nonprofitStatus: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): nonprofitStatus indicates the legal status of a non-profit organization in its primary place of business.
        contactPoint: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A contact point for a person or organization.
        hasOfferCatalog: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates an OfferCatalog listing for this Organization, Person, or Service.
        members: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A member of this organization.
        aggregateRating: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The overall rating, based on a collection of reviews or ratings, of the item.
        faxNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The fax number.
        telephone: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The telephone number.
        taxID: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.
        naics: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The North American Industry Classification System (NAICS) code for a particular organization or business person.
        location: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
        numberOfEmployees: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of employees in an organization, e.g. business.
        sponsor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
    """

    serviceArea: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    founder: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    isicV4: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasPOS: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    globalLocationNumber: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    member: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    knowsAbout: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    makesOffer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    ownershipFundingInfo: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    founders: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    legalName: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actionableFeedbackPolicy: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    areaServed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    parentOrganization: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    slogan: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    department: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    keywords: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    reviews: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    memberOf: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    publishingPrinciples: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    employee: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    award: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    email: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    contactPoints: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    diversityStaffingReport: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    foundingDate: NotRequired[
        Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]
    ]
    owns: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    awards: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    review: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    dissolutionDate: NotRequired[
        Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]
    ]
    funding: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    interactionStatistic: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    events: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    seeks: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    employees: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    unnamedSourcesPolicy: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    subOrganization: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    foundingLocation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    funder: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    iso6523Code: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    diversityPolicy: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    hasMerchantReturnPolicy: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    event: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    duns: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    alumni: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    ethicsPolicy: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    leiCode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    vatID: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    knowsLanguage: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    correctionsPolicy: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    logo: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    hasCredential: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    address: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    brand: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    nonprofitStatus: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    contactPoint: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasOfferCatalog: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    members: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    aggregateRating: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    faxNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    telephone: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    taxID: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    naics: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    location: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfEmployees: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    sponsor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class NGOProperties(TypedDict):
    """Organization: Non-governmental Organization.

    References:
        https://schema.org/NGO
    Note:
        Model Depth 3
    Attributes:
    """


class NGOAllProperties(NGOInheritedProperties, NGOProperties, TypedDict):
    pass


class NGOBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NGO", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"serviceArea": {"exclude": True}}
        fields = {"founder": {"exclude": True}}
        fields = {"isicV4": {"exclude": True}}
        fields = {"hasPOS": {"exclude": True}}
        fields = {"globalLocationNumber": {"exclude": True}}
        fields = {"member": {"exclude": True}}
        fields = {"knowsAbout": {"exclude": True}}
        fields = {"makesOffer": {"exclude": True}}
        fields = {"ownershipFundingInfo": {"exclude": True}}
        fields = {"founders": {"exclude": True}}
        fields = {"legalName": {"exclude": True}}
        fields = {"actionableFeedbackPolicy": {"exclude": True}}
        fields = {"areaServed": {"exclude": True}}
        fields = {"parentOrganization": {"exclude": True}}
        fields = {"slogan": {"exclude": True}}
        fields = {"department": {"exclude": True}}
        fields = {"keywords": {"exclude": True}}
        fields = {"reviews": {"exclude": True}}
        fields = {"memberOf": {"exclude": True}}
        fields = {"publishingPrinciples": {"exclude": True}}
        fields = {"employee": {"exclude": True}}
        fields = {"award": {"exclude": True}}
        fields = {"email": {"exclude": True}}
        fields = {"contactPoints": {"exclude": True}}
        fields = {"diversityStaffingReport": {"exclude": True}}
        fields = {"foundingDate": {"exclude": True}}
        fields = {"owns": {"exclude": True}}
        fields = {"awards": {"exclude": True}}
        fields = {"review": {"exclude": True}}
        fields = {"dissolutionDate": {"exclude": True}}
        fields = {"funding": {"exclude": True}}
        fields = {"interactionStatistic": {"exclude": True}}
        fields = {"events": {"exclude": True}}
        fields = {"seeks": {"exclude": True}}
        fields = {"employees": {"exclude": True}}
        fields = {"unnamedSourcesPolicy": {"exclude": True}}
        fields = {"subOrganization": {"exclude": True}}
        fields = {"foundingLocation": {"exclude": True}}
        fields = {"funder": {"exclude": True}}
        fields = {"iso6523Code": {"exclude": True}}
        fields = {"diversityPolicy": {"exclude": True}}
        fields = {"hasMerchantReturnPolicy": {"exclude": True}}
        fields = {"event": {"exclude": True}}
        fields = {"duns": {"exclude": True}}
        fields = {"alumni": {"exclude": True}}
        fields = {"ethicsPolicy": {"exclude": True}}
        fields = {"leiCode": {"exclude": True}}
        fields = {"vatID": {"exclude": True}}
        fields = {"knowsLanguage": {"exclude": True}}
        fields = {"correctionsPolicy": {"exclude": True}}
        fields = {"logo": {"exclude": True}}
        fields = {"hasCredential": {"exclude": True}}
        fields = {"address": {"exclude": True}}
        fields = {"brand": {"exclude": True}}
        fields = {"nonprofitStatus": {"exclude": True}}
        fields = {"contactPoint": {"exclude": True}}
        fields = {"hasOfferCatalog": {"exclude": True}}
        fields = {"members": {"exclude": True}}
        fields = {"aggregateRating": {"exclude": True}}
        fields = {"faxNumber": {"exclude": True}}
        fields = {"telephone": {"exclude": True}}
        fields = {"taxID": {"exclude": True}}
        fields = {"naics": {"exclude": True}}
        fields = {"location": {"exclude": True}}
        fields = {"numberOfEmployees": {"exclude": True}}
        fields = {"sponsor": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        NGOProperties, NGOInheritedProperties, NGOAllProperties
    ] = NGOAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NGO"
    return model


NGO = create_schema_org_model()


def create_ngo_model(
    model: Union[NGOProperties, NGOInheritedProperties, NGOAllProperties]
):
    _type = deepcopy(NGOAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NGOAllProperties):
    pydantic_type = create_ngo_model(model=model)
    return pydantic_type(model).schema_json()
