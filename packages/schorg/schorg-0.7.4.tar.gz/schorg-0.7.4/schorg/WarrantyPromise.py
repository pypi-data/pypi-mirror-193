"""
A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.

https://schema.org/WarrantyPromise
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WarrantyPromiseInheritedProperties(TypedDict):
    """A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.

    References:
        https://schema.org/WarrantyPromise
    Note:
        Model Depth 4
    Attributes:
    """


class WarrantyPromiseProperties(TypedDict):
    """A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.

    References:
        https://schema.org/WarrantyPromise
    Note:
        Model Depth 4
    Attributes:
        warrantyScope: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The scope of the warranty promise.
        durationOfWarranty: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The duration of the warranty promise. Common unitCode values are ANN for year, MON for months, or DAY for days.
    """

    warrantyScope: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    durationOfWarranty: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class WarrantyPromiseAllProperties(
    WarrantyPromiseInheritedProperties, WarrantyPromiseProperties, TypedDict
):
    pass


class WarrantyPromiseBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WarrantyPromise", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"warrantyScope": {"exclude": True}}
        fields = {"durationOfWarranty": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        WarrantyPromiseProperties,
        WarrantyPromiseInheritedProperties,
        WarrantyPromiseAllProperties,
    ] = WarrantyPromiseAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WarrantyPromise"
    return model


WarrantyPromise = create_schema_org_model()


def create_warrantypromise_model(
    model: Union[
        WarrantyPromiseProperties,
        WarrantyPromiseInheritedProperties,
        WarrantyPromiseAllProperties,
    ]
):
    _type = deepcopy(WarrantyPromiseAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WarrantyPromiseAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WarrantyPromiseAllProperties):
    pydantic_type = create_warrantypromise_model(model=model)
    return pydantic_type(model).schema_json()
