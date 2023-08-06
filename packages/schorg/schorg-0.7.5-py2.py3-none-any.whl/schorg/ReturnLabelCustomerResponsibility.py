"""
Indicated that creating a return label is the responsibility of the customer.

https://schema.org/ReturnLabelCustomerResponsibility
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class ReturnLabelCustomerResponsibilityAllProperties(
    ReturnLabelCustomerResponsibilityInheritedProperties,
    ReturnLabelCustomerResponsibilityProperties,
    TypedDict,
):
    pass


class ReturnLabelCustomerResponsibilityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReturnLabelCustomerResponsibility", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReturnLabelCustomerResponsibilityProperties,
        ReturnLabelCustomerResponsibilityInheritedProperties,
        ReturnLabelCustomerResponsibilityAllProperties,
    ] = ReturnLabelCustomerResponsibilityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnLabelCustomerResponsibility"
    return model


ReturnLabelCustomerResponsibility = create_schema_org_model()


def create_returnlabelcustomerresponsibility_model(
    model: Union[
        ReturnLabelCustomerResponsibilityProperties,
        ReturnLabelCustomerResponsibilityInheritedProperties,
        ReturnLabelCustomerResponsibilityAllProperties,
    ]
):
    _type = deepcopy(ReturnLabelCustomerResponsibilityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ReturnLabelCustomerResponsibility. Please see: https://schema.org/ReturnLabelCustomerResponsibility"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ReturnLabelCustomerResponsibilityAllProperties):
    pydantic_type = create_returnlabelcustomerresponsibility_model(model=model)
    return pydantic_type(model).schema_json()
