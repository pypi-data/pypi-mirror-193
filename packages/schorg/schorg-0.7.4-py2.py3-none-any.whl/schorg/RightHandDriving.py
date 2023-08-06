"""
The steering position is on the right side of the vehicle (viewed from the main direction of driving).

https://schema.org/RightHandDriving
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class RightHandDrivingAllProperties(
    RightHandDrivingInheritedProperties, RightHandDrivingProperties, TypedDict
):
    pass


class RightHandDrivingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RightHandDriving", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RightHandDrivingProperties,
        RightHandDrivingInheritedProperties,
        RightHandDrivingAllProperties,
    ] = RightHandDrivingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RightHandDriving"
    return model


RightHandDriving = create_schema_org_model()


def create_righthanddriving_model(
    model: Union[
        RightHandDrivingProperties,
        RightHandDrivingInheritedProperties,
        RightHandDrivingAllProperties,
    ]
):
    _type = deepcopy(RightHandDrivingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of RightHandDrivingAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RightHandDrivingAllProperties):
    pydantic_type = create_righthanddriving_model(model=model)
    return pydantic_type(model).schema_json()
