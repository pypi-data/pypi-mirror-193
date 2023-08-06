"""
The act of capturing sound and moving images on film, video, or digitally.

https://schema.org/FilmAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FilmActionInheritedProperties(TypedDict):
    """The act of capturing sound and moving images on film, video, or digitally.

    References:
        https://schema.org/FilmAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class FilmActionProperties(TypedDict):
    """The act of capturing sound and moving images on film, video, or digitally.

    References:
        https://schema.org/FilmAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(FilmActionInheritedProperties , FilmActionProperties, TypedDict):
    pass


class FilmActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="FilmAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[FilmActionProperties, FilmActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FilmAction"
    return model
    

FilmAction = create_schema_org_model()


def create_filmaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_filmaction_model(model=model)
    return pydantic_type(model).schema_json()


