"""
Researchers.

https://schema.org/Researcher
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ResearcherInheritedProperties(TypedDict):
    """Researchers.

    References:
        https://schema.org/Researcher
    Note:
        Model Depth 4
    Attributes:
        audienceType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).
        geographicArea: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The geographic area associated with the audience.
    """

    audienceType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    geographicArea: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class ResearcherProperties(TypedDict):
    """Researchers.

    References:
        https://schema.org/Researcher
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(ResearcherInheritedProperties , ResearcherProperties, TypedDict):
    pass


class ResearcherBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Researcher",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'audienceType': {'exclude': True}}
        fields = {'geographicArea': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ResearcherProperties, ResearcherInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Researcher"
    return model
    

Researcher = create_schema_org_model()


def create_researcher_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_researcher_model(model=model)
    return pydantic_type(model).schema_json()


