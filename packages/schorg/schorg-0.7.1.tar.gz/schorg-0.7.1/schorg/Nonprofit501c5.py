"""
Nonprofit501c5: Non-profit type referring to Labor, Agricultural and Horticultural Organizations.

https://schema.org/Nonprofit501c5
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c5InheritedProperties(TypedDict):
    """Nonprofit501c5: Non-profit type referring to Labor, Agricultural and Horticultural Organizations.

    References:
        https://schema.org/Nonprofit501c5
    Note:
        Model Depth 6
    Attributes:
    """

    


class Nonprofit501c5Properties(TypedDict):
    """Nonprofit501c5: Non-profit type referring to Labor, Agricultural and Horticultural Organizations.

    References:
        https://schema.org/Nonprofit501c5
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(Nonprofit501c5InheritedProperties , Nonprofit501c5Properties, TypedDict):
    pass


class Nonprofit501c5BaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Nonprofit501c5",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[Nonprofit501c5Properties, Nonprofit501c5InheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c5"
    return model
    

Nonprofit501c5 = create_schema_org_model()


def create_nonprofit501c5_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nonprofit501c5_model(model=model)
    return pydantic_type(model).schema_json()


