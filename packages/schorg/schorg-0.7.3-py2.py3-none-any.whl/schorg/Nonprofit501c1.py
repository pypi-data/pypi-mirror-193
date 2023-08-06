"""
Nonprofit501c1: Non-profit type referring to Corporations Organized Under Act of Congress, including Federal Credit Unions and National Farm Loan Associations.

https://schema.org/Nonprofit501c1
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c1InheritedProperties(TypedDict):
    """Nonprofit501c1: Non-profit type referring to Corporations Organized Under Act of Congress, including Federal Credit Unions and National Farm Loan Associations.

    References:
        https://schema.org/Nonprofit501c1
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c1Properties(TypedDict):
    """Nonprofit501c1: Non-profit type referring to Corporations Organized Under Act of Congress, including Federal Credit Unions and National Farm Loan Associations.

    References:
        https://schema.org/Nonprofit501c1
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c1AllProperties(
    Nonprofit501c1InheritedProperties, Nonprofit501c1Properties, TypedDict
):
    pass


class Nonprofit501c1BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c1", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c1Properties,
        Nonprofit501c1InheritedProperties,
        Nonprofit501c1AllProperties,
    ] = Nonprofit501c1AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c1"
    return model


Nonprofit501c1 = create_schema_org_model()


def create_nonprofit501c1_model(
    model: Union[
        Nonprofit501c1Properties,
        Nonprofit501c1InheritedProperties,
        Nonprofit501c1AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c1AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501c1AllProperties):
    pydantic_type = create_nonprofit501c1_model(model=model)
    return pydantic_type(model).schema_json()
