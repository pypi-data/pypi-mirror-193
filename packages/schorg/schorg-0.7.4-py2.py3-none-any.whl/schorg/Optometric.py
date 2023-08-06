"""
The science or practice of testing visual acuity and prescribing corrective lenses.

https://schema.org/Optometric
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OptometricInheritedProperties(TypedDict):
    """The science or practice of testing visual acuity and prescribing corrective lenses.

    References:
        https://schema.org/Optometric
    Note:
        Model Depth 5
    Attributes:
    """


class OptometricProperties(TypedDict):
    """The science or practice of testing visual acuity and prescribing corrective lenses.

    References:
        https://schema.org/Optometric
    Note:
        Model Depth 5
    Attributes:
    """


class OptometricAllProperties(
    OptometricInheritedProperties, OptometricProperties, TypedDict
):
    pass


class OptometricBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Optometric", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OptometricProperties, OptometricInheritedProperties, OptometricAllProperties
    ] = OptometricAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Optometric"
    return model


Optometric = create_schema_org_model()


def create_optometric_model(
    model: Union[
        OptometricProperties, OptometricInheritedProperties, OptometricAllProperties
    ]
):
    _type = deepcopy(OptometricAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of OptometricAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OptometricAllProperties):
    pydantic_type = create_optometric_model(model=model)
    return pydantic_type(model).schema_json()
