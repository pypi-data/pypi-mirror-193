"""
An enumeration of genders.

https://schema.org/GenderType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GenderTypeInheritedProperties(TypedDict):
    """An enumeration of genders.

    References:
        https://schema.org/GenderType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class GenderTypeProperties(TypedDict):
    """An enumeration of genders.

    References:
        https://schema.org/GenderType
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(GenderTypeInheritedProperties , GenderTypeProperties, TypedDict):
    pass


class GenderTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="GenderType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[GenderTypeProperties, GenderTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GenderType"
    return model
    

GenderType = create_schema_org_model()


def create_gendertype_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_gendertype_model(model=model)
    return pydantic_type(model).schema_json()


