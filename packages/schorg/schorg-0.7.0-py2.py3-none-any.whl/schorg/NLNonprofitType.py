"""
NLNonprofitType: Non-profit organization type originating from the Netherlands.

https://schema.org/NLNonprofitType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NLNonprofitTypeInheritedProperties(TypedDict):
    """NLNonprofitType: Non-profit organization type originating from the Netherlands.

    References:
        https://schema.org/NLNonprofitType
    Note:
        Model Depth 5
    Attributes:
    """

    


class NLNonprofitTypeProperties(TypedDict):
    """NLNonprofitType: Non-profit organization type originating from the Netherlands.

    References:
        https://schema.org/NLNonprofitType
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(NLNonprofitTypeInheritedProperties , NLNonprofitTypeProperties, TypedDict):
    pass


class NLNonprofitTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="NLNonprofitType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[NLNonprofitTypeProperties, NLNonprofitTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NLNonprofitType"
    return model
    

NLNonprofitType = create_schema_org_model()


def create_nlnonprofittype_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nlnonprofittype_model(model=model)
    return pydantic_type(model).schema_json()


