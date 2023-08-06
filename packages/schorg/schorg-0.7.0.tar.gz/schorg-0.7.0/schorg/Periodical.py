"""
A publication in any medium issued in successive parts bearing numerical or chronological designations and intended to continue indefinitely, such as a magazine, scholarly journal, or newspaper.See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

https://schema.org/Periodical
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PeriodicalInheritedProperties(TypedDict):
    """A publication in any medium issued in successive parts bearing numerical or chronological designations and intended to continue indefinitely, such as a magazine, scholarly journal, or newspaper.See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

    References:
        https://schema.org/Periodical
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
    


class PeriodicalProperties(TypedDict):
    """A publication in any medium issued in successive parts bearing numerical or chronological designations and intended to continue indefinitely, such as a magazine, scholarly journal, or newspaper.See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

    References:
        https://schema.org/Periodical
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(PeriodicalInheritedProperties , PeriodicalProperties, TypedDict):
    pass


class PeriodicalBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Periodical",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'issn': {'exclude': True}}
        fields = {'startDate': {'exclude': True}}
        fields = {'endDate': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PeriodicalProperties, PeriodicalInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Periodical"
    return model
    

Periodical = create_schema_org_model()


def create_periodical_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_periodical_model(model=model)
    return pydantic_type(model).schema_json()


