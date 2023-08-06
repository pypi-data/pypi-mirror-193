"""
A Category Code.

https://schema.org/CategoryCode
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CategoryCodeInheritedProperties(TypedDict):
    """A Category Code.

    References:
        https://schema.org/CategoryCode
    Note:
        Model Depth 4
    Attributes:
        inDefinedTermSet: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A [[DefinedTermSet]] that contains this term.
        termCode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]]
    """

    inDefinedTermSet: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    termCode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class CategoryCodeProperties(TypedDict):
    """A Category Code.

    References:
        https://schema.org/CategoryCode
    Note:
        Model Depth 4
    Attributes:
        codeValue: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A short textual code that uniquely identifies the value.
        inCodeSet: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A [[CategoryCodeSet]] that contains this category code.
    """

    codeValue: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    inCodeSet: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]


class CategoryCodeAllProperties(
    CategoryCodeInheritedProperties, CategoryCodeProperties, TypedDict
):
    pass


class CategoryCodeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CategoryCode", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"inDefinedTermSet": {"exclude": True}}
        fields = {"termCode": {"exclude": True}}
        fields = {"codeValue": {"exclude": True}}
        fields = {"inCodeSet": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        CategoryCodeProperties,
        CategoryCodeInheritedProperties,
        CategoryCodeAllProperties,
    ] = CategoryCodeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CategoryCode"
    return model


CategoryCode = create_schema_org_model()


def create_categorycode_model(
    model: Union[
        CategoryCodeProperties,
        CategoryCodeInheritedProperties,
        CategoryCodeAllProperties,
    ]
):
    _type = deepcopy(CategoryCodeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of CategoryCode. Please see: https://schema.org/CategoryCode"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CategoryCodeAllProperties):
    pydantic_type = create_categorycode_model(model=model)
    return pydantic_type(model).schema_json()
