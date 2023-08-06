"""
Represents the installment pricing component of the total price for an offered product.

https://schema.org/Installment
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InstallmentInheritedProperties(TypedDict):
    """Represents the installment pricing component of the total price for an offered product.

    References:
        https://schema.org/Installment
    Note:
        Model Depth 5
    Attributes:
    """


class InstallmentProperties(TypedDict):
    """Represents the installment pricing component of the total price for an offered product.

    References:
        https://schema.org/Installment
    Note:
        Model Depth 5
    Attributes:
    """


class InstallmentAllProperties(
    InstallmentInheritedProperties, InstallmentProperties, TypedDict
):
    pass


class InstallmentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Installment", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        InstallmentProperties, InstallmentInheritedProperties, InstallmentAllProperties
    ] = InstallmentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Installment"
    return model


Installment = create_schema_org_model()


def create_installment_model(
    model: Union[
        InstallmentProperties, InstallmentInheritedProperties, InstallmentAllProperties
    ]
):
    _type = deepcopy(InstallmentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: InstallmentAllProperties):
    pydantic_type = create_installment_model(model=model)
    return pydantic_type(model).schema_json()
