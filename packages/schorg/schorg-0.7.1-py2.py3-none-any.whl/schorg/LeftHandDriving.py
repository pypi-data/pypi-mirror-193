"""
The steering position is on the left side of the vehicle (viewed from the main direction of driving).

https://schema.org/LeftHandDriving
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LeftHandDrivingInheritedProperties(TypedDict):
    """The steering position is on the left side of the vehicle (viewed from the main direction of driving).

    References:
        https://schema.org/LeftHandDriving
    Note:
        Model Depth 6
    Attributes:
    """

    


class LeftHandDrivingProperties(TypedDict):
    """The steering position is on the left side of the vehicle (viewed from the main direction of driving).

    References:
        https://schema.org/LeftHandDriving
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(LeftHandDrivingInheritedProperties , LeftHandDrivingProperties, TypedDict):
    pass


class LeftHandDrivingBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LeftHandDriving",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[LeftHandDrivingProperties, LeftHandDrivingInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LeftHandDriving"
    return model
    

LeftHandDriving = create_schema_org_model()


def create_lefthanddriving_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_lefthanddriving_model(model=model)
    return pydantic_type(model).schema_json()


