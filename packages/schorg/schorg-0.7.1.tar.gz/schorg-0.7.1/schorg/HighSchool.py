"""
A high school.

https://schema.org/HighSchool
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(HighSchoolInheritedProperties , HighSchoolProperties, TypedDict):
    pass


class HighSchoolBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HighSchool",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'alumni': {'exclude': True}}
        


def create_schema_org_model(type_: Union[HighSchoolProperties, HighSchoolInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HighSchool"
    return model
    

HighSchool = create_schema_org_model()


def create_highschool_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_highschool_model(model=model)
    return pydantic_type(model).schema_json()


