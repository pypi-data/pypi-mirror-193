"""
Data type: URL.

https://schema.org/URL
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class URLInheritedProperties(TypedDict):
    """Data type: URL.

    References:
        https://schema.org/URL
    Note:
        Model Depth 6
    Attributes:
    """


class URLProperties(TypedDict):
    """Data type: URL.

    References:
        https://schema.org/URL
    Note:
        Model Depth 6
    Attributes:
    """


class URLAllProperties(URLInheritedProperties, URLProperties, TypedDict):
    pass


class URLBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="URL", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        URLProperties, URLInheritedProperties, URLAllProperties
    ] = URLAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "URL"
    return model


URL = create_schema_org_model()


def create_url_model(
    model: Union[URLProperties, URLInheritedProperties, URLAllProperties]
):
    _type = deepcopy(URLAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of URLAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: URLAllProperties):
    pydantic_type = create_url_model(model=model)
    return pydantic_type(model).schema_json()
