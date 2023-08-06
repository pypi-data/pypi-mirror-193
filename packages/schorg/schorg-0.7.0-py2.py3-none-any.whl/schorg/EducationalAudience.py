"""
An EducationalAudience.

https://schema.org/EducationalAudience
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EducationalAudienceInheritedProperties(TypedDict):
    """An EducationalAudience.

    References:
        https://schema.org/EducationalAudience
    Note:
        Model Depth 4
    Attributes:
        audienceType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).
        geographicArea: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The geographic area associated with the audience.
    """

    audienceType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    geographicArea: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class EducationalAudienceProperties(TypedDict):
    """An EducationalAudience.

    References:
        https://schema.org/EducationalAudience
    Note:
        Model Depth 4
    Attributes:
        educationalRole: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An educationalRole of an EducationalAudience.
    """

    educationalRole: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(EducationalAudienceInheritedProperties , EducationalAudienceProperties, TypedDict):
    pass


class EducationalAudienceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EducationalAudience",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'audienceType': {'exclude': True}}
        fields = {'geographicArea': {'exclude': True}}
        fields = {'educationalRole': {'exclude': True}}
        


def create_schema_org_model(type_: Union[EducationalAudienceProperties, EducationalAudienceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EducationalAudience"
    return model
    

EducationalAudience = create_schema_org_model()


def create_educationalaudience_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_educationalaudience_model(model=model)
    return pydantic_type(model).schema_json()


