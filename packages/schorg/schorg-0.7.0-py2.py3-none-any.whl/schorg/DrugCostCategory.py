"""
Enumerated categories of medical drug costs.

https://schema.org/DrugCostCategory
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(DrugCostCategoryInheritedProperties , DrugCostCategoryProperties, TypedDict):
    pass


class DrugCostCategoryBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DrugCostCategory",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DrugCostCategoryProperties, DrugCostCategoryInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DrugCostCategory"
    return model
    

DrugCostCategory = create_schema_org_model()


def create_drugcostcategory_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_drugcostcategory_model(model=model)
    return pydantic_type(model).schema_json()


