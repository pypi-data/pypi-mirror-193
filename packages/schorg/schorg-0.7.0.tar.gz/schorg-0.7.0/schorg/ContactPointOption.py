"""
Enumerated options related to a ContactPoint.

https://schema.org/ContactPointOption
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ContactPointOptionInheritedProperties(TypedDict):
    """Enumerated options related to a ContactPoint.

    References:
        https://schema.org/ContactPointOption
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class ContactPointOptionProperties(TypedDict):
    """Enumerated options related to a ContactPoint.

    References:
        https://schema.org/ContactPointOption
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(ContactPointOptionInheritedProperties , ContactPointOptionProperties, TypedDict):
    pass


class ContactPointOptionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ContactPointOption",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ContactPointOptionProperties, ContactPointOptionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ContactPointOption"
    return model
    

ContactPointOption = create_schema_org_model()


def create_contactpointoption_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_contactpointoption_model(model=model)
    return pydantic_type(model).schema_json()


