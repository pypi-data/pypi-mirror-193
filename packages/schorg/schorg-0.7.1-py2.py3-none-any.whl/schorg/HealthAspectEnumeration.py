"""
HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].

https://schema.org/HealthAspectEnumeration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HealthAspectEnumerationInheritedProperties(TypedDict):
    """HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].

    References:
        https://schema.org/HealthAspectEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class HealthAspectEnumerationProperties(TypedDict):
    """HealthAspectEnumeration enumerates several aspects of health content online, each of which might be described using [[hasHealthAspect]] and [[HealthTopicContent]].

    References:
        https://schema.org/HealthAspectEnumeration
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(HealthAspectEnumerationInheritedProperties , HealthAspectEnumerationProperties, TypedDict):
    pass


class HealthAspectEnumerationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HealthAspectEnumeration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[HealthAspectEnumerationProperties, HealthAspectEnumerationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HealthAspectEnumeration"
    return model
    

HealthAspectEnumeration = create_schema_org_model()


def create_healthaspectenumeration_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_healthaspectenumeration_model(model=model)
    return pydantic_type(model).schema_json()


