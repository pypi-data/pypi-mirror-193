"""
An action that has already taken place.

https://schema.org/CompletedActionStatus
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CompletedActionStatusInheritedProperties(TypedDict):
    """An action that has already taken place.

    References:
        https://schema.org/CompletedActionStatus
    Note:
        Model Depth 6
    Attributes:
    """

    


class CompletedActionStatusProperties(TypedDict):
    """An action that has already taken place.

    References:
        https://schema.org/CompletedActionStatus
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(CompletedActionStatusInheritedProperties , CompletedActionStatusProperties, TypedDict):
    pass


class CompletedActionStatusBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CompletedActionStatus",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[CompletedActionStatusProperties, CompletedActionStatusInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CompletedActionStatus"
    return model
    

CompletedActionStatus = create_schema_org_model()


def create_completedactionstatus_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_completedactionstatus_model(model=model)
    return pydantic_type(model).schema_json()


