"""
The steering position is on the right side of the vehicle (viewed from the main direction of driving).

https://schema.org/RightHandDriving
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RightHandDrivingInheritedProperties(TypedDict):
    """The steering position is on the right side of the vehicle (viewed from the main direction of driving).

    References:
        https://schema.org/RightHandDriving
    Note:
        Model Depth 6
    Attributes:
    """

    


class RightHandDrivingProperties(TypedDict):
    """The steering position is on the right side of the vehicle (viewed from the main direction of driving).

    References:
        https://schema.org/RightHandDriving
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(RightHandDrivingInheritedProperties , RightHandDrivingProperties, TypedDict):
    pass


class RightHandDrivingBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RightHandDriving",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RightHandDrivingProperties, RightHandDrivingInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RightHandDriving"
    return model
    

RightHandDriving = create_schema_org_model()


def create_righthanddriving_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_righthanddriving_model(model=model)
    return pydantic_type(model).schema_json()


