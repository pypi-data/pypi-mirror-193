"""
Nonprofit501d: Non-profit type referring to Religious and Apostolic Associations.

https://schema.org/Nonprofit501d
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501dInheritedProperties(TypedDict):
    """Nonprofit501d: Non-profit type referring to Religious and Apostolic Associations.

    References:
        https://schema.org/Nonprofit501d
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501dProperties(TypedDict):
    """Nonprofit501d: Non-profit type referring to Religious and Apostolic Associations.

    References:
        https://schema.org/Nonprofit501d
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501dAllProperties(
    Nonprofit501dInheritedProperties, Nonprofit501dProperties, TypedDict
):
    pass


class Nonprofit501dBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501d", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501dProperties,
        Nonprofit501dInheritedProperties,
        Nonprofit501dAllProperties,
    ] = Nonprofit501dAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501d"
    return model


Nonprofit501d = create_schema_org_model()


def create_nonprofit501d_model(
    model: Union[
        Nonprofit501dProperties,
        Nonprofit501dInheritedProperties,
        Nonprofit501dAllProperties,
    ]
):
    _type = deepcopy(Nonprofit501dAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of Nonprofit501dAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: Nonprofit501dAllProperties):
    pydantic_type = create_nonprofit501d_model(model=model)
    return pydantic_type(model).schema_json()
