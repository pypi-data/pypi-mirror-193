"""
A preschool.

https://schema.org/Preschool
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PreschoolInheritedProperties(TypedDict):
    """A preschool.

    References:
        https://schema.org/Preschool
    Note:
        Model Depth 4
    Attributes:
        alumni: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Alumni of an organization.
    """

    alumni: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class PreschoolProperties(TypedDict):
    """A preschool.

    References:
        https://schema.org/Preschool
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(PreschoolInheritedProperties , PreschoolProperties, TypedDict):
    pass


class PreschoolBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Preschool",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'alumni': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PreschoolProperties, PreschoolInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Preschool"
    return model
    

Preschool = create_schema_org_model()


def create_preschool_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_preschool_model(model=model)
    return pydantic_type(model).schema_json()


