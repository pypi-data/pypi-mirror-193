"""
Categorization and other types related to a topic.

https://schema.org/TypesHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TypesHealthAspectInheritedProperties(TypedDict):
    """Categorization and other types related to a topic.

    References:
        https://schema.org/TypesHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class TypesHealthAspectProperties(TypedDict):
    """Categorization and other types related to a topic.

    References:
        https://schema.org/TypesHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class TypesHealthAspectAllProperties(
    TypesHealthAspectInheritedProperties, TypesHealthAspectProperties, TypedDict
):
    pass


class TypesHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TypesHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TypesHealthAspectProperties,
        TypesHealthAspectInheritedProperties,
        TypesHealthAspectAllProperties,
    ] = TypesHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TypesHealthAspect"
    return model


TypesHealthAspect = create_schema_org_model()


def create_typeshealthaspect_model(
    model: Union[
        TypesHealthAspectProperties,
        TypesHealthAspectInheritedProperties,
        TypesHealthAspectAllProperties,
    ]
):
    _type = deepcopy(TypesHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TypesHealthAspect. Please see: https://schema.org/TypesHealthAspect"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TypesHealthAspectAllProperties):
    pydantic_type = create_typeshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
