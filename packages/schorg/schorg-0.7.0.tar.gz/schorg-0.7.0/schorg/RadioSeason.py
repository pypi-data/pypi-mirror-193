"""
Season dedicated to radio broadcast and associated online delivery.

https://schema.org/RadioSeason
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RadioSeasonInheritedProperties(TypedDict):
    """Season dedicated to radio broadcast and associated online delivery.

    References:
        https://schema.org/RadioSeason
    Note:
        Model Depth 4
    Attributes:
        seasonNumber: (Optional[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]): Position of the season within an ordered group of seasons.
        actor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        trailer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The trailer of a movie or TV/radio series, season, episode, etc.
        productionCompany: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The production company or studio responsible for the item, e.g. series, video game, episode etc.
        episodes: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An episode of a TV/radio series or season.
        partOfSeries: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The series to which this episode or season belongs.
        episode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An episode of a TV, radio or game media within a series or season.
        director: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        startDate: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        numberOfEpisodes: (Optional[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]): The number of episodes in this season or series.
        endDate: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    seasonNumber: NotRequired[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]
    actor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    trailer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    productionCompany: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    episodes: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    partOfSeries: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    episode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    director: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    startDate: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    numberOfEpisodes: NotRequired[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]
    endDate: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    


class RadioSeasonProperties(TypedDict):
    """Season dedicated to radio broadcast and associated online delivery.

    References:
        https://schema.org/RadioSeason
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(RadioSeasonInheritedProperties , RadioSeasonProperties, TypedDict):
    pass


class RadioSeasonBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RadioSeason",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'seasonNumber': {'exclude': True}}
        fields = {'actor': {'exclude': True}}
        fields = {'trailer': {'exclude': True}}
        fields = {'productionCompany': {'exclude': True}}
        fields = {'episodes': {'exclude': True}}
        fields = {'partOfSeries': {'exclude': True}}
        fields = {'episode': {'exclude': True}}
        fields = {'director': {'exclude': True}}
        fields = {'startDate': {'exclude': True}}
        fields = {'numberOfEpisodes': {'exclude': True}}
        fields = {'endDate': {'exclude': True}}
        


def create_schema_org_model(type_: Union[RadioSeasonProperties, RadioSeasonInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RadioSeason"
    return model
    

RadioSeason = create_schema_org_model()


def create_radioseason_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_radioseason_model(model=model)
    return pydantic_type(model).schema_json()


