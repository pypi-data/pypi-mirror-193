"""
A designation by the US FDA signifying that adequate and well-controlled studies have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of risk in later trimesters).

https://schema.org/FDAcategoryA
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FDAcategoryAInheritedProperties(TypedDict):
    """A designation by the US FDA signifying that adequate and well-controlled studies have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of risk in later trimesters).

    References:
        https://schema.org/FDAcategoryA
    Note:
        Model Depth 6
    Attributes:
    """

    


class FDAcategoryAProperties(TypedDict):
    """A designation by the US FDA signifying that adequate and well-controlled studies have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of risk in later trimesters).

    References:
        https://schema.org/FDAcategoryA
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(FDAcategoryAInheritedProperties , FDAcategoryAProperties, TypedDict):
    pass


class FDAcategoryABaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="FDAcategoryA",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[FDAcategoryAProperties, FDAcategoryAInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FDAcategoryA"
    return model
    

FDAcategoryA = create_schema_org_model()


def create_fdacategorya_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_fdacategorya_model(model=model)
    return pydantic_type(model).schema_json()


