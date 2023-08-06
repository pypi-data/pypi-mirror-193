"""
Nonprofit501c12: Non-profit type referring to Benevolent Life Insurance Associations, Mutual Ditch or Irrigation Companies, Mutual or Cooperative Telephone Companies.

https://schema.org/Nonprofit501c12
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class Nonprofit501c12AllProperties(
    Nonprofit501c12InheritedProperties, Nonprofit501c12Properties, TypedDict
):
    pass


class Nonprofit501c12BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c12", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c12Properties,
        Nonprofit501c12InheritedProperties,
        Nonprofit501c12AllProperties,
    ] = Nonprofit501c12AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c12"
    return model


Nonprofit501c12 = create_schema_org_model()


def create_nonprofit501c12_model(
    model: Union[
        Nonprofit501c12Properties,
        Nonprofit501c12InheritedProperties,
        Nonprofit501c12AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c12AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Nonprofit501c12. Please see: https://schema.org/Nonprofit501c12"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: Nonprofit501c12AllProperties):
    pydantic_type = create_nonprofit501c12_model(model=model)
    return pydantic_type(model).schema_json()
