"""
Nonprofit501c18: Non-profit type referring to Employee Funded Pension Trust (created before 25 June 1959).

https://schema.org/Nonprofit501c18
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c18InheritedProperties(TypedDict):
    """Nonprofit501c18: Non-profit type referring to Employee Funded Pension Trust (created before 25 June 1959).

    References:
        https://schema.org/Nonprofit501c18
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c18Properties(TypedDict):
    """Nonprofit501c18: Non-profit type referring to Employee Funded Pension Trust (created before 25 June 1959).

    References:
        https://schema.org/Nonprofit501c18
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c18AllProperties(
    Nonprofit501c18InheritedProperties, Nonprofit501c18Properties, TypedDict
):
    pass


class Nonprofit501c18BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c18", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c18Properties,
        Nonprofit501c18InheritedProperties,
        Nonprofit501c18AllProperties,
    ] = Nonprofit501c18AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c18"
    return model


Nonprofit501c18 = create_schema_org_model()


def create_nonprofit501c18_model(
    model: Union[
        Nonprofit501c18Properties,
        Nonprofit501c18InheritedProperties,
        Nonprofit501c18AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c18AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501c18AllProperties):
    pydantic_type = create_nonprofit501c18_model(model=model)
    return pydantic_type(model).schema_json()
