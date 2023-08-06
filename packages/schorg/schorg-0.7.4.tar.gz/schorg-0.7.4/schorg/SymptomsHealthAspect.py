"""
Symptoms or related symptoms of a Topic.

https://schema.org/SymptomsHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SymptomsHealthAspectInheritedProperties(TypedDict):
    """Symptoms or related symptoms of a Topic.

    References:
        https://schema.org/SymptomsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class SymptomsHealthAspectProperties(TypedDict):
    """Symptoms or related symptoms of a Topic.

    References:
        https://schema.org/SymptomsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class SymptomsHealthAspectAllProperties(
    SymptomsHealthAspectInheritedProperties, SymptomsHealthAspectProperties, TypedDict
):
    pass


class SymptomsHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SymptomsHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SymptomsHealthAspectProperties,
        SymptomsHealthAspectInheritedProperties,
        SymptomsHealthAspectAllProperties,
    ] = SymptomsHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SymptomsHealthAspect"
    return model


SymptomsHealthAspect = create_schema_org_model()


def create_symptomshealthaspect_model(
    model: Union[
        SymptomsHealthAspectProperties,
        SymptomsHealthAspectInheritedProperties,
        SymptomsHealthAspectAllProperties,
    ]
):
    _type = deepcopy(SymptomsHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SymptomsHealthAspectAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SymptomsHealthAspectAllProperties):
    pydantic_type = create_symptomshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
