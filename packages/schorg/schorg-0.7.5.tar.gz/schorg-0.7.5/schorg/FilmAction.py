"""
The act of capturing sound and moving images on film, video, or digitally.

https://schema.org/FilmAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class FilmActionAllProperties(
    FilmActionInheritedProperties, FilmActionProperties, TypedDict
):
    pass


class FilmActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FilmAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FilmActionProperties, FilmActionInheritedProperties, FilmActionAllProperties
    ] = FilmActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FilmAction"
    return model


FilmAction = create_schema_org_model()


def create_filmaction_model(
    model: Union[
        FilmActionProperties, FilmActionInheritedProperties, FilmActionAllProperties
    ]
):
    _type = deepcopy(FilmActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of FilmAction. Please see: https://schema.org/FilmAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: FilmActionAllProperties):
    pydantic_type = create_filmaction_model(model=model)
    return pydantic_type(model).schema_json()
