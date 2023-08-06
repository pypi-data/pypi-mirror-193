"""
A post office.

https://schema.org/PostOffice
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(PostOfficeInheritedProperties , PostOfficeProperties, TypedDict):
    pass


class PostOfficeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PostOffice",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PostOfficeProperties, PostOfficeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PostOffice"
    return model
    

PostOffice = create_schema_org_model()


def create_postoffice_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_postoffice_model(model=model)
    return pydantic_type(model).schema_json()


