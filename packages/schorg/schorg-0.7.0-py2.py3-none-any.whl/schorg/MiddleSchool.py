"""
A middle school (typically for children aged around 11-14, although this varies somewhat).

https://schema.org/MiddleSchool
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MiddleSchoolInheritedProperties(TypedDict):
    """A middle school (typically for children aged around 11-14, although this varies somewhat).

    References:
        https://schema.org/MiddleSchool
    Note:
        Model Depth 4
    Attributes:
        alumni: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Alumni of an organization.
    """

    alumni: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class MiddleSchoolProperties(TypedDict):
    """A middle school (typically for children aged around 11-14, although this varies somewhat).

    References:
        https://schema.org/MiddleSchool
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(MiddleSchoolInheritedProperties , MiddleSchoolProperties, TypedDict):
    pass


class MiddleSchoolBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MiddleSchool",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'alumni': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MiddleSchoolProperties, MiddleSchoolInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MiddleSchool"
    return model
    

MiddleSchool = create_schema_org_model()


def create_middleschool_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_middleschool_model(model=model)
    return pydantic_type(model).schema_json()


