"""
A field of public health focusing on improving health characteristics of a defined population in relation with their geographical or environment areas.

https://schema.org/CommunityHealth
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CommunityHealthInheritedProperties(TypedDict):
    """A field of public health focusing on improving health characteristics of a defined population in relation with their geographical or environment areas.

    References:
        https://schema.org/CommunityHealth
    Note:
        Model Depth 5
    Attributes:
    """

    


class CommunityHealthProperties(TypedDict):
    """A field of public health focusing on improving health characteristics of a defined population in relation with their geographical or environment areas.

    References:
        https://schema.org/CommunityHealth
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(CommunityHealthInheritedProperties , CommunityHealthProperties, TypedDict):
    pass


class CommunityHealthBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CommunityHealth",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[CommunityHealthProperties, CommunityHealthInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CommunityHealth"
    return model
    

CommunityHealth = create_schema_org_model()


def create_communityhealth_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_communityhealth_model(model=model)
    return pydantic_type(model).schema_json()


