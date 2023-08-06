"""
Nonprofit501c22: Non-profit type referring to Withdrawal Liability Payment Funds.

https://schema.org/Nonprofit501c22
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c22InheritedProperties(TypedDict):
    """Nonprofit501c22: Non-profit type referring to Withdrawal Liability Payment Funds.

    References:
        https://schema.org/Nonprofit501c22
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c22Properties(TypedDict):
    """Nonprofit501c22: Non-profit type referring to Withdrawal Liability Payment Funds.

    References:
        https://schema.org/Nonprofit501c22
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c22AllProperties(
    Nonprofit501c22InheritedProperties, Nonprofit501c22Properties, TypedDict
):
    pass


class Nonprofit501c22BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c22", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c22Properties,
        Nonprofit501c22InheritedProperties,
        Nonprofit501c22AllProperties,
    ] = Nonprofit501c22AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c22"
    return model


Nonprofit501c22 = create_schema_org_model()


def create_nonprofit501c22_model(
    model: Union[
        Nonprofit501c22Properties,
        Nonprofit501c22InheritedProperties,
        Nonprofit501c22AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c22AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501c22AllProperties):
    pydantic_type = create_nonprofit501c22_model(model=model)
    return pydantic_type(model).schema_json()
