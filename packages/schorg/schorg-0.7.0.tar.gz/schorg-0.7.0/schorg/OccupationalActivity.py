"""
Any physical activity engaged in for job-related purposes. Examples may include waiting tables, maid service, carrying a mailbag, picking fruits or vegetables, construction work, etc.

https://schema.org/OccupationalActivity
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OccupationalActivityInheritedProperties(TypedDict):
    """Any physical activity engaged in for job-related purposes. Examples may include waiting tables, maid service, carrying a mailbag, picking fruits or vegetables, construction work, etc.

    References:
        https://schema.org/OccupationalActivity
    Note:
        Model Depth 5
    Attributes:
    """

    


class OccupationalActivityProperties(TypedDict):
    """Any physical activity engaged in for job-related purposes. Examples may include waiting tables, maid service, carrying a mailbag, picking fruits or vegetables, construction work, etc.

    References:
        https://schema.org/OccupationalActivity
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(OccupationalActivityInheritedProperties , OccupationalActivityProperties, TypedDict):
    pass


class OccupationalActivityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OccupationalActivity",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OccupationalActivityProperties, OccupationalActivityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OccupationalActivity"
    return model
    

OccupationalActivity = create_schema_org_model()


def create_occupationalactivity_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_occupationalactivity_model(model=model)
    return pydantic_type(model).schema_json()


