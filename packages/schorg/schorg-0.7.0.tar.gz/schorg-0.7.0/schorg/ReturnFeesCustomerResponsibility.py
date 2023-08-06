"""
Specifies that product returns must be paid for, and are the responsibility of, the customer.

https://schema.org/ReturnFeesCustomerResponsibility
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnFeesCustomerResponsibilityInheritedProperties(TypedDict):
    """Specifies that product returns must be paid for, and are the responsibility of, the customer.

    References:
        https://schema.org/ReturnFeesCustomerResponsibility
    Note:
        Model Depth 5
    Attributes:
    """

    


class ReturnFeesCustomerResponsibilityProperties(TypedDict):
    """Specifies that product returns must be paid for, and are the responsibility of, the customer.

    References:
        https://schema.org/ReturnFeesCustomerResponsibility
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ReturnFeesCustomerResponsibilityInheritedProperties , ReturnFeesCustomerResponsibilityProperties, TypedDict):
    pass


class ReturnFeesCustomerResponsibilityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReturnFeesCustomerResponsibility",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReturnFeesCustomerResponsibilityProperties, ReturnFeesCustomerResponsibilityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnFeesCustomerResponsibility"
    return model
    

ReturnFeesCustomerResponsibility = create_schema_org_model()


def create_returnfeescustomerresponsibility_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_returnfeescustomerresponsibility_model(model=model)
    return pydantic_type(model).schema_json()


