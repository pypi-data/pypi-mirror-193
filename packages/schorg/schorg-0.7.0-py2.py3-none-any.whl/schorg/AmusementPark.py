"""
An amusement park.

https://schema.org/AmusementPark
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AmusementParkInheritedProperties(TypedDict):
    """An amusement park.

    References:
        https://schema.org/AmusementPark
    Note:
        Model Depth 5
    Attributes:
    """

    


class AmusementParkProperties(TypedDict):
    """An amusement park.

    References:
        https://schema.org/AmusementPark
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(AmusementParkInheritedProperties , AmusementParkProperties, TypedDict):
    pass


class AmusementParkBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AmusementPark",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[AmusementParkProperties, AmusementParkInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AmusementPark"
    return model
    

AmusementPark = create_schema_org_model()


def create_amusementpark_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_amusementpark_model(model=model)
    return pydantic_type(model).schema_json()


