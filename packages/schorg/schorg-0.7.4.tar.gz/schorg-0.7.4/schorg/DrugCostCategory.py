"""
Enumerated categories of medical drug costs.

https://schema.org/DrugCostCategory
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DrugCostCategoryInheritedProperties(TypedDict):
    """Enumerated categories of medical drug costs.

    References:
        https://schema.org/DrugCostCategory
    Note:
        Model Depth 5
    Attributes:
    """


class DrugCostCategoryProperties(TypedDict):
    """Enumerated categories of medical drug costs.

    References:
        https://schema.org/DrugCostCategory
    Note:
        Model Depth 5
    Attributes:
    """


class DrugCostCategoryAllProperties(
    DrugCostCategoryInheritedProperties, DrugCostCategoryProperties, TypedDict
):
    pass


class DrugCostCategoryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DrugCostCategory", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DrugCostCategoryProperties,
        DrugCostCategoryInheritedProperties,
        DrugCostCategoryAllProperties,
    ] = DrugCostCategoryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DrugCostCategory"
    return model


DrugCostCategory = create_schema_org_model()


def create_drugcostcategory_model(
    model: Union[
        DrugCostCategoryProperties,
        DrugCostCategoryInheritedProperties,
        DrugCostCategoryAllProperties,
    ]
):
    _type = deepcopy(DrugCostCategoryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DrugCostCategoryAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DrugCostCategoryAllProperties):
    pydantic_type = create_drugcostcategory_model(model=model)
    return pydantic_type(model).schema_json()
