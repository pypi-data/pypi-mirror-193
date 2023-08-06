"""
Represents the activation fee part of the total price for an offered product, for example a cellphone contract.

https://schema.org/ActivationFee
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ActivationFeeInheritedProperties(TypedDict):
    """Represents the activation fee part of the total price for an offered product, for example a cellphone contract.

    References:
        https://schema.org/ActivationFee
    Note:
        Model Depth 5
    Attributes:
    """


class ActivationFeeProperties(TypedDict):
    """Represents the activation fee part of the total price for an offered product, for example a cellphone contract.

    References:
        https://schema.org/ActivationFee
    Note:
        Model Depth 5
    Attributes:
    """


class ActivationFeeAllProperties(
    ActivationFeeInheritedProperties, ActivationFeeProperties, TypedDict
):
    pass


class ActivationFeeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ActivationFee", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ActivationFeeProperties,
        ActivationFeeInheritedProperties,
        ActivationFeeAllProperties,
    ] = ActivationFeeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ActivationFee"
    return model


ActivationFee = create_schema_org_model()


def create_activationfee_model(
    model: Union[
        ActivationFeeProperties,
        ActivationFeeInheritedProperties,
        ActivationFeeAllProperties,
    ]
):
    _type = deepcopy(ActivationFeeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ActivationFee. Please see: https://schema.org/ActivationFee"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ActivationFeeAllProperties):
    pydantic_type = create_activationfee_model(model=model)
    return pydantic_type(model).schema_json()
