"""
A collection of music tracks.

https://schema.org/MusicAlbum
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MusicAlbumInheritedProperties(TypedDict):
    """A collection of music tracks.

    References:
        https://schema.org/MusicAlbum
    Note:
        Model Depth 4
    Attributes:
        tracks: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A music recording (track)&#x2014;usually a single song.
        track: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A music recording (track)&#x2014;usually a single song. If an ItemList is given, the list should contain items of type MusicRecording.
        numTracks: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of tracks in this album or playlist.
    """

    tracks: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    track: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    numTracks: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]


class MusicAlbumProperties(TypedDict):
    """A collection of music tracks.

    References:
        https://schema.org/MusicAlbum
    Note:
        Model Depth 4
    Attributes:
        albumReleaseType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The kind of release which this album is: single, EP or album.
        albumRelease: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A release of this album.
        byArtist: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The artist that performed this album or recording.
        albumProductionType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Classification of the album by its type of content: soundtrack, live album, studio album, etc.
    """

    albumReleaseType: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    albumRelease: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    byArtist: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    albumProductionType: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class MusicAlbumAllProperties(
    MusicAlbumInheritedProperties, MusicAlbumProperties, TypedDict
):
    pass


class MusicAlbumBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MusicAlbum", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"tracks": {"exclude": True}}
        fields = {"track": {"exclude": True}}
        fields = {"numTracks": {"exclude": True}}
        fields = {"albumReleaseType": {"exclude": True}}
        fields = {"albumRelease": {"exclude": True}}
        fields = {"byArtist": {"exclude": True}}
        fields = {"albumProductionType": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MusicAlbumProperties, MusicAlbumInheritedProperties, MusicAlbumAllProperties
    ] = MusicAlbumAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MusicAlbum"
    return model


MusicAlbum = create_schema_org_model()


def create_musicalbum_model(
    model: Union[
        MusicAlbumProperties, MusicAlbumInheritedProperties, MusicAlbumAllProperties
    ]
):
    _type = deepcopy(MusicAlbumAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MusicAlbumAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MusicAlbumAllProperties):
    pydantic_type = create_musicalbum_model(model=model)
    return pydantic_type(model).schema_json()
