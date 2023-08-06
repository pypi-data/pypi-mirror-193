"""
A music video file.

https://schema.org/MusicVideoObject
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MusicVideoObjectInheritedProperties(TypedDict):
    """A music video file.

    References:
        https://schema.org/MusicVideoObject
    Note:
        Model Depth 4
    Attributes:
        embedUrl: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A URL pointing to a player for a specific video. In general, this is the information in the ```src``` element of an ```embed``` tag and should not be the same as the content of the ```loc``` tag.
        bitrate: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The bitrate of the media object.
        width: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The width of the item.
        sha256: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The [SHA-2](https://en.wikipedia.org/wiki/SHA-2) SHA256 hash of the content of the item. For example, a zero-length input has value 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        endTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        startTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        contentSize: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): File size in (mega/kilo)bytes.
        height: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The height of the item.
        playerType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Player type required&#x2014;for example, Flash or Silverlight.
        associatedArticle: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A NewsArticle associated with the Media Object.
        interpretedAsClaim: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Used to indicate a specific claim contained, implied, translated or refined from the content of a [[MediaObject]] or other [[CreativeWork]]. The interpreting party can be indicated using [[claimInterpreter]].
        duration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).
        requiresSubscription: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): Indicates if use of the media require a subscription  (either paid or free). Allowed values are ```true``` or ```false``` (note that an earlier version had 'yes', 'no').
        regionsAllowed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The regions where the media is allowed. If not specified, then it's assumed to be allowed everywhere. Specify the countries in [ISO 3166 format](http://en.wikipedia.org/wiki/ISO_3166).
        contentUrl: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Actual bytes of the media object, for example the image file or video file.
        productionCompany: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The production company or studio responsible for the item, e.g. series, video game, episode etc.
        encodesCreativeWork: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The CreativeWork encoded by this media object.
        uploadDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): Date when this media object was uploaded to this site.
        ineligibleRegion: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.See also [[eligibleRegion]].      
        encodingFormat: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Media type typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)), e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.In cases where a [[CreativeWork]] has several media type representations, [[encoding]] can be used to indicate each [[MediaObject]] alongside particular [[encodingFormat]] information.Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.
    """

    embedUrl: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    bitrate: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    width: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sha256: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    endTime: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    startTime: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    contentSize: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    height: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    playerType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    associatedArticle: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    interpretedAsClaim: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    duration: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    requiresSubscription: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    regionsAllowed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    contentUrl: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    productionCompany: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    encodesCreativeWork: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    uploadDate: NotRequired[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]
    ineligibleRegion: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    encodingFormat: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    


class MusicVideoObjectProperties(TypedDict):
    """A music video file.

    References:
        https://schema.org/MusicVideoObject
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(MusicVideoObjectInheritedProperties , MusicVideoObjectProperties, TypedDict):
    pass


class MusicVideoObjectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MusicVideoObject",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
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
        


def create_schema_org_model(type_: Union[MusicVideoObjectProperties, MusicVideoObjectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MusicVideoObject"
    return model
    

MusicVideoObject = create_schema_org_model()


def create_musicvideoobject_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_musicvideoobject_model(model=model)
    return pydantic_type(model).schema_json()


