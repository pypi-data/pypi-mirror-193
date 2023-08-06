"""
Nonprofit501c12: Non-profit type referring to Benevolent Life Insurance Associations, Mutual Ditch or Irrigation Companies, Mutual or Cooperative Telephone Companies.

https://schema.org/Nonprofit501c12
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c12InheritedProperties(TypedDict):
    """Nonprofit501c12: Non-profit type referring to Benevolent Life Insurance Associations, Mutual Ditch or Irrigation Companies, Mutual or Cooperative Telephone Companies.

    References:
        https://schema.org/Nonprofit501c12
    Note:
        Model Depth 6
    Attributes:
    """

    


class Nonprofit501c12Properties(TypedDict):
    """Nonprofit501c12: Non-profit type referring to Benevolent Life Insurance Associations, Mutual Ditch or Irrigation Companies, Mutual or Cooperative Telephone Companies.

    References:
        https://schema.org/Nonprofit501c12
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(Nonprofit501c12InheritedProperties , Nonprofit501c12Properties, TypedDict):
    pass


class Nonprofit501c12BaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Nonprofit501c12",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[Nonprofit501c12Properties, Nonprofit501c12InheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c12"
    return model
    

Nonprofit501c12 = create_schema_org_model()


def create_nonprofit501c12_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nonprofit501c12_model(model=model)
    return pydantic_type(model).schema_json()


