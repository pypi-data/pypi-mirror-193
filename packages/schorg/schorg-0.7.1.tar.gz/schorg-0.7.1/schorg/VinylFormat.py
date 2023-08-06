"""
VinylFormat.

https://schema.org/VinylFormat
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VinylFormatInheritedProperties(TypedDict):
    """VinylFormat.

    References:
        https://schema.org/VinylFormat
    Note:
        Model Depth 5
    Attributes:
    """

    


class VinylFormatProperties(TypedDict):
    """VinylFormat.

    References:
        https://schema.org/VinylFormat
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(VinylFormatInheritedProperties , VinylFormatProperties, TypedDict):
    pass


class VinylFormatBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="VinylFormat",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[VinylFormatProperties, VinylFormatInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VinylFormat"
    return model
    

VinylFormat = create_schema_org_model()


def create_vinylformat_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_vinylformat_model(model=model)
    return pydantic_type(model).schema_json()


