"""
Nonprofit501c17: Non-profit type referring to Supplemental Unemployment Benefit Trusts.

https://schema.org/Nonprofit501c17
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c17InheritedProperties(TypedDict):
    """Nonprofit501c17: Non-profit type referring to Supplemental Unemployment Benefit Trusts.

    References:
        https://schema.org/Nonprofit501c17
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c17Properties(TypedDict):
    """Nonprofit501c17: Non-profit type referring to Supplemental Unemployment Benefit Trusts.

    References:
        https://schema.org/Nonprofit501c17
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c17AllProperties(
    Nonprofit501c17InheritedProperties, Nonprofit501c17Properties, TypedDict
):
    pass


class Nonprofit501c17BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c17", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c17Properties,
        Nonprofit501c17InheritedProperties,
        Nonprofit501c17AllProperties,
    ] = Nonprofit501c17AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c17"
    return model


Nonprofit501c17 = create_schema_org_model()


def create_nonprofit501c17_model(
    model: Union[
        Nonprofit501c17Properties,
        Nonprofit501c17InheritedProperties,
        Nonprofit501c17AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c17AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501c17AllProperties):
    pydantic_type = create_nonprofit501c17_model(model=model)
    return pydantic_type(model).schema_json()
