"""
Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.

https://schema.org/Specialty
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SpecialtyInheritedProperties(TypedDict):
    """Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.

    References:
        https://schema.org/Specialty
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class SpecialtyProperties(TypedDict):
    """Any branch of a field in which people typically develop specific expertise, usually after significant study, time, and effort.

    References:
        https://schema.org/Specialty
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(SpecialtyInheritedProperties , SpecialtyProperties, TypedDict):
    pass


class SpecialtyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Specialty",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[SpecialtyProperties, SpecialtyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Specialty"
    return model
    

Specialty = create_schema_org_model()


def create_specialty_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_specialty_model(model=model)
    return pydantic_type(model).schema_json()


