"""
A designation by the US FDA signifying that animal reproduction studies have failed to demonstrate a risk to the fetus and there are no adequate and well-controlled studies in pregnant women.

https://schema.org/FDAcategoryB
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FDAcategoryBInheritedProperties(TypedDict):
    """A designation by the US FDA signifying that animal reproduction studies have failed to demonstrate a risk to the fetus and there are no adequate and well-controlled studies in pregnant women.

    References:
        https://schema.org/FDAcategoryB
    Note:
        Model Depth 6
    Attributes:
    """

    


class FDAcategoryBProperties(TypedDict):
    """A designation by the US FDA signifying that animal reproduction studies have failed to demonstrate a risk to the fetus and there are no adequate and well-controlled studies in pregnant women.

    References:
        https://schema.org/FDAcategoryB
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(FDAcategoryBInheritedProperties , FDAcategoryBProperties, TypedDict):
    pass


class FDAcategoryBBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="FDAcategoryB",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[FDAcategoryBProperties, FDAcategoryBInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FDAcategoryB"
    return model
    

FDAcategoryB = create_schema_org_model()


def create_fdacategoryb_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_fdacategoryb_model(model=model)
    return pydantic_type(model).schema_json()


