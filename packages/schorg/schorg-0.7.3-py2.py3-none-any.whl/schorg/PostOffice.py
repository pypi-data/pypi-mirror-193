"""
A post office.

https://schema.org/PostOffice
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PostOfficeInheritedProperties(TypedDict):
    """A post office.

    References:
        https://schema.org/PostOffice
    Note:
        Model Depth 5
    Attributes:
    """


class PostOfficeProperties(TypedDict):
    """A post office.

    References:
        https://schema.org/PostOffice
    Note:
        Model Depth 5
    Attributes:
    """


class PostOfficeAllProperties(
    PostOfficeInheritedProperties, PostOfficeProperties, TypedDict
):
    pass


class PostOfficeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PostOffice", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PostOfficeProperties, PostOfficeInheritedProperties, PostOfficeAllProperties
    ] = PostOfficeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PostOffice"
    return model


PostOffice = create_schema_org_model()


def create_postoffice_model(
    model: Union[
        PostOfficeProperties, PostOfficeInheritedProperties, PostOfficeAllProperties
    ]
):
    _type = deepcopy(PostOfficeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PostOfficeAllProperties):
    pydantic_type = create_postoffice_model(model=model)
    return pydantic_type(model).schema_json()
