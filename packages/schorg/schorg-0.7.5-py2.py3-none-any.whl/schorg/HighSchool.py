"""
A high school.

https://schema.org/HighSchool
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HighSchoolInheritedProperties(TypedDict):
    """A high school.

    References:
        https://schema.org/HighSchool
    Note:
        Model Depth 4
    Attributes:
        alumni: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Alumni of an organization.
    """

    alumni: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class HighSchoolProperties(TypedDict):
    """A high school.

    References:
        https://schema.org/HighSchool
    Note:
        Model Depth 4
    Attributes:
    """


class HighSchoolAllProperties(
    HighSchoolInheritedProperties, HighSchoolProperties, TypedDict
):
    pass


class HighSchoolBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HighSchool", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"alumni": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        HighSchoolProperties, HighSchoolInheritedProperties, HighSchoolAllProperties
    ] = HighSchoolAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HighSchool"
    return model


HighSchool = create_schema_org_model()


def create_highschool_model(
    model: Union[
        HighSchoolProperties, HighSchoolInheritedProperties, HighSchoolAllProperties
    ]
):
    _type = deepcopy(HighSchoolAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of HighSchool. Please see: https://schema.org/HighSchool"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: HighSchoolAllProperties):
    pydantic_type = create_highschool_model(model=model)
    return pydantic_type(model).schema_json()
