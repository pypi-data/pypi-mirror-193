"""
Represents the cleaning fee part of the total price for an offered product, for example a vacation rental.

https://schema.org/CleaningFee
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CleaningFeeInheritedProperties(TypedDict):
    """Represents the cleaning fee part of the total price for an offered product, for example a vacation rental.

    References:
        https://schema.org/CleaningFee
    Note:
        Model Depth 5
    Attributes:
    """


class CleaningFeeProperties(TypedDict):
    """Represents the cleaning fee part of the total price for an offered product, for example a vacation rental.

    References:
        https://schema.org/CleaningFee
    Note:
        Model Depth 5
    Attributes:
    """


class CleaningFeeAllProperties(
    CleaningFeeInheritedProperties, CleaningFeeProperties, TypedDict
):
    pass


class CleaningFeeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CleaningFee", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CleaningFeeProperties, CleaningFeeInheritedProperties, CleaningFeeAllProperties
    ] = CleaningFeeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CleaningFee"
    return model


CleaningFee = create_schema_org_model()


def create_cleaningfee_model(
    model: Union[
        CleaningFeeProperties, CleaningFeeInheritedProperties, CleaningFeeAllProperties
    ]
):
    _type = deepcopy(CleaningFeeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of CleaningFeeAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CleaningFeeAllProperties):
    pydantic_type = create_cleaningfee_model(model=model)
    return pydantic_type(model).schema_json()
