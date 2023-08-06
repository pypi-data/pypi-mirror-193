"""
A podcast is an episodic series of digital audio or video files which a user can download and listen to.

https://schema.org/PodcastSeries
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PodcastSeriesInheritedProperties(TypedDict):
    """A podcast is an episodic series of digital audio or video files which a user can download and listen to.

    References:
        https://schema.org/PodcastSeries
    Note:
        Model Depth 4
    Attributes:
        issn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication.
        startDate: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    issn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    startDate: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    endDate: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    


class PodcastSeriesProperties(TypedDict):
    """A podcast is an episodic series of digital audio or video files which a user can download and listen to.

    References:
        https://schema.org/PodcastSeries
    Note:
        Model Depth 4
    Attributes:
        actor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        webFeed: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The URL for a feed, e.g. associated with a podcast series, blog, or series of date-stamped updates. This is usually RSS or Atom.
    """

    actor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    webFeed: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    


class AllProperties(PodcastSeriesInheritedProperties , PodcastSeriesProperties, TypedDict):
    pass


class PodcastSeriesBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PodcastSeries",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'issn': {'exclude': True}}
        fields = {'startDate': {'exclude': True}}
        fields = {'endDate': {'exclude': True}}
        fields = {'actor': {'exclude': True}}
        fields = {'webFeed': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PodcastSeriesProperties, PodcastSeriesInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PodcastSeries"
    return model
    

PodcastSeries = create_schema_org_model()


def create_podcastseries_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_podcastseries_model(model=model)
    return pydantic_type(model).schema_json()


