"""
A short radio program or a segment/part of a radio program.

https://schema.org/RadioClip
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RadioClipInheritedProperties(TypedDict):
    """A short radio program or a segment/part of a radio program.

    References:
        https://schema.org/RadioClip
    Note:
        Model Depth 4
    Attributes:
        actors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        actor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        clipNumber: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): Position of the clip within an ordered group of clips.
        partOfEpisode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The episode to which this clip belongs.
        partOfSeason: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The season to which this episode belongs.
        startOffset: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The start time of the clip expressed as the number of seconds from the beginning of the work.
        partOfSeries: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The series to which this episode or season belongs.
        endOffset: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The end time of the clip expressed as the number of seconds from the beginning of the work.
        director: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        directors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        musicBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The composer of the soundtrack.
    """

    actors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    clipNumber: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    partOfEpisode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    partOfSeason: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    startOffset: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    partOfSeries: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    endOffset: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    director: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    directors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    musicBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class RadioClipProperties(TypedDict):
    """A short radio program or a segment/part of a radio program.

    References:
        https://schema.org/RadioClip
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(RadioClipInheritedProperties , RadioClipProperties, TypedDict):
    pass


class RadioClipBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RadioClip",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'actors': {'exclude': True}}
        fields = {'actor': {'exclude': True}}
        fields = {'clipNumber': {'exclude': True}}
        fields = {'partOfEpisode': {'exclude': True}}
        fields = {'partOfSeason': {'exclude': True}}
        fields = {'startOffset': {'exclude': True}}
        fields = {'partOfSeries': {'exclude': True}}
        fields = {'endOffset': {'exclude': True}}
        fields = {'director': {'exclude': True}}
        fields = {'directors': {'exclude': True}}
        fields = {'musicBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[RadioClipProperties, RadioClipInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RadioClip"
    return model
    

RadioClip = create_schema_org_model()


def create_radioclip_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_radioclip_model(model=model)
    return pydantic_type(model).schema_json()


