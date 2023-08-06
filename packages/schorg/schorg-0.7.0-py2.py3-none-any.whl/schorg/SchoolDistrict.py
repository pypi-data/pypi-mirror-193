"""
A School District is an administrative area for the administration of schools.

https://schema.org/SchoolDistrict
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(SchoolDistrictInheritedProperties , SchoolDistrictProperties, TypedDict):
    pass


class SchoolDistrictBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SchoolDistrict",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SchoolDistrictProperties, SchoolDistrictInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SchoolDistrict"
    return model
    

SchoolDistrict = create_schema_org_model()


def create_schooldistrict_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_schooldistrict_model(model=model)
    return pydantic_type(model).schema_json()


