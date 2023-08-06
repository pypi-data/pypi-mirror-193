"""
OneTimePayments: this is a benefit for one-time payments for individuals.

https://schema.org/OneTimePayments
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OneTimePaymentsInheritedProperties(TypedDict):
    """OneTimePayments: this is a benefit for one-time payments for individuals.

    References:
        https://schema.org/OneTimePayments
    Note:
        Model Depth 5
    Attributes:
    """


class OneTimePaymentsProperties(TypedDict):
    """OneTimePayments: this is a benefit for one-time payments for individuals.

    References:
        https://schema.org/OneTimePayments
    Note:
        Model Depth 5
    Attributes:
    """


class OneTimePaymentsAllProperties(
    OneTimePaymentsInheritedProperties, OneTimePaymentsProperties, TypedDict
):
    pass


class OneTimePaymentsBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OneTimePayments", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OneTimePaymentsProperties,
        OneTimePaymentsInheritedProperties,
        OneTimePaymentsAllProperties,
    ] = OneTimePaymentsAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OneTimePayments"
    return model


OneTimePayments = create_schema_org_model()


def create_onetimepayments_model(
    model: Union[
        OneTimePaymentsProperties,
        OneTimePaymentsInheritedProperties,
        OneTimePaymentsAllProperties,
    ]
):
    _type = deepcopy(OneTimePaymentsAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of OneTimePayments. Please see: https://schema.org/OneTimePayments"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: OneTimePaymentsAllProperties):
    pydantic_type = create_onetimepayments_model(model=model)
    return pydantic_type(model).schema_json()
