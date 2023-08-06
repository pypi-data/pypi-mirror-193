"""
A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi.

https://schema.org/CarUsageType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CarUsageTypeInheritedProperties(TypedDict):
    """A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi.

    References:
        https://schema.org/CarUsageType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class CarUsageTypeProperties(TypedDict):
    """A value indicating a special usage of a car, e.g. commercial rental, driving school, or as a taxi.

    References:
        https://schema.org/CarUsageType
    Note:
        Model Depth 4
    Attributes:
    """


class CarUsageTypeAllProperties(
    CarUsageTypeInheritedProperties, CarUsageTypeProperties, TypedDict
):
    pass


class CarUsageTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CarUsageType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        CarUsageTypeProperties,
        CarUsageTypeInheritedProperties,
        CarUsageTypeAllProperties,
    ] = CarUsageTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CarUsageType"
    return model


CarUsageType = create_schema_org_model()


def create_carusagetype_model(
    model: Union[
        CarUsageTypeProperties,
        CarUsageTypeInheritedProperties,
        CarUsageTypeAllProperties,
    ]
):
    _type = deepcopy(CarUsageTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of CarUsageTypeAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CarUsageTypeAllProperties):
    pydantic_type = create_carusagetype_model(model=model)
    return pydantic_type(model).schema_json()
