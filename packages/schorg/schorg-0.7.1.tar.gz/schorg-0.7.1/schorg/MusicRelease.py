"""
A MusicRelease is a specific release of a music album.

https://schema.org/MusicRelease
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MusicReleaseInheritedProperties(TypedDict):
    """A MusicRelease is a specific release of a music album.

    References:
        https://schema.org/MusicRelease
    Note:
        Model Depth 4
    Attributes:
        tracks: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A music recording (track)&#x2014;usually a single song.
        track: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A music recording (track)&#x2014;usually a single song. If an ItemList is given, the list should contain items of type MusicRecording.
        numTracks: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The number of tracks in this album or playlist.
    """

    tracks: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    track: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numTracks: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    


class MusicReleaseProperties(TypedDict):
    """A MusicRelease is a specific release of a music album.

    References:
        https://schema.org/MusicRelease
    Note:
        Model Depth 4
    Attributes:
        releaseOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The album this is a release of.
        musicReleaseFormat: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Format of this release (the type of recording media used, i.e. compact disc, digital media, LP, etc.).
        duration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).
        recordLabel: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The label that issued the release.
        catalogNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The catalog number for the release.
        creditedTo: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The group the release is credited to if different than the byArtist. For example, Red and Blue is credited to "Stefani Germanotta Band", but by Lady Gaga.
    """

    releaseOf: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    musicReleaseFormat: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    duration: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    recordLabel: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    catalogNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    creditedTo: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(MusicReleaseInheritedProperties , MusicReleaseProperties, TypedDict):
    pass


class MusicReleaseBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MusicRelease",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'tracks': {'exclude': True}}
        fields = {'track': {'exclude': True}}
        fields = {'numTracks': {'exclude': True}}
        fields = {'releaseOf': {'exclude': True}}
        fields = {'musicReleaseFormat': {'exclude': True}}
        fields = {'duration': {'exclude': True}}
        fields = {'recordLabel': {'exclude': True}}
        fields = {'catalogNumber': {'exclude': True}}
        fields = {'creditedTo': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MusicReleaseProperties, MusicReleaseInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MusicRelease"
    return model
    

MusicRelease = create_schema_org_model()


def create_musicrelease_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_musicrelease_model(model=model)
    return pydantic_type(model).schema_json()


