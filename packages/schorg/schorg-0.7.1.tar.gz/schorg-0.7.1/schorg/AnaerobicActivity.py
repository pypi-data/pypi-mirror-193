"""
Physical activity that is of high-intensity which utilizes the anaerobic metabolism of the body.

https://schema.org/AnaerobicActivity
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AnaerobicActivityInheritedProperties(TypedDict):
    """Physical activity that is of high-intensity which utilizes the anaerobic metabolism of the body.

    References:
        https://schema.org/AnaerobicActivity
    Note:
        Model Depth 5
    Attributes:
    """

    


class AnaerobicActivityProperties(TypedDict):
    """Physical activity that is of high-intensity which utilizes the anaerobic metabolism of the body.

    References:
        https://schema.org/AnaerobicActivity
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(AnaerobicActivityInheritedProperties , AnaerobicActivityProperties, TypedDict):
    pass


class AnaerobicActivityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AnaerobicActivity",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[AnaerobicActivityProperties, AnaerobicActivityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AnaerobicActivity"
    return model
    

AnaerobicActivity = create_schema_org_model()


def create_anaerobicactivity_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_anaerobicactivity_model(model=model)
    return pydantic_type(model).schema_json()


