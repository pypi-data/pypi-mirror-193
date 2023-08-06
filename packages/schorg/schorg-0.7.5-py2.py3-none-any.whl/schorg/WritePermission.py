"""
Permission to write or edit the document.

https://schema.org/WritePermission
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WritePermissionInheritedProperties(TypedDict):
    """Permission to write or edit the document.

    References:
        https://schema.org/WritePermission
    Note:
        Model Depth 5
    Attributes:
    """


class WritePermissionProperties(TypedDict):
    """Permission to write or edit the document.

    References:
        https://schema.org/WritePermission
    Note:
        Model Depth 5
    Attributes:
    """


class WritePermissionAllProperties(
    WritePermissionInheritedProperties, WritePermissionProperties, TypedDict
):
    pass


class WritePermissionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WritePermission", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WritePermissionProperties,
        WritePermissionInheritedProperties,
        WritePermissionAllProperties,
    ] = WritePermissionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WritePermission"
    return model


WritePermission = create_schema_org_model()


def create_writepermission_model(
    model: Union[
        WritePermissionProperties,
        WritePermissionInheritedProperties,
        WritePermissionAllProperties,
    ]
):
    _type = deepcopy(WritePermissionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WritePermission. Please see: https://schema.org/WritePermission"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WritePermissionAllProperties):
    pydantic_type = create_writepermission_model(model=model)
    return pydantic_type(model).schema_json()
