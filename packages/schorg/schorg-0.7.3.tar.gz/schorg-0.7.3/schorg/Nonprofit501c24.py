"""
Nonprofit501c24: Non-profit type referring to Section 4049 ERISA Trusts.

https://schema.org/Nonprofit501c24
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c24InheritedProperties(TypedDict):
    """Nonprofit501c24: Non-profit type referring to Section 4049 ERISA Trusts.

    References:
        https://schema.org/Nonprofit501c24
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c24Properties(TypedDict):
    """Nonprofit501c24: Non-profit type referring to Section 4049 ERISA Trusts.

    References:
        https://schema.org/Nonprofit501c24
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c24AllProperties(
    Nonprofit501c24InheritedProperties, Nonprofit501c24Properties, TypedDict
):
    pass


class Nonprofit501c24BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c24", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c24Properties,
        Nonprofit501c24InheritedProperties,
        Nonprofit501c24AllProperties,
    ] = Nonprofit501c24AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c24"
    return model


Nonprofit501c24 = create_schema_org_model()


def create_nonprofit501c24_model(
    model: Union[
        Nonprofit501c24Properties,
        Nonprofit501c24InheritedProperties,
        Nonprofit501c24AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c24AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501c24AllProperties):
    pydantic_type = create_nonprofit501c24_model(model=model)
    return pydantic_type(model).schema_json()
