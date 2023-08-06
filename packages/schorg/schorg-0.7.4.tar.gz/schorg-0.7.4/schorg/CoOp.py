"""
Play mode: CoOp. Co-operative games, where you play on the same team with friends.

https://schema.org/CoOp
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CoOpInheritedProperties(TypedDict):
    """Play mode: CoOp. Co-operative games, where you play on the same team with friends.

    References:
        https://schema.org/CoOp
    Note:
        Model Depth 5
    Attributes:
    """


class CoOpProperties(TypedDict):
    """Play mode: CoOp. Co-operative games, where you play on the same team with friends.

    References:
        https://schema.org/CoOp
    Note:
        Model Depth 5
    Attributes:
    """


class CoOpAllProperties(CoOpInheritedProperties, CoOpProperties, TypedDict):
    pass


class CoOpBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CoOp", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CoOpProperties, CoOpInheritedProperties, CoOpAllProperties
    ] = CoOpAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CoOp"
    return model


CoOp = create_schema_org_model()


def create_coop_model(
    model: Union[CoOpProperties, CoOpInheritedProperties, CoOpAllProperties]
):
    _type = deepcopy(CoOpAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of CoOpAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CoOpAllProperties):
    pydantic_type = create_coop_model(model=model)
    return pydantic_type(model).schema_json()
