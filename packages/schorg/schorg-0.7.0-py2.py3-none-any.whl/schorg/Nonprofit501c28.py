"""
Nonprofit501c28: Non-profit type referring to National Railroad Retirement Investment Trusts.

https://schema.org/Nonprofit501c28
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c28InheritedProperties(TypedDict):
    """Nonprofit501c28: Non-profit type referring to National Railroad Retirement Investment Trusts.

    References:
        https://schema.org/Nonprofit501c28
    Note:
        Model Depth 6
    Attributes:
    """

    


class Nonprofit501c28Properties(TypedDict):
    """Nonprofit501c28: Non-profit type referring to National Railroad Retirement Investment Trusts.

    References:
        https://schema.org/Nonprofit501c28
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(Nonprofit501c28InheritedProperties , Nonprofit501c28Properties, TypedDict):
    pass


class Nonprofit501c28BaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Nonprofit501c28",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[Nonprofit501c28Properties, Nonprofit501c28InheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c28"
    return model
    

Nonprofit501c28 = create_schema_org_model()


def create_nonprofit501c28_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nonprofit501c28_model(model=model)
    return pydantic_type(model).schema_json()


