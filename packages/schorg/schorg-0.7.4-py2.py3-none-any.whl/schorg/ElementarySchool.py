"""
An elementary school.

https://schema.org/ElementarySchool
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ElementarySchoolInheritedProperties(TypedDict):
    """An elementary school.

    References:
        https://schema.org/ElementarySchool
    Note:
        Model Depth 4
    Attributes:
        alumni: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Alumni of an organization.
    """

    alumni: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class ElementarySchoolProperties(TypedDict):
    """An elementary school.

    References:
        https://schema.org/ElementarySchool
    Note:
        Model Depth 4
    Attributes:
    """


class ElementarySchoolAllProperties(
    ElementarySchoolInheritedProperties, ElementarySchoolProperties, TypedDict
):
    pass


class ElementarySchoolBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ElementarySchool", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"alumni": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ElementarySchoolProperties,
        ElementarySchoolInheritedProperties,
        ElementarySchoolAllProperties,
    ] = ElementarySchoolAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ElementarySchool"
    return model


ElementarySchool = create_schema_org_model()


def create_elementaryschool_model(
    model: Union[
        ElementarySchoolProperties,
        ElementarySchoolInheritedProperties,
        ElementarySchoolAllProperties,
    ]
):
    _type = deepcopy(ElementarySchoolAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ElementarySchoolAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ElementarySchoolAllProperties):
    pydantic_type = create_elementaryschool_model(model=model)
    return pydantic_type(model).schema_json()
