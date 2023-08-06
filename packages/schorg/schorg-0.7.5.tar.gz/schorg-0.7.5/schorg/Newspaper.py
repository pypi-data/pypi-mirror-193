"""
A publication containing information about varied topics that are pertinent to general information, a geographic area, or a specific subject matter (i.e. business, culture, education). Often published daily.

https://schema.org/Newspaper
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NewspaperInheritedProperties(TypedDict):
    """A publication containing information about varied topics that are pertinent to general information, a geographic area, or a specific subject matter (i.e. business, culture, education). Often published daily.

    References:
        https://schema.org/Newspaper
    Note:
        Model Depth 5
    Attributes:
    """


class NewspaperProperties(TypedDict):
    """A publication containing information about varied topics that are pertinent to general information, a geographic area, or a specific subject matter (i.e. business, culture, education). Often published daily.

    References:
        https://schema.org/Newspaper
    Note:
        Model Depth 5
    Attributes:
    """


class NewspaperAllProperties(
    NewspaperInheritedProperties, NewspaperProperties, TypedDict
):
    pass


class NewspaperBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Newspaper", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NewspaperProperties, NewspaperInheritedProperties, NewspaperAllProperties
    ] = NewspaperAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Newspaper"
    return model


Newspaper = create_schema_org_model()


def create_newspaper_model(
    model: Union[
        NewspaperProperties, NewspaperInheritedProperties, NewspaperAllProperties
    ]
):
    _type = deepcopy(NewspaperAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Newspaper. Please see: https://schema.org/Newspaper"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: NewspaperAllProperties):
    pydantic_type = create_newspaper_model(model=model)
    return pydantic_type(model).schema_json()
