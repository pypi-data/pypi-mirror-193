"""
SingleRelease.

https://schema.org/SingleRelease
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SingleReleaseInheritedProperties(TypedDict):
    """SingleRelease.

    References:
        https://schema.org/SingleRelease
    Note:
        Model Depth 5
    Attributes:
    """

    


class SingleReleaseProperties(TypedDict):
    """SingleRelease.

    References:
        https://schema.org/SingleRelease
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(SingleReleaseInheritedProperties , SingleReleaseProperties, TypedDict):
    pass


class SingleReleaseBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SingleRelease",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SingleReleaseProperties, SingleReleaseInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SingleRelease"
    return model
    

SingleRelease = create_schema_org_model()


def create_singlerelease_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_singlerelease_model(model=model)
    return pydantic_type(model).schema_json()


