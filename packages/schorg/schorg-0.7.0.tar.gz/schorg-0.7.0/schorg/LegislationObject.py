"""
A specific object or file containing a Legislation. Note that the same Legislation can be published in multiple files. For example, a digitally signed PDF, a plain PDF and an HTML version.

https://schema.org/LegislationObject
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LegislationObjectInheritedProperties(TypedDict):
    """A specific object or file containing a Legislation. Note that the same Legislation can be published in multiple files. For example, a digitally signed PDF, a plain PDF and an HTML version.

    References:
        https://schema.org/LegislationObject
    Note:
        Model Depth 4
    Attributes:
        legislationTransposes: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates that this legislation (or part of legislation) fulfills the objectives set by another legislation, by passing appropriate implementation measures. Typically, some legislations of European Union's member states or regions transpose European Directives. This indicates a legally binding link between the 2 legislations.
        legislationPassedBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The person or organization that originally passed or made the law: typically parliament (for primary legislation) or government (for secondary legislation). This indicates the "legal author" of the law, as opposed to its physical author.
        legislationDate: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): The date of adoption or signature of the legislation. This is the date at which the text is officially aknowledged to be a legislation, even though it might not even be published or in force.
        legislationConsolidates: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates another legislation taken into account in this consolidated legislation (which is usually the product of an editorial process that revises the legislation). This property should be used multiple times to refer to both the original version or the previous consolidated version, and to the legislations making the change.
        legislationIdentifier: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): An identifier for the legislation. This can be either a string-based identifier, like the CELEX at EU level or the NOR in France, or a web-based, URL/URI identifier, like an ELI (European Legislation Identifier) or an URN-Lex.
        legislationType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The type of the legislation. Examples of values are "law", "act", "directive", "decree", "regulation", "statutory instrument", "loi organique", "règlement grand-ducal", etc., depending on the country.
        legislationChanges: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Another legislation that this legislation changes. This encompasses the notions of amendment, replacement, correction, repeal, or other types of change. This may be a direct change (textual or non-textual amendment) or a consequential or indirect change. The property is to be used to express the existence of a change relationship between two acts rather than the existence of a consolidated version of the text that shows the result of the change. For consolidation relationships, use the <a href="/legislationConsolidates">legislationConsolidates</a> property.
        legislationApplies: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates that this legislation (or part of a legislation) somehow transfers another legislation in a different legislative context. This is an informative link, and it has no legal value. For legally-binding links of transposition, use the <a href="/legislationTransposes">legislationTransposes</a> property. For example an informative consolidated law of a European Union's member state "applies" the consolidated version of the European Directive implemented in it.
        jurisdiction: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates a legal jurisdiction, e.g. of some legislation, or where some government service is based.
        legislationDateVersion: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): The point-in-time at which the provided description of the legislation is valid (e.g.: when looking at the law on the 2016-04-07 (= dateVersion), I get the consolidation of 2015-04-12 of the "National Insurance Contributions Act 2015")
        legislationLegalForce: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Whether the legislation is currently in force, not in force, or partially in force.
        legislationResponsible: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An individual or organization that has some kind of responsibility for the legislation. Typically the ministry who is/was in charge of elaborating the legislation, or the adressee for potential questions about the legislation once it is published.
        legislationJurisdiction: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The jurisdiction from which the legislation originates.
        embedUrl: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A URL pointing to a player for a specific video. In general, this is the information in the ```src``` element of an ```embed``` tag and should not be the same as the content of the ```loc``` tag.
        bitrate: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The bitrate of the media object.
        width: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The width of the item.
        sha256: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The [SHA-2](https://en.wikipedia.org/wiki/SHA-2) SHA256 hash of the content of the item. For example, a zero-length input has value 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        endTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        startTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        contentSize: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): File size in (mega/kilo)bytes.
        height: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The height of the item.
        playerType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Player type required&#x2014;for example, Flash or Silverlight.
        associatedArticle: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A NewsArticle associated with the Media Object.
        interpretedAsClaim: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Used to indicate a specific claim contained, implied, translated or refined from the content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can be indicated using [[claimInterpreter]].
        duration: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).
        requiresSubscription: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates if use of the media require a subscription  (either paid or free). Allowed values are ```true``` or ```false``` (note that an earlier version had 'yes', 'no').
        regionsAllowed: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The regions where the media is allowed. If not specified, then it's assumed to be allowed everywhere. Specify the countries in [ISO 3166 format](http://en.wikipedia.org/wiki/ISO_3166).
        contentUrl: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Actual bytes of the media object, for example the image file or video file.
        productionCompany: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The production company or studio responsible for the item, e.g. series, video game, episode etc.
        encodesCreativeWork: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The CreativeWork encoded by this media object.
        uploadDate: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): Date when this media object was uploaded to this site.
        ineligibleRegion: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.See also [[eligibleRegion]].      
        encodingFormat: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)), e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.In cases where a [[CreativeWork]] has several media type representations, [[encoding]] can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]] information.Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.
    """

    legislationTransposes: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    legislationPassedBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    legislationDate: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    legislationConsolidates: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    legislationIdentifier: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    legislationType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    legislationChanges: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    legislationApplies: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    jurisdiction: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    legislationDateVersion: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    legislationLegalForce: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    legislationResponsible: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    legislationJurisdiction: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    embedUrl: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    bitrate: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    width: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sha256: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    endTime: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]
    startTime: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]
    contentSize: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    height: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    playerType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    associatedArticle: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    interpretedAsClaim: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    duration: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    requiresSubscription: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    regionsAllowed: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    contentUrl: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    productionCompany: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    encodesCreativeWork: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    uploadDate: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    ineligibleRegion: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    encodingFormat: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    


class LegislationObjectProperties(TypedDict):
    """A specific object or file containing a Legislation. Note that the same Legislation can be published in multiple files. For example, a digitally signed PDF, a plain PDF and an HTML version.

    References:
        https://schema.org/LegislationObject
    Note:
        Model Depth 4
    Attributes:
        legislationLegalValue: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The legal value of this legislation file. The same legislation can be written in multiple files with different legal values. Typically a digitally signed PDF have a "stronger" legal value than the HTML file of the same act.
    """

    legislationLegalValue: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(LegislationObjectInheritedProperties , LegislationObjectProperties, TypedDict):
    pass


class LegislationObjectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LegislationObject",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'legislationTransposes': {'exclude': True}}
        fields = {'legislationPassedBy': {'exclude': True}}
        fields = {'legislationDate': {'exclude': True}}
        fields = {'legislationConsolidates': {'exclude': True}}
        fields = {'legislationIdentifier': {'exclude': True}}
        fields = {'legislationType': {'exclude': True}}
        fields = {'legislationChanges': {'exclude': True}}
        fields = {'legislationApplies': {'exclude': True}}
        fields = {'jurisdiction': {'exclude': True}}
        fields = {'legislationDateVersion': {'exclude': True}}
        fields = {'legislationLegalForce': {'exclude': True}}
        fields = {'legislationResponsible': {'exclude': True}}
        fields = {'legislationJurisdiction': {'exclude': True}}
        fields = {'embedUrl': {'exclude': True}}
        fields = {'bitrate': {'exclude': True}}
        fields = {'width': {'exclude': True}}
        fields = {'sha256': {'exclude': True}}
        fields = {'endTime': {'exclude': True}}
        fields = {'startTime': {'exclude': True}}
        fields = {'contentSize': {'exclude': True}}
        fields = {'height': {'exclude': True}}
        fields = {'playerType': {'exclude': True}}
        fields = {'associatedArticle': {'exclude': True}}
        fields = {'interpretedAsClaim': {'exclude': True}}
        fields = {'duration': {'exclude': True}}
        fields = {'requiresSubscription': {'exclude': True}}
        fields = {'regionsAllowed': {'exclude': True}}
        fields = {'contentUrl': {'exclude': True}}
        fields = {'productionCompany': {'exclude': True}}
        fields = {'encodesCreativeWork': {'exclude': True}}
        fields = {'uploadDate': {'exclude': True}}
        fields = {'ineligibleRegion': {'exclude': True}}
        fields = {'encodingFormat': {'exclude': True}}
        fields = {'legislationLegalValue': {'exclude': True}}
        


def create_schema_org_model(type_: Union[LegislationObjectProperties, LegislationObjectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LegislationObject"
    return model
    

LegislationObject = create_schema_org_model()


def create_legislationobject_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_legislationobject_model(model=model)
    return pydantic_type(model).schema_json()


