"""
Permission to read or view the document.

https://schema.org/ReadPermission
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReadPermissionInheritedProperties(TypedDict):
    """Permission to read or view the document.

    References:
        https://schema.org/ReadPermission
    Note:
        Model Depth 5
    Attributes:
    """


class ReadPermissionProperties(TypedDict):
    """Permission to read or view the document.

    References:
        https://schema.org/ReadPermission
    Note:
        Model Depth 5
    Attributes:
    """


class ReadPermissionAllProperties(
    ReadPermissionInheritedProperties, ReadPermissionProperties, TypedDict
):
    pass


class ReadPermissionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReadPermission", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReadPermissionProperties,
        ReadPermissionInheritedProperties,
        ReadPermissionAllProperties,
    ] = ReadPermissionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReadPermission"
    return model


ReadPermission = create_schema_org_model()


def create_readpermission_model(
    model: Union[
        ReadPermissionProperties,
        ReadPermissionInheritedProperties,
        ReadPermissionAllProperties,
    ]
):
    _type = deepcopy(ReadPermissionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ReadPermission. Please see: https://schema.org/ReadPermission"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ReadPermissionAllProperties):
    pydantic_type = create_readpermission_model(model=model)
    return pydantic_type(model).schema_json()
