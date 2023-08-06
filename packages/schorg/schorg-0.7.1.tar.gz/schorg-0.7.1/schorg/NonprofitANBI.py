"""
NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL).

https://schema.org/NonprofitANBI
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NonprofitANBIInheritedProperties(TypedDict):
    """NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL).

    References:
        https://schema.org/NonprofitANBI
    Note:
        Model Depth 6
    Attributes:
    """

    


class NonprofitANBIProperties(TypedDict):
    """NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL).

    References:
        https://schema.org/NonprofitANBI
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(NonprofitANBIInheritedProperties , NonprofitANBIProperties, TypedDict):
    pass


class NonprofitANBIBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="NonprofitANBI",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[NonprofitANBIProperties, NonprofitANBIInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NonprofitANBI"
    return model
    

NonprofitANBI = create_schema_org_model()


def create_nonprofitanbi_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nonprofitanbi_model(model=model)
    return pydantic_type(model).schema_json()


