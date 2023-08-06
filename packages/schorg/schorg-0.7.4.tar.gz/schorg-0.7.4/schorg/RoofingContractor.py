"""
A roofing contractor.

https://schema.org/RoofingContractor
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RoofingContractorInheritedProperties(TypedDict):
    """A roofing contractor.

    References:
        https://schema.org/RoofingContractor
    Note:
        Model Depth 5
    Attributes:
    """


class RoofingContractorProperties(TypedDict):
    """A roofing contractor.

    References:
        https://schema.org/RoofingContractor
    Note:
        Model Depth 5
    Attributes:
    """


class RoofingContractorAllProperties(
    RoofingContractorInheritedProperties, RoofingContractorProperties, TypedDict
):
    pass


class RoofingContractorBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RoofingContractor", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RoofingContractorProperties,
        RoofingContractorInheritedProperties,
        RoofingContractorAllProperties,
    ] = RoofingContractorAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RoofingContractor"
    return model


RoofingContractor = create_schema_org_model()


def create_roofingcontractor_model(
    model: Union[
        RoofingContractorProperties,
        RoofingContractorInheritedProperties,
        RoofingContractorAllProperties,
    ]
):
    _type = deepcopy(RoofingContractorAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of RoofingContractorAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RoofingContractorAllProperties):
    pydantic_type = create_roofingcontractor_model(model=model)
    return pydantic_type(model).schema_json()
