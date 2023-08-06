"""
A general contractor.

https://schema.org/GeneralContractor
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GeneralContractorInheritedProperties(TypedDict):
    """A general contractor.

    References:
        https://schema.org/GeneralContractor
    Note:
        Model Depth 5
    Attributes:
    """


class GeneralContractorProperties(TypedDict):
    """A general contractor.

    References:
        https://schema.org/GeneralContractor
    Note:
        Model Depth 5
    Attributes:
    """


class GeneralContractorAllProperties(
    GeneralContractorInheritedProperties, GeneralContractorProperties, TypedDict
):
    pass


class GeneralContractorBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GeneralContractor", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        GeneralContractorProperties,
        GeneralContractorInheritedProperties,
        GeneralContractorAllProperties,
    ] = GeneralContractorAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GeneralContractor"
    return model


GeneralContractor = create_schema_org_model()


def create_generalcontractor_model(
    model: Union[
        GeneralContractorProperties,
        GeneralContractorInheritedProperties,
        GeneralContractorAllProperties,
    ]
):
    _type = deepcopy(GeneralContractorAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GeneralContractorAllProperties):
    pydantic_type = create_generalcontractor_model(model=model)
    return pydantic_type(model).schema_json()
