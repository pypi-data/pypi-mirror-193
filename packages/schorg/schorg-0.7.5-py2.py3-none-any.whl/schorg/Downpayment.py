"""
Represents the downpayment (up-front payment) price component of the total price for an offered product that has additional installment payments.

https://schema.org/Downpayment
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DownpaymentInheritedProperties(TypedDict):
    """Represents the downpayment (up-front payment) price component of the total price for an offered product that has additional installment payments.

    References:
        https://schema.org/Downpayment
    Note:
        Model Depth 5
    Attributes:
    """


class DownpaymentProperties(TypedDict):
    """Represents the downpayment (up-front payment) price component of the total price for an offered product that has additional installment payments.

    References:
        https://schema.org/Downpayment
    Note:
        Model Depth 5
    Attributes:
    """


class DownpaymentAllProperties(
    DownpaymentInheritedProperties, DownpaymentProperties, TypedDict
):
    pass


class DownpaymentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Downpayment", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DownpaymentProperties, DownpaymentInheritedProperties, DownpaymentAllProperties
    ] = DownpaymentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Downpayment"
    return model


Downpayment = create_schema_org_model()


def create_downpayment_model(
    model: Union[
        DownpaymentProperties, DownpaymentInheritedProperties, DownpaymentAllProperties
    ]
):
    _type = deepcopy(DownpaymentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Downpayment. Please see: https://schema.org/Downpayment"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DownpaymentAllProperties):
    pydantic_type = create_downpayment_model(model=model)
    return pydantic_type(model).schema_json()
