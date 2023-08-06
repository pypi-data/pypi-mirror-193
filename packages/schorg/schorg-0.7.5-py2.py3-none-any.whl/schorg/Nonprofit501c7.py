"""
Nonprofit501c7: Non-profit type referring to Social and Recreational Clubs.

https://schema.org/Nonprofit501c7
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c7InheritedProperties(TypedDict):
    """Nonprofit501c7: Non-profit type referring to Social and Recreational Clubs.

    References:
        https://schema.org/Nonprofit501c7
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c7Properties(TypedDict):
    """Nonprofit501c7: Non-profit type referring to Social and Recreational Clubs.

    References:
        https://schema.org/Nonprofit501c7
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c7AllProperties(
    Nonprofit501c7InheritedProperties, Nonprofit501c7Properties, TypedDict
):
    pass


class Nonprofit501c7BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c7", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c7Properties,
        Nonprofit501c7InheritedProperties,
        Nonprofit501c7AllProperties,
    ] = Nonprofit501c7AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c7"
    return model


Nonprofit501c7 = create_schema_org_model()


def create_nonprofit501c7_model(
    model: Union[
        Nonprofit501c7Properties,
        Nonprofit501c7InheritedProperties,
        Nonprofit501c7AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c7AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Nonprofit501c7. Please see: https://schema.org/Nonprofit501c7"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: Nonprofit501c7AllProperties):
    pydantic_type = create_nonprofit501c7_model(model=model)
    return pydantic_type(model).schema_json()
