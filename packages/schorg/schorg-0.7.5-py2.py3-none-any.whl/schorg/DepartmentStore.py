"""
A department store.

https://schema.org/DepartmentStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DepartmentStoreInheritedProperties(TypedDict):
    """A department store.

    References:
        https://schema.org/DepartmentStore
    Note:
        Model Depth 5
    Attributes:
    """


class DepartmentStoreProperties(TypedDict):
    """A department store.

    References:
        https://schema.org/DepartmentStore
    Note:
        Model Depth 5
    Attributes:
    """


class DepartmentStoreAllProperties(
    DepartmentStoreInheritedProperties, DepartmentStoreProperties, TypedDict
):
    pass


class DepartmentStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DepartmentStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DepartmentStoreProperties,
        DepartmentStoreInheritedProperties,
        DepartmentStoreAllProperties,
    ] = DepartmentStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DepartmentStore"
    return model


DepartmentStore = create_schema_org_model()


def create_departmentstore_model(
    model: Union[
        DepartmentStoreProperties,
        DepartmentStoreInheritedProperties,
        DepartmentStoreAllProperties,
    ]
):
    _type = deepcopy(DepartmentStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DepartmentStore. Please see: https://schema.org/DepartmentStore"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DepartmentStoreAllProperties):
    pydantic_type = create_departmentstore_model(model=model)
    return pydantic_type(model).schema_json()
