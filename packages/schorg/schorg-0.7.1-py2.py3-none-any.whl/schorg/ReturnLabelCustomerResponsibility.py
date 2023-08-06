"""
Indicated that creating a return label is the responsibility of the customer.

https://schema.org/ReturnLabelCustomerResponsibility
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnLabelCustomerResponsibilityInheritedProperties(TypedDict):
    """Indicated that creating a return label is the responsibility of the customer.

    References:
        https://schema.org/ReturnLabelCustomerResponsibility
    Note:
        Model Depth 5
    Attributes:
    """

    


class ReturnLabelCustomerResponsibilityProperties(TypedDict):
    """Indicated that creating a return label is the responsibility of the customer.

    References:
        https://schema.org/ReturnLabelCustomerResponsibility
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ReturnLabelCustomerResponsibilityInheritedProperties , ReturnLabelCustomerResponsibilityProperties, TypedDict):
    pass


class ReturnLabelCustomerResponsibilityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReturnLabelCustomerResponsibility",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReturnLabelCustomerResponsibilityProperties, ReturnLabelCustomerResponsibilityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnLabelCustomerResponsibility"
    return model
    

ReturnLabelCustomerResponsibility = create_schema_org_model()


def create_returnlabelcustomerresponsibility_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_returnlabelcustomerresponsibility_model(model=model)
    return pydantic_type(model).schema_json()


