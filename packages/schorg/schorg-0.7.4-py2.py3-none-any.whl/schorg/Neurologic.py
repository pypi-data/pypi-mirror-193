"""
A specific branch of medical science that studies the nerves and nervous system and its respective disease states.

https://schema.org/Neurologic
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NeurologicInheritedProperties(TypedDict):
    """A specific branch of medical science that studies the nerves and nervous system and its respective disease states.

    References:
        https://schema.org/Neurologic
    Note:
        Model Depth 6
    Attributes:
    """


class NeurologicProperties(TypedDict):
    """A specific branch of medical science that studies the nerves and nervous system and its respective disease states.

    References:
        https://schema.org/Neurologic
    Note:
        Model Depth 6
    Attributes:
    """


class NeurologicAllProperties(
    NeurologicInheritedProperties, NeurologicProperties, TypedDict
):
    pass


class NeurologicBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Neurologic", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NeurologicProperties, NeurologicInheritedProperties, NeurologicAllProperties
    ] = NeurologicAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Neurologic"
    return model


Neurologic = create_schema_org_model()


def create_neurologic_model(
    model: Union[
        NeurologicProperties, NeurologicInheritedProperties, NeurologicAllProperties
    ]
):
    _type = deepcopy(NeurologicAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of NeurologicAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NeurologicAllProperties):
    pydantic_type = create_neurologic_model(model=model)
    return pydantic_type(model).schema_json()
