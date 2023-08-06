"""
The drug's cost represents the wholesale acquisition cost of the drug.

https://schema.org/Wholesale
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WholesaleInheritedProperties(TypedDict):
    """The drug's cost represents the wholesale acquisition cost of the drug.

    References:
        https://schema.org/Wholesale
    Note:
        Model Depth 6
    Attributes:
    """

    


class WholesaleProperties(TypedDict):
    """The drug's cost represents the wholesale acquisition cost of the drug.

    References:
        https://schema.org/Wholesale
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WholesaleInheritedProperties , WholesaleProperties, TypedDict):
    pass


class WholesaleBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Wholesale",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WholesaleProperties, WholesaleInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Wholesale"
    return model
    

Wholesale = create_schema_org_model()


def create_wholesale_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wholesale_model(model=model)
    return pydantic_type(model).schema_json()


