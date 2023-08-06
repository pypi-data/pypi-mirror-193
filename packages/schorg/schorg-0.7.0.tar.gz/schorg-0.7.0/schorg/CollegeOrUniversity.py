"""
A college, university, or other third-level educational institution.

https://schema.org/CollegeOrUniversity
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CollegeOrUniversityInheritedProperties(TypedDict):
    """A college, university, or other third-level educational institution.

    References:
        https://schema.org/CollegeOrUniversity
    Note:
        Model Depth 4
    Attributes:
        alumni: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Alumni of an organization.
    """

    alumni: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class CollegeOrUniversityProperties(TypedDict):
    """A college, university, or other third-level educational institution.

    References:
        https://schema.org/CollegeOrUniversity
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(CollegeOrUniversityInheritedProperties , CollegeOrUniversityProperties, TypedDict):
    pass


class CollegeOrUniversityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CollegeOrUniversity",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'alumni': {'exclude': True}}
        


def create_schema_org_model(type_: Union[CollegeOrUniversityProperties, CollegeOrUniversityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CollegeOrUniversity"
    return model
    

CollegeOrUniversity = create_schema_org_model()


def create_collegeoruniversity_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_collegeoruniversity_model(model=model)
    return pydantic_type(model).schema_json()


