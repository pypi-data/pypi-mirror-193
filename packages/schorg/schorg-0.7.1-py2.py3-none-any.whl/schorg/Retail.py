"""
The drug's cost represents the retail cost of the drug.

https://schema.org/Retail
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RetailInheritedProperties(TypedDict):
    """The drug's cost represents the retail cost of the drug.

    References:
        https://schema.org/Retail
    Note:
        Model Depth 6
    Attributes:
    """

    


class RetailProperties(TypedDict):
    """The drug's cost represents the retail cost of the drug.

    References:
        https://schema.org/Retail
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(RetailInheritedProperties , RetailProperties, TypedDict):
    pass


class RetailBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Retail",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RetailProperties, RetailInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Retail"
    return model
    

Retail = create_schema_org_model()


def create_retail_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_retail_model(model=model)
    return pydantic_type(model).schema_json()


