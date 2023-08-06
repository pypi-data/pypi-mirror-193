"""
PaidLeave: this is a benefit for paid leave.

https://schema.org/PaidLeave
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaidLeaveInheritedProperties(TypedDict):
    """PaidLeave: this is a benefit for paid leave.

    References:
        https://schema.org/PaidLeave
    Note:
        Model Depth 5
    Attributes:
    """

    


class PaidLeaveProperties(TypedDict):
    """PaidLeave: this is a benefit for paid leave.

    References:
        https://schema.org/PaidLeave
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PaidLeaveInheritedProperties , PaidLeaveProperties, TypedDict):
    pass


class PaidLeaveBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PaidLeave",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PaidLeaveProperties, PaidLeaveInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaidLeave"
    return model
    

PaidLeave = create_schema_org_model()


def create_paidleave_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_paidleave_model(model=model)
    return pydantic_type(model).schema_json()


