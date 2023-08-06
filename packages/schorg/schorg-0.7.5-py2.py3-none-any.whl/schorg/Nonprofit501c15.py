"""
Nonprofit501c15: Non-profit type referring to Mutual Insurance Companies or Associations.

https://schema.org/Nonprofit501c15
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c15InheritedProperties(TypedDict):
    """Nonprofit501c15: Non-profit type referring to Mutual Insurance Companies or Associations.

    References:
        https://schema.org/Nonprofit501c15
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c15Properties(TypedDict):
    """Nonprofit501c15: Non-profit type referring to Mutual Insurance Companies or Associations.

    References:
        https://schema.org/Nonprofit501c15
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c15AllProperties(
    Nonprofit501c15InheritedProperties, Nonprofit501c15Properties, TypedDict
):
    pass


class Nonprofit501c15BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c15", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c15Properties,
        Nonprofit501c15InheritedProperties,
        Nonprofit501c15AllProperties,
    ] = Nonprofit501c15AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c15"
    return model


Nonprofit501c15 = create_schema_org_model()


def create_nonprofit501c15_model(
    model: Union[
        Nonprofit501c15Properties,
        Nonprofit501c15InheritedProperties,
        Nonprofit501c15AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c15AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Nonprofit501c15. Please see: https://schema.org/Nonprofit501c15"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: Nonprofit501c15AllProperties):
    pydantic_type = create_nonprofit501c15_model(model=model)
    return pydantic_type(model).schema_json()
