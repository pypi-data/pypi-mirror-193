"""
A set of Category Code values.

https://schema.org/CategoryCodeSet
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CategoryCodeSetInheritedProperties(TypedDict):
    """A set of Category Code values.

    References:
        https://schema.org/CategoryCodeSet
    Note:
        Model Depth 4
    Attributes:
        hasDefinedTerm: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A Defined Term contained in this term set.
    """

    hasDefinedTerm: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class CategoryCodeSetProperties(TypedDict):
    """A set of Category Code values.

    References:
        https://schema.org/CategoryCodeSet
    Note:
        Model Depth 4
    Attributes:
        hasCategoryCode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A Category code contained in this code set.
    """

    hasCategoryCode: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class CategoryCodeSetAllProperties(
    CategoryCodeSetInheritedProperties, CategoryCodeSetProperties, TypedDict
):
    pass


class CategoryCodeSetBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CategoryCodeSet", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"hasDefinedTerm": {"exclude": True}}
        fields = {"hasCategoryCode": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        CategoryCodeSetProperties,
        CategoryCodeSetInheritedProperties,
        CategoryCodeSetAllProperties,
    ] = CategoryCodeSetAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CategoryCodeSet"
    return model


CategoryCodeSet = create_schema_org_model()


def create_categorycodeset_model(
    model: Union[
        CategoryCodeSetProperties,
        CategoryCodeSetInheritedProperties,
        CategoryCodeSetAllProperties,
    ]
):
    _type = deepcopy(CategoryCodeSetAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CategoryCodeSetAllProperties):
    pydantic_type = create_categorycodeset_model(model=model)
    return pydantic_type(model).schema_json()
