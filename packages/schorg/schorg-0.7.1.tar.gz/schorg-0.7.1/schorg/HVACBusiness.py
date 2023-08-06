"""
A business that provides Heating, Ventilation and Air Conditioning services.

https://schema.org/HVACBusiness
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HVACBusinessInheritedProperties(TypedDict):
    """A business that provides Heating, Ventilation and Air Conditioning services.

    References:
        https://schema.org/HVACBusiness
    Note:
        Model Depth 5
    Attributes:
    """

    


class HVACBusinessProperties(TypedDict):
    """A business that provides Heating, Ventilation and Air Conditioning services.

    References:
        https://schema.org/HVACBusiness
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HVACBusinessInheritedProperties , HVACBusinessProperties, TypedDict):
    pass


class HVACBusinessBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HVACBusiness",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HVACBusinessProperties, HVACBusinessInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HVACBusiness"
    return model
    

HVACBusiness = create_schema_org_model()


def create_hvacbusiness_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_hvacbusiness_model(model=model)
    return pydantic_type(model).schema_json()


