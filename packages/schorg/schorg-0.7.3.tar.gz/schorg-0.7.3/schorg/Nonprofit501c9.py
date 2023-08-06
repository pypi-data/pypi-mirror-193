"""
Nonprofit501c9: Non-profit type referring to Voluntary Employee Beneficiary Associations.

https://schema.org/Nonprofit501c9
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c9InheritedProperties(TypedDict):
    """Nonprofit501c9: Non-profit type referring to Voluntary Employee Beneficiary Associations.

    References:
        https://schema.org/Nonprofit501c9
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c9Properties(TypedDict):
    """Nonprofit501c9: Non-profit type referring to Voluntary Employee Beneficiary Associations.

    References:
        https://schema.org/Nonprofit501c9
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c9AllProperties(
    Nonprofit501c9InheritedProperties, Nonprofit501c9Properties, TypedDict
):
    pass


class Nonprofit501c9BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c9", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c9Properties,
        Nonprofit501c9InheritedProperties,
        Nonprofit501c9AllProperties,
    ] = Nonprofit501c9AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c9"
    return model


Nonprofit501c9 = create_schema_org_model()


def create_nonprofit501c9_model(
    model: Union[
        Nonprofit501c9Properties,
        Nonprofit501c9InheritedProperties,
        Nonprofit501c9AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c9AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501c9AllProperties):
    pydantic_type = create_nonprofit501c9_model(model=model)
    return pydantic_type(model).schema_json()
