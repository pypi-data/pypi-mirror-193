"""
A college, university, or other third-level educational institution.

https://schema.org/CollegeOrUniversity
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CollegeOrUniversityInheritedProperties(TypedDict):
    """A college, university, or other third-level educational institution.

    References:
        https://schema.org/CollegeOrUniversity
    Note:
        Model Depth 4
    Attributes:
        alumni: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Alumni of an organization.
    """

    alumni: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class CollegeOrUniversityProperties(TypedDict):
    """A college, university, or other third-level educational institution.

    References:
        https://schema.org/CollegeOrUniversity
    Note:
        Model Depth 4
    Attributes:
    """


class CollegeOrUniversityAllProperties(
    CollegeOrUniversityInheritedProperties, CollegeOrUniversityProperties, TypedDict
):
    pass


class CollegeOrUniversityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CollegeOrUniversity", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"alumni": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        CollegeOrUniversityProperties,
        CollegeOrUniversityInheritedProperties,
        CollegeOrUniversityAllProperties,
    ] = CollegeOrUniversityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CollegeOrUniversity"
    return model


CollegeOrUniversity = create_schema_org_model()


def create_collegeoruniversity_model(
    model: Union[
        CollegeOrUniversityProperties,
        CollegeOrUniversityInheritedProperties,
        CollegeOrUniversityAllProperties,
    ]
):
    _type = deepcopy(CollegeOrUniversityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of CollegeOrUniversity. Please see: https://schema.org/CollegeOrUniversity"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CollegeOrUniversityAllProperties):
    pydantic_type = create_collegeoruniversity_model(model=model)
    return pydantic_type(model).schema_json()
