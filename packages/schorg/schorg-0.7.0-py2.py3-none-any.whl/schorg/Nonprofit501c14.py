"""
Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual Reserve Funds.

https://schema.org/Nonprofit501c14
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c14InheritedProperties(TypedDict):
    """Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual Reserve Funds.

    References:
        https://schema.org/Nonprofit501c14
    Note:
        Model Depth 6
    Attributes:
    """

    


class Nonprofit501c14Properties(TypedDict):
    """Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual Reserve Funds.

    References:
        https://schema.org/Nonprofit501c14
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(Nonprofit501c14InheritedProperties , Nonprofit501c14Properties, TypedDict):
    pass


class Nonprofit501c14BaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Nonprofit501c14",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[Nonprofit501c14Properties, Nonprofit501c14InheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c14"
    return model
    

Nonprofit501c14 = create_schema_org_model()


def create_nonprofit501c14_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nonprofit501c14_model(model=model)
    return pydantic_type(model).schema_json()


