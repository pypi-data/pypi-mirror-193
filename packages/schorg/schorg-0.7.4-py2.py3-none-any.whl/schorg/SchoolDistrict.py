"""
A School District is an administrative area for the administration of schools.

https://schema.org/SchoolDistrict
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SchoolDistrictInheritedProperties(TypedDict):
    """A School District is an administrative area for the administration of schools.

    References:
        https://schema.org/SchoolDistrict
    Note:
        Model Depth 4
    Attributes:
    """


class SchoolDistrictProperties(TypedDict):
    """A School District is an administrative area for the administration of schools.

    References:
        https://schema.org/SchoolDistrict
    Note:
        Model Depth 4
    Attributes:
    """


class SchoolDistrictAllProperties(
    SchoolDistrictInheritedProperties, SchoolDistrictProperties, TypedDict
):
    pass


class SchoolDistrictBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SchoolDistrict", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SchoolDistrictProperties,
        SchoolDistrictInheritedProperties,
        SchoolDistrictAllProperties,
    ] = SchoolDistrictAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SchoolDistrict"
    return model


SchoolDistrict = create_schema_org_model()


def create_schooldistrict_model(
    model: Union[
        SchoolDistrictProperties,
        SchoolDistrictInheritedProperties,
        SchoolDistrictAllProperties,
    ]
):
    _type = deepcopy(SchoolDistrictAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SchoolDistrictAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SchoolDistrictAllProperties):
    pydantic_type = create_schooldistrict_model(model=model)
    return pydantic_type(model).schema_json()
