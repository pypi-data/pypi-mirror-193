"""
Book format: Audiobook. This is an enumerated value for use with the bookFormat property. There is also a type 'Audiobook' in the bib extension which includes Audiobook specific properties.

https://schema.org/AudiobookFormat
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AudiobookFormatInheritedProperties(TypedDict):
    """Book format: Audiobook. This is an enumerated value for use with the bookFormat property. There is also a type 'Audiobook' in the bib extension which includes Audiobook specific properties.

    References:
        https://schema.org/AudiobookFormat
    Note:
        Model Depth 5
    Attributes:
    """

    


class AudiobookFormatProperties(TypedDict):
    """Book format: Audiobook. This is an enumerated value for use with the bookFormat property. There is also a type 'Audiobook' in the bib extension which includes Audiobook specific properties.

    References:
        https://schema.org/AudiobookFormat
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(AudiobookFormatInheritedProperties , AudiobookFormatProperties, TypedDict):
    pass


class AudiobookFormatBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AudiobookFormat",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[AudiobookFormatProperties, AudiobookFormatInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AudiobookFormat"
    return model
    

AudiobookFormat = create_schema_org_model()


def create_audiobookformat_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_audiobookformat_model(model=model)
    return pydantic_type(model).schema_json()


