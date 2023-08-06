"""
The drug's cost represents the maximum reimbursement paid by an insurer for the drug.

https://schema.org/ReimbursementCap
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReimbursementCapInheritedProperties(TypedDict):
    """The drug's cost represents the maximum reimbursement paid by an insurer for the drug.

    References:
        https://schema.org/ReimbursementCap
    Note:
        Model Depth 6
    Attributes:
    """

    


class ReimbursementCapProperties(TypedDict):
    """The drug's cost represents the maximum reimbursement paid by an insurer for the drug.

    References:
        https://schema.org/ReimbursementCap
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(ReimbursementCapInheritedProperties , ReimbursementCapProperties, TypedDict):
    pass


class ReimbursementCapBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReimbursementCap",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReimbursementCapProperties, ReimbursementCapInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReimbursementCap"
    return model
    

ReimbursementCap = create_schema_org_model()


def create_reimbursementcap_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_reimbursementcap_model(model=model)
    return pydantic_type(model).schema_json()


