"""
NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution (NL).

https://schema.org/NonprofitSBBI
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NonprofitSBBIInheritedProperties(TypedDict):
    """NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution (NL).

    References:
        https://schema.org/NonprofitSBBI
    Note:
        Model Depth 6
    Attributes:
    """

    


class NonprofitSBBIProperties(TypedDict):
    """NonprofitSBBI: Non-profit type referring to a Social Interest Promoting Institution (NL).

    References:
        https://schema.org/NonprofitSBBI
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(NonprofitSBBIInheritedProperties , NonprofitSBBIProperties, TypedDict):
    pass


class NonprofitSBBIBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="NonprofitSBBI",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[NonprofitSBBIProperties, NonprofitSBBIInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NonprofitSBBI"
    return model
    

NonprofitSBBI = create_schema_org_model()


def create_nonprofitsbbi_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nonprofitsbbi_model(model=model)
    return pydantic_type(model).schema_json()


