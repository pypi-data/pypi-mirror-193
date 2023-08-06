"""
A specific branch of medical science that deals with the evaluation and initial treatment of medical conditions caused by trauma or sudden illness.

https://schema.org/Emergency
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EmergencyInheritedProperties(TypedDict):
    """A specific branch of medical science that deals with the evaluation and initial treatment of medical conditions caused by trauma or sudden illness.

    References:
        https://schema.org/Emergency
    Note:
        Model Depth 5
    Attributes:
    """


class EmergencyProperties(TypedDict):
    """A specific branch of medical science that deals with the evaluation and initial treatment of medical conditions caused by trauma or sudden illness.

    References:
        https://schema.org/Emergency
    Note:
        Model Depth 5
    Attributes:
    """


class EmergencyAllProperties(
    EmergencyInheritedProperties, EmergencyProperties, TypedDict
):
    pass


class EmergencyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Emergency", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EmergencyProperties, EmergencyInheritedProperties, EmergencyAllProperties
    ] = EmergencyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Emergency"
    return model


Emergency = create_schema_org_model()


def create_emergency_model(
    model: Union[
        EmergencyProperties, EmergencyInheritedProperties, EmergencyAllProperties
    ]
):
    _type = deepcopy(EmergencyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of EmergencyAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EmergencyAllProperties):
    pydantic_type = create_emergency_model(model=model)
    return pydantic_type(model).schema_json()
