"""
Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.

https://schema.org/DrugPregnancyCategory
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DrugPregnancyCategoryInheritedProperties(TypedDict):
    """Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.

    References:
        https://schema.org/DrugPregnancyCategory
    Note:
        Model Depth 5
    Attributes:
    """

    


class DrugPregnancyCategoryProperties(TypedDict):
    """Categories that represent an assessment of the risk of fetal injury due to a drug or pharmaceutical used as directed by the mother during pregnancy.

    References:
        https://schema.org/DrugPregnancyCategory
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(DrugPregnancyCategoryInheritedProperties , DrugPregnancyCategoryProperties, TypedDict):
    pass


class DrugPregnancyCategoryBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DrugPregnancyCategory",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DrugPregnancyCategoryProperties, DrugPregnancyCategoryInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DrugPregnancyCategory"
    return model
    

DrugPregnancyCategory = create_schema_org_model()


def create_drugpregnancycategory_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_drugpregnancycategory_model(model=model)
    return pydantic_type(model).schema_json()


