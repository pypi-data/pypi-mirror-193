"""
Imperial size system.

https://schema.org/SizeSystemImperial
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SizeSystemImperialInheritedProperties(TypedDict):
    """Imperial size system.

    References:
        https://schema.org/SizeSystemImperial
    Note:
        Model Depth 5
    Attributes:
    """

    


class SizeSystemImperialProperties(TypedDict):
    """Imperial size system.

    References:
        https://schema.org/SizeSystemImperial
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(SizeSystemImperialInheritedProperties , SizeSystemImperialProperties, TypedDict):
    pass


class SizeSystemImperialBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SizeSystemImperial",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SizeSystemImperialProperties, SizeSystemImperialInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SizeSystemImperial"
    return model
    

SizeSystemImperial = create_schema_org_model()


def create_sizesystemimperial_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_sizesystemimperial_model(model=model)
    return pydantic_type(model).schema_json()


