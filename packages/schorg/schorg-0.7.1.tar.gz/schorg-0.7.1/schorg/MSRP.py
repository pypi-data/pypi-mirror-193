"""
Represents the manufacturer suggested retail price ("MSRP") of an offered product.

https://schema.org/MSRP
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MSRPInheritedProperties(TypedDict):
    """Represents the manufacturer suggested retail price ("MSRP") of an offered product.

    References:
        https://schema.org/MSRP
    Note:
        Model Depth 5
    Attributes:
    """

    


class MSRPProperties(TypedDict):
    """Represents the manufacturer suggested retail price ("MSRP") of an offered product.

    References:
        https://schema.org/MSRP
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MSRPInheritedProperties , MSRPProperties, TypedDict):
    pass


class MSRPBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MSRP",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MSRPProperties, MSRPInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MSRP"
    return model
    

MSRP = create_schema_org_model()


def create_msrp_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_msrp_model(model=model)
    return pydantic_type(model).schema_json()


