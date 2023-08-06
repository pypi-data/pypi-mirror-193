"""
A designation by the US FDA signifying that there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.

https://schema.org/FDAcategoryD
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FDAcategoryDInheritedProperties(TypedDict):
    """A designation by the US FDA signifying that there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.

    References:
        https://schema.org/FDAcategoryD
    Note:
        Model Depth 6
    Attributes:
    """

    


class FDAcategoryDProperties(TypedDict):
    """A designation by the US FDA signifying that there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.

    References:
        https://schema.org/FDAcategoryD
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(FDAcategoryDInheritedProperties , FDAcategoryDProperties, TypedDict):
    pass


class FDAcategoryDBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="FDAcategoryD",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[FDAcategoryDProperties, FDAcategoryDInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FDAcategoryD"
    return model
    

FDAcategoryD = create_schema_org_model()


def create_fdacategoryd_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_fdacategoryd_model(model=model)
    return pydantic_type(model).schema_json()


