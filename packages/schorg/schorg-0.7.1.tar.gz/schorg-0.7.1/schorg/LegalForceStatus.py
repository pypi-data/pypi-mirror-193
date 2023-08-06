"""
A list of possible statuses for the legal force of a legislation.

https://schema.org/LegalForceStatus
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LegalForceStatusInheritedProperties(TypedDict):
    """A list of possible statuses for the legal force of a legislation.

    References:
        https://schema.org/LegalForceStatus
    Note:
        Model Depth 5
    Attributes:
    """

    


class LegalForceStatusProperties(TypedDict):
    """A list of possible statuses for the legal force of a legislation.

    References:
        https://schema.org/LegalForceStatus
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(LegalForceStatusInheritedProperties , LegalForceStatusProperties, TypedDict):
    pass


class LegalForceStatusBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LegalForceStatus",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[LegalForceStatusProperties, LegalForceStatusInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LegalForceStatus"
    return model
    

LegalForceStatus = create_schema_org_model()


def create_legalforcestatus_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_legalforcestatus_model(model=model)
    return pydantic_type(model).schema_json()


