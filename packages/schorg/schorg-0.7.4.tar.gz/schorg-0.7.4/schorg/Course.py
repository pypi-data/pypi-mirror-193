"""
A description of an educational course which may be offered as distinct instances which take place at different times or take place at different locations, or be offered through different media or modes of study. An educational course is a sequence of one or more educational events and/or creative works which aims to build knowledge, competence or ability of learners.

https://schema.org/Course
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CourseInheritedProperties(TypedDict):
    """A description of an educational course which may be offered as distinct instances which take place at different times or take place at different locations, or be offered through different media or modes of study. An educational course is a sequence of one or more educational events and/or creative works which aims to build knowledge, competence or ability of learners.

    References:
        https://schema.org/Course
    Note:
        Model Depth 3
    Attributes:
        educationalLevel: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The level in terms of progression through an educational or training context. Examples of educational levels include 'beginner', 'intermediate' or 'advanced', and formal sets of level indicators.
        competencyRequired: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Knowledge, skill, ability or personal attribute that must be demonstrated by a person or other entity in order to do something such as earn an Educational Occupational Credential or understand a LearningResource.
        educationalUse: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The purpose of a work in the context of education; for example, 'assignment', 'group work'.
        educationalAlignment: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An alignment to an established educational framework.This property should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.
        assesses: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The item being described is intended to assess the competency or learning outcome defined by the referenced term.
        learningResourceType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.
        teaches: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The item being described is intended to help a person learn the competency or learning outcome defined by the referenced term.
        workTranslation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A work that is a translation of the content of this work. E.g. 西遊記 has an English workTranslation “Journey to the West”, a German workTranslation “Monkeys Pilgerfahrt” and a Vietnamese  translation Tây du ký bình khảo.
        educationalLevel: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The level in terms of progression through an educational or training context. Examples of educational levels include 'beginner', 'intermediate' or 'advanced', and formal sets of level indicators.
        associatedMedia: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A media object that encodes this CreativeWork. This property is a synonym for encoding.
        exampleOfWork: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A creative work that this work is an example/instance/realization/derivation of.
        releasedEvent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The place and time the release was issued, expressed as a PublicationEvent.
        version: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The version of the CreativeWork embodied by a specified resource.
        locationCreated: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The location where the CreativeWork was created, which may not be the same as the location depicted in the CreativeWork.
        acquireLicensePage: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Indicates a page documenting how licenses can be purchased or otherwise acquired, for the current item.
        thumbnailUrl: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A thumbnail image relevant to the Thing.
        provider: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        expires: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): Date the content expires and is no longer useful or available. For example a [[VideoObject]] or [[NewsArticle]] whose availability or relevance is time-limited, or a [[ClaimReview]] fact check whose publisher wants to indicate that it may no longer be relevant (or helpful to highlight) after some date.
        contentLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The location depicted or described in the content. For example, the location in a photograph or painting.
        educationalUse: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The purpose of a work in the context of education; for example, 'assignment', 'group work'.
        copyrightHolder: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The party holding the legal copyright to the CreativeWork.
        accessibilityControl: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Identifies input methods that are sufficient to fully control the described resource. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityControl-vocabulary).
        maintainer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A maintainer of a [[Dataset]], software package ([[SoftwareApplication]]), or other [[Project]]. A maintainer is a [[Person]] or [[Organization]] that manages contributions to, and/or publication of, some (typically complex) artifact. It is common for distributions of software and data to be based on "upstream" sources. When [[maintainer]] is applied to a specific version of something e.g. a particular version or packaging of a [[Dataset]], it is always  possible that the upstream source has a different maintainer. The [[isBasedOn]] property can be used to indicate such relationships between datasets to make the different maintenance roles clear. Similarly in the case of software, a package may have dedicated maintainers working on integration into software distributions such as Ubuntu, as well as upstream maintainers of the underlying work.
        educationalAlignment: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An alignment to an established educational framework.This property should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.
        spatial: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The "spatial" property can be used in cases when more specific properties(e.g. [[locationCreated]], [[spatialCoverage]], [[contentLocation]]) are not known to be appropriate.
        publisher: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The publisher of the creative work.
        keywords: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.
        assesses: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The item being described is intended to assess the competency or learning outcome defined by the referenced term.
        reviews: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Review of the item.
        isBasedOn: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A resource from which this work is derived or from which it is a modification or adaption.
        mentions: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.
        publishingPrinciples: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The publishingPrinciples property indicates (typically via [[URL]]) a document describing the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]] writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles are those of the party primarily responsible for the creation of the [[CreativeWork]].While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.
        contributor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A secondary contributor to the CreativeWork or Event.
        license: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A license document that applies to this content, typically indicated by URL.
        citation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.
        accessibilitySummary: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A human-readable summary of specific accessibility features or deficiencies, consistent with the other accessibility metadata but expressing subtleties such as "short descriptions are present but long descriptions will be needed for non-visual users" or "short descriptions are present and no long descriptions are needed."
        award: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An award won by or for this item.
        commentCount: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of comments this CreativeWork (e.g. Article, Question or Answer) has received. This is most applicable to works published in Web sites with commenting system; additional comments may exist elsewhere.
        temporalCoverage: (Optional[Union[List[Union[AnyUrl, datetime, SchemaOrgObj, str]], AnyUrl, datetime, SchemaOrgObj, str]]): The temporalCoverage of a CreativeWork indicates the period that the content applies to, i.e. that it describes, either as a DateTime or as a textual string indicating a time period in [ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals). In      the case of a Dataset it will typically indicate the relevant time period in a precise notation (e.g. for a 2011 census dataset, the year 2011 would be written "2011/2012"). Other forms of content, e.g. ScholarlyArticle, Book, TVSeries or TVEpisode, may indicate their temporalCoverage in broader terms - textually or via well-known URL.      Written works such as books may sometimes have precise temporal coverage too, e.g. a work set in 1939 - 1945 can be indicated in ISO 8601 interval format format via "1939/1945".Open-ended date ranges can be written with ".." in place of the end date. For example, "2015-11/.." indicates a range beginning in November 2015 and with no specified final date. This is tentative and might be updated in future when ISO 8601 is officially updated.
        dateCreated: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The date on which the CreativeWork was created or the item was added to a DataFeed.
        discussionUrl: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A link to the page containing the comments of the CreativeWork.
        copyrightNotice: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Text of a notice appropriate for describing the copyright aspects of this Creative Work, ideally indicating the owner of the copyright for the Work.
        learningResourceType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.
        awards: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Awards won by or for this item.
        accessModeSufficient: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A list of single or combined accessModes that are sufficient to understand all the intellectual content of a resource. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessModeSufficient-vocabulary).
        review: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A review of the item.
        conditionsOfAccess: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Conditions that affect the availability of, or method(s) of access to, an item. Typically used for real world items such as an [[ArchiveComponent]] held by an [[ArchiveOrganization]]. This property is not suitable for use as a general Web access control mechanism. It is expressed only in natural language.For example "Available by appointment from the Reading Room" or "Accessible only from logged-in accounts ".
        interactivityType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The predominant mode of learning supported by the learning resource. Acceptable values are 'active', 'expositive', or 'mixed'.
        abstract: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An abstract is a short description that summarizes a [[CreativeWork]].
        fileFormat: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Media type, typically MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml)) of the content, e.g. application/zip of a SoftwareApplication binary. In cases where a CreativeWork has several media type representations, 'encoding' can be used to indicate each MediaObject alongside particular fileFormat information. Unregistered or niche file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia entry.
        interpretedAsClaim: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Used to indicate a specific claim contained, implied, translated or refined from the content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can be indicated using [[claimInterpreter]].
        text: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The textual content of this CreativeWork.
        archivedAt: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Indicates a page or other link involved in archival of a [[CreativeWork]]. In the case of [[MediaReview]], the items in a [[MediaReviewItem]] may often become inaccessible, but be archived by archival, journalistic, activist, or law enforcement organizations. In such cases, the referenced page may not directly publish the content.
        alternativeHeadline: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A secondary title of the CreativeWork.
        creditText: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Text that can be used to credit person(s) and/or organization(s) associated with a published Creative Work.
        funding: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        interactionStatistic: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number of interactions for the CreativeWork using the WebSite or SoftwareApplication. The most specific child type of InteractionCounter should be used.
        workExample: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Example/instance/realization/derivation of the concept of this creative work. E.g. the paperback edition, first edition, or e-book.
        about: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The subject matter of the content.
        encodings: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A media object that encodes this CreativeWork.
        funder: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A person or organization that supports (sponsors) something through some kind of financial contribution.
        video: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An embedded video object.
        isPartOf: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Indicates an item or CreativeWork that this item, or CreativeWork (in some sense), is part of.
        pattern: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'. Values are typically expressed as text, although links to controlled value schemes are also supported.
        editor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifies the Person who edited the CreativeWork.
        dateModified: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.
        translationOfWork: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The work that this work has been translated from. E.g. 物种起源 is a translationOf “On the Origin of Species”.
        creativeWorkStatus: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The status of a creative work in terms of its stage in a lifecycle. Example terms include Incomplete, Draft, Published, Obsolete. Some organizations define a set of terms for the stages of their publication lifecycle.
        isBasedOnUrl: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html.
        isFamilyFriendly: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates whether this content is family friendly.
        isAccessibleForFree: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): A flag to signal that the item, event, or place is accessible for free.
        author: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.
        contentReferenceTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The specific time described by a creative work, for works (e.g. articles, video objects etc.) that emphasise a particular moment within an Event.
        correction: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Indicates a correction to a [[CreativeWork]], either via a [[CorrectionComment]], textually or in another document.
        sdDatePublished: (Optional[Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]]): Indicates the date on which the current structured data was generated / published. Typically used alongside [[sdPublisher]]
        comment: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Comments, typically from users.
        countryOfOrigin: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The country of origin of something, including products as well as creative  works such as movie and TV content.In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties such as [[contentLocation]] and [[locationCreated]] may be more applicable.In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.
        timeRequired: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Approximate or typical time it takes to work with or through this learning resource for the typical intended target audience, e.g. 'PT30M', 'PT1H25M'.
        typicalAgeRange: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The typical expected age range, e.g. '7-9', '11-'.
        genre: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Genre of the creative work, broadcast channel or group.
        producer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The person or organization who produced the work (e.g. music album, movie, TV/radio series etc.).
        schemaVersion: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Indicates (by URL or string) a particular version of a schema used in some CreativeWork. This property was created primarily to    indicate the use of a specific schema.org release, e.g. ```10.0``` as a simple string, or more explicitly via URL, ```https://schema.org/docs/releases.html#v10.0```. There may be situations in which other schemas might usefully be referenced this way, e.g. ```http://dublincore.org/specifications/dublin-core/dces/1999-07-02/``` but this has not been carefully explored in the community.
        audience: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An intended audience, i.e. a group for whom something was created.
        encoding: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A media object that encodes this CreativeWork. This property is a synonym for associatedMedia.
        publisherImprint: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The publishing division which published the comic.
        accessibilityAPI: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates that the resource is compatible with the referenced accessibility API. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityAPI-vocabulary).
        sdPublisher: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates the party responsible for generating and publishing the current structured data markup, typically in cases where the structured data is derived automatically from existing published content but published on a different site. For example, student projects and open data initiatives often re-publish existing content with more explicitly structured metadata. The[[sdPublisher]] property helps make such practices more explicit.
        audio: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An embedded audio object.
        accessibilityFeature: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Content features of the resource, such as accessible media, alternatives and supported enhancements for accessibility. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityFeature-vocabulary).
        spatialCoverage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The spatialCoverage of a CreativeWork indicates the place(s) which are the focus of the content. It is a subproperty of      contentLocation intended primarily for more technical and detailed materials. For example with a Dataset, it indicates      areas that the dataset describes: a dataset of New York weather would have spatialCoverage which was the place: the state of New York.
        accessMode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The human sensory perceptual system or cognitive faculty through which a person may process or perceive information. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessMode-vocabulary).
        editEIDR: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]] representing a specific edit / edition for a work of film or television.For example, the motion picture known as "Ghostbusters" whose [[titleEIDR]] is "10.5240/7EC7-228A-510A-053E-CBB8-J" has several edits, e.g. "10.5240/1F2A-E1C5-680A-14C6-E76B-I" and "10.5240/8A35-3BEE-6497-5D12-9E4F-3".Since schema.org types like [[Movie]] and [[TVEpisode]] can be used for both works and their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general description), or alongside [[editEIDR]] for a more edit-specific description.
        usageInfo: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The schema.org [[usageInfo]] property indicates further information about a [[CreativeWork]]. This property is applicable both to works that are freely available and to those that require payment or other transactions. It can reference additional information, e.g. community expectations on preferred linking and citation conventions, as well as purchasing details. For something that can be commercially licensed, usageInfo can provide detailed, resource-specific information about licensing options.This property can be used alongside the license property which indicates license(s) applicable to some piece of content. The usageInfo property can provide information about other licensing options, e.g. acquiring commercial usage rights for an image that is also available under non-commercial creative commons licenses.
        position: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The position of an item in a series or sequence of items.
        encodingFormat: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)), e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.In cases where a [[CreativeWork]] has several media type representations, [[encoding]] can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]] information.Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.
        copyrightYear: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The year during which the claimed copyright for the CreativeWork was first asserted.
        mainEntity: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates the primary entity described in some page or other CreativeWork.
        creator: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.
        teaches: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The item being described is intended to help a person learn the competency or learning outcome defined by the referenced term.
        temporal: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The "temporal" property can be used in cases where more specific properties(e.g. [[temporalCoverage]], [[dateCreated]], [[dateModified]], [[datePublished]]) are not known to be appropriate.
        size: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A standardized size of a product or creative work, specified either through a simple textual string (for example 'XL', '32Wx34L'), a  QuantitativeValue with a unitCode, or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]], [[height]], [[depth]] and [[weight]] properties may be more applicable.
        translator: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during some event.
        aggregateRating: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The overall rating, based on a collection of reviews or ratings, of the item.
        accountablePerson: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifies the Person that is legally accountable for the CreativeWork.
        accessibilityHazard: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A characteristic of the described resource that is physiologically dangerous to some users. Related to WCAG 2.0 guideline 2.3. Values should be drawn from the [approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessibilityHazard-vocabulary).
        contentRating: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Official rating of a piece of content&#x2014;for example, 'MPAA PG-13'.
        recordedAt: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The Event where the CreativeWork was recorded. The CreativeWork may capture all or part of the event.
        publication: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A publication event associated with the item.
        sdLicense: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A license document that applies to this structured data, typically indicated by URL.
        headline: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Headline of the article.
        materialExtent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The quantity of the materials being described or an expression of the physical space they occupy.
        inLanguage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
        material: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A material that something is made from, e.g. leather, wool, cotton, paper.
        datePublished: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): Date of first broadcast/publication.
        offers: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
        hasPart: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates an item or CreativeWork that is part of this item, or CreativeWork (in some sense).
        sourceOrganization: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The Organization on whose behalf the creator was working.
        sponsor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
        character: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Fictional person connected with a creative work.
    """

    educationalLevel: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    competencyRequired: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    educationalUse: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    educationalAlignment: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    assesses: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    learningResourceType: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    teaches: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    workTranslation: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    educationalLevel: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    associatedMedia: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    exampleOfWork: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    releasedEvent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    version: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    locationCreated: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    acquireLicensePage: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    thumbnailUrl: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    provider: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    expires: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    contentLocation: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    educationalUse: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    copyrightHolder: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    accessibilityControl: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    maintainer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    educationalAlignment: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    spatial: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    publisher: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    keywords: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    assesses: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    reviews: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isBasedOn: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    mentions: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    publishingPrinciples: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    contributor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    license: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    citation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    accessibilitySummary: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    award: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    commentCount: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    temporalCoverage: NotRequired[
        Union[
            List[Union[AnyUrl, datetime, SchemaOrgObj, str]],
            AnyUrl,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    dateCreated: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    discussionUrl: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    copyrightNotice: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    learningResourceType: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    awards: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    accessModeSufficient: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    review: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    conditionsOfAccess: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    interactivityType: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    abstract: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    fileFormat: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    interpretedAsClaim: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    text: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    archivedAt: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    alternativeHeadline: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    creditText: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    funding: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    interactionStatistic: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    workExample: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    about: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    encodings: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    funder: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    video: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isPartOf: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    pattern: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    editor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    dateModified: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    translationOfWork: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    creativeWorkStatus: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    isBasedOnUrl: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    isFamilyFriendly: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    isAccessibleForFree: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    author: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    contentReferenceTime: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    correction: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    sdDatePublished: NotRequired[
        Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]
    ]
    comment: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    countryOfOrigin: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    timeRequired: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    typicalAgeRange: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    genre: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    producer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    schemaVersion: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    audience: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    encoding: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    publisherImprint: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    accessibilityAPI: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    sdPublisher: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    audio: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    accessibilityFeature: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    spatialCoverage: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    accessMode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    editEIDR: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    usageInfo: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    position: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    encodingFormat: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    copyrightYear: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    mainEntity: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    creator: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    teaches: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    temporal: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    size: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    translator: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    aggregateRating: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    accountablePerson: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    accessibilityHazard: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    contentRating: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    recordedAt: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    publication: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sdLicense: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    headline: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    materialExtent: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    inLanguage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    material: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    datePublished: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    offers: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    hasPart: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sourceOrganization: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    sponsor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    character: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class CourseProperties(TypedDict):
    """A description of an educational course which may be offered as distinct instances which take place at different times or take place at different locations, or be offered through different media or modes of study. An educational course is a sequence of one or more educational events and/or creative works which aims to build knowledge, competence or ability of learners.

    References:
        https://schema.org/Course
    Note:
        Model Depth 3
    Attributes:
        occupationalCredentialAwarded: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A description of the qualification, award, certificate, diploma or other occupational credential awarded as a consequence of successful completion of this course or program.
        coursePrerequisites: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Requirements for taking the Course. May be completion of another [[Course]] or a textual description like "permission of instructor". Requirements may be a pre-requisite competency, referenced using [[AlignmentObject]].
        educationalCredentialAwarded: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A description of the qualification, award, certificate, diploma or other educational credential awarded as a consequence of successful completion of this course or program.
        courseCode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The identifier for the [[Course]] used by the course [[provider]] (e.g. CS101 or 6.001).
        numberOfCredits: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.
        hasCourseInstance: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An offering of the course at a specific time and place or through specific media or mode of study or to a specific section of students.
    """

    occupationalCredentialAwarded: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    coursePrerequisites: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    educationalCredentialAwarded: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    courseCode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    numberOfCredits: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    hasCourseInstance: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class CourseAllProperties(CourseInheritedProperties, CourseProperties, TypedDict):
    pass


class CourseBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Course", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"educationalLevel": {"exclude": True}}
        fields = {"competencyRequired": {"exclude": True}}
        fields = {"educationalUse": {"exclude": True}}
        fields = {"educationalAlignment": {"exclude": True}}
        fields = {"assesses": {"exclude": True}}
        fields = {"learningResourceType": {"exclude": True}}
        fields = {"teaches": {"exclude": True}}
        fields = {"workTranslation": {"exclude": True}}
        fields = {"educationalLevel": {"exclude": True}}
        fields = {"associatedMedia": {"exclude": True}}
        fields = {"exampleOfWork": {"exclude": True}}
        fields = {"releasedEvent": {"exclude": True}}
        fields = {"version": {"exclude": True}}
        fields = {"locationCreated": {"exclude": True}}
        fields = {"acquireLicensePage": {"exclude": True}}
        fields = {"thumbnailUrl": {"exclude": True}}
        fields = {"provider": {"exclude": True}}
        fields = {"expires": {"exclude": True}}
        fields = {"contentLocation": {"exclude": True}}
        fields = {"educationalUse": {"exclude": True}}
        fields = {"copyrightHolder": {"exclude": True}}
        fields = {"accessibilityControl": {"exclude": True}}
        fields = {"maintainer": {"exclude": True}}
        fields = {"educationalAlignment": {"exclude": True}}
        fields = {"spatial": {"exclude": True}}
        fields = {"publisher": {"exclude": True}}
        fields = {"keywords": {"exclude": True}}
        fields = {"assesses": {"exclude": True}}
        fields = {"reviews": {"exclude": True}}
        fields = {"isBasedOn": {"exclude": True}}
        fields = {"mentions": {"exclude": True}}
        fields = {"publishingPrinciples": {"exclude": True}}
        fields = {"contributor": {"exclude": True}}
        fields = {"license": {"exclude": True}}
        fields = {"citation": {"exclude": True}}
        fields = {"accessibilitySummary": {"exclude": True}}
        fields = {"award": {"exclude": True}}
        fields = {"commentCount": {"exclude": True}}
        fields = {"temporalCoverage": {"exclude": True}}
        fields = {"dateCreated": {"exclude": True}}
        fields = {"discussionUrl": {"exclude": True}}
        fields = {"copyrightNotice": {"exclude": True}}
        fields = {"learningResourceType": {"exclude": True}}
        fields = {"awards": {"exclude": True}}
        fields = {"accessModeSufficient": {"exclude": True}}
        fields = {"review": {"exclude": True}}
        fields = {"conditionsOfAccess": {"exclude": True}}
        fields = {"interactivityType": {"exclude": True}}
        fields = {"abstract": {"exclude": True}}
        fields = {"fileFormat": {"exclude": True}}
        fields = {"interpretedAsClaim": {"exclude": True}}
        fields = {"text": {"exclude": True}}
        fields = {"archivedAt": {"exclude": True}}
        fields = {"alternativeHeadline": {"exclude": True}}
        fields = {"creditText": {"exclude": True}}
        fields = {"funding": {"exclude": True}}
        fields = {"interactionStatistic": {"exclude": True}}
        fields = {"workExample": {"exclude": True}}
        fields = {"about": {"exclude": True}}
        fields = {"encodings": {"exclude": True}}
        fields = {"funder": {"exclude": True}}
        fields = {"video": {"exclude": True}}
        fields = {"isPartOf": {"exclude": True}}
        fields = {"pattern": {"exclude": True}}
        fields = {"editor": {"exclude": True}}
        fields = {"dateModified": {"exclude": True}}
        fields = {"translationOfWork": {"exclude": True}}
        fields = {"creativeWorkStatus": {"exclude": True}}
        fields = {"isBasedOnUrl": {"exclude": True}}
        fields = {"isFamilyFriendly": {"exclude": True}}
        fields = {"isAccessibleForFree": {"exclude": True}}
        fields = {"author": {"exclude": True}}
        fields = {"contentReferenceTime": {"exclude": True}}
        fields = {"correction": {"exclude": True}}
        fields = {"sdDatePublished": {"exclude": True}}
        fields = {"comment": {"exclude": True}}
        fields = {"countryOfOrigin": {"exclude": True}}
        fields = {"timeRequired": {"exclude": True}}
        fields = {"typicalAgeRange": {"exclude": True}}
        fields = {"genre": {"exclude": True}}
        fields = {"producer": {"exclude": True}}
        fields = {"schemaVersion": {"exclude": True}}
        fields = {"audience": {"exclude": True}}
        fields = {"encoding": {"exclude": True}}
        fields = {"publisherImprint": {"exclude": True}}
        fields = {"accessibilityAPI": {"exclude": True}}
        fields = {"sdPublisher": {"exclude": True}}
        fields = {"audio": {"exclude": True}}
        fields = {"accessibilityFeature": {"exclude": True}}
        fields = {"spatialCoverage": {"exclude": True}}
        fields = {"accessMode": {"exclude": True}}
        fields = {"editEIDR": {"exclude": True}}
        fields = {"usageInfo": {"exclude": True}}
        fields = {"position": {"exclude": True}}
        fields = {"encodingFormat": {"exclude": True}}
        fields = {"copyrightYear": {"exclude": True}}
        fields = {"mainEntity": {"exclude": True}}
        fields = {"creator": {"exclude": True}}
        fields = {"teaches": {"exclude": True}}
        fields = {"temporal": {"exclude": True}}
        fields = {"size": {"exclude": True}}
        fields = {"translator": {"exclude": True}}
        fields = {"aggregateRating": {"exclude": True}}
        fields = {"accountablePerson": {"exclude": True}}
        fields = {"accessibilityHazard": {"exclude": True}}
        fields = {"contentRating": {"exclude": True}}
        fields = {"recordedAt": {"exclude": True}}
        fields = {"publication": {"exclude": True}}
        fields = {"sdLicense": {"exclude": True}}
        fields = {"headline": {"exclude": True}}
        fields = {"materialExtent": {"exclude": True}}
        fields = {"inLanguage": {"exclude": True}}
        fields = {"material": {"exclude": True}}
        fields = {"datePublished": {"exclude": True}}
        fields = {"offers": {"exclude": True}}
        fields = {"hasPart": {"exclude": True}}
        fields = {"sourceOrganization": {"exclude": True}}
        fields = {"sponsor": {"exclude": True}}
        fields = {"character": {"exclude": True}}
        fields = {"occupationalCredentialAwarded": {"exclude": True}}
        fields = {"coursePrerequisites": {"exclude": True}}
        fields = {"educationalCredentialAwarded": {"exclude": True}}
        fields = {"courseCode": {"exclude": True}}
        fields = {"numberOfCredits": {"exclude": True}}
        fields = {"hasCourseInstance": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        CourseProperties, CourseInheritedProperties, CourseAllProperties
    ] = CourseAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Course"
    return model


Course = create_schema_org_model()


def create_course_model(
    model: Union[CourseProperties, CourseInheritedProperties, CourseAllProperties]
):
    _type = deepcopy(CourseAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of CourseAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CourseAllProperties):
    pydantic_type = create_course_model(model=model)
    return pydantic_type(model).schema_json()
