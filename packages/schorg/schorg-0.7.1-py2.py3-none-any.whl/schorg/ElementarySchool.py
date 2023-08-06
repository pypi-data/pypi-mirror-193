"""
An elementary school.

https://schema.org/ElementarySchool
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ElementarySchoolInheritedProperties(TypedDict):
    """An elementary school.

    References:
        https://schema.org/ElementarySchool
    Note:
        Model Depth 4
    Attributes:
        alumni: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Alumni of an organization.
    """

    alumni: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class ElementarySchoolProperties(TypedDict):
    """An elementary school.

    References:
        https://schema.org/ElementarySchool
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(ElementarySchoolInheritedProperties , ElementarySchoolProperties, TypedDict):
    pass


class ElementarySchoolBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ElementarySchool",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'alumni': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ElementarySchoolProperties, ElementarySchoolInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ElementarySchool"
    return model
    

ElementarySchool = create_schema_org_model()


def create_elementaryschool_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_elementaryschool_model(model=model)
    return pydantic_type(model).schema_json()


