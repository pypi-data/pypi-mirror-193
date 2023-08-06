"""
CharitableIncorporatedOrganization: Non-profit type referring to a Charitable Incorporated Organization (UK).

https://schema.org/CharitableIncorporatedOrganization
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CharitableIncorporatedOrganizationInheritedProperties(TypedDict):
    """CharitableIncorporatedOrganization: Non-profit type referring to a Charitable Incorporated Organization (UK).

    References:
        https://schema.org/CharitableIncorporatedOrganization
    Note:
        Model Depth 6
    Attributes:
    """

    


class CharitableIncorporatedOrganizationProperties(TypedDict):
    """CharitableIncorporatedOrganization: Non-profit type referring to a Charitable Incorporated Organization (UK).

    References:
        https://schema.org/CharitableIncorporatedOrganization
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(CharitableIncorporatedOrganizationInheritedProperties , CharitableIncorporatedOrganizationProperties, TypedDict):
    pass


class CharitableIncorporatedOrganizationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CharitableIncorporatedOrganization",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[CharitableIncorporatedOrganizationProperties, CharitableIncorporatedOrganizationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CharitableIncorporatedOrganization"
    return model
    

CharitableIncorporatedOrganization = create_schema_org_model()


def create_charitableincorporatedorganization_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_charitableincorporatedorganization_model(model=model)
    return pydantic_type(model).schema_json()


