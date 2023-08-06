"""
Game server status: OfflineTemporarily. Server is offline now but it can be online soon.

https://schema.org/OfflineTemporarily
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OfflineTemporarilyInheritedProperties(TypedDict):
    """Game server status: OfflineTemporarily. Server is offline now but it can be online soon.

    References:
        https://schema.org/OfflineTemporarily
    Note:
        Model Depth 6
    Attributes:
    """


class OfflineTemporarilyProperties(TypedDict):
    """Game server status: OfflineTemporarily. Server is offline now but it can be online soon.

    References:
        https://schema.org/OfflineTemporarily
    Note:
        Model Depth 6
    Attributes:
    """


class OfflineTemporarilyAllProperties(
    OfflineTemporarilyInheritedProperties, OfflineTemporarilyProperties, TypedDict
):
    pass


class OfflineTemporarilyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OfflineTemporarily", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OfflineTemporarilyProperties,
        OfflineTemporarilyInheritedProperties,
        OfflineTemporarilyAllProperties,
    ] = OfflineTemporarilyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OfflineTemporarily"
    return model


OfflineTemporarily = create_schema_org_model()


def create_offlinetemporarily_model(
    model: Union[
        OfflineTemporarilyProperties,
        OfflineTemporarilyInheritedProperties,
        OfflineTemporarilyAllProperties,
    ]
):
    _type = deepcopy(OfflineTemporarilyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of OfflineTemporarily. Please see: https://schema.org/OfflineTemporarily"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: OfflineTemporarilyAllProperties):
    pydantic_type = create_offlinetemporarily_model(model=model)
    return pydantic_type(model).schema_json()
