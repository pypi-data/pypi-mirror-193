"""
Professional service: Attorney. This type is deprecated - [[LegalService]] is more inclusive and less ambiguous.

https://schema.org/Attorney
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AttorneyInheritedProperties(TypedDict):
    """Professional service: Attorney. This type is deprecated - [[LegalService]] is more inclusive and less ambiguous.

    References:
        https://schema.org/Attorney
    Note:
        Model Depth 5
    Attributes:
    """

    


class AttorneyProperties(TypedDict):
    """Professional service: Attorney. This type is deprecated - [[LegalService]] is more inclusive and less ambiguous.

    References:
        https://schema.org/Attorney
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(AttorneyInheritedProperties , AttorneyProperties, TypedDict):
    pass


class AttorneyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Attorney",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[AttorneyProperties, AttorneyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Attorney"
    return model
    

Attorney = create_schema_org_model()


def create_attorney_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_attorney_model(model=model)
    return pydantic_type(model).schema_json()


