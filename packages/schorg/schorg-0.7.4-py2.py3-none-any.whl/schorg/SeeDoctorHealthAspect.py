"""
Information about questions that may be asked, when to see a professional, measures before seeing a doctor or content about the first consultation.

https://schema.org/SeeDoctorHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SeeDoctorHealthAspectInheritedProperties(TypedDict):
    """Information about questions that may be asked, when to see a professional, measures before seeing a doctor or content about the first consultation.

    References:
        https://schema.org/SeeDoctorHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class SeeDoctorHealthAspectProperties(TypedDict):
    """Information about questions that may be asked, when to see a professional, measures before seeing a doctor or content about the first consultation.

    References:
        https://schema.org/SeeDoctorHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class SeeDoctorHealthAspectAllProperties(
    SeeDoctorHealthAspectInheritedProperties, SeeDoctorHealthAspectProperties, TypedDict
):
    pass


class SeeDoctorHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SeeDoctorHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SeeDoctorHealthAspectProperties,
        SeeDoctorHealthAspectInheritedProperties,
        SeeDoctorHealthAspectAllProperties,
    ] = SeeDoctorHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SeeDoctorHealthAspect"
    return model


SeeDoctorHealthAspect = create_schema_org_model()


def create_seedoctorhealthaspect_model(
    model: Union[
        SeeDoctorHealthAspectProperties,
        SeeDoctorHealthAspectInheritedProperties,
        SeeDoctorHealthAspectAllProperties,
    ]
):
    _type = deepcopy(SeeDoctorHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SeeDoctorHealthAspectAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SeeDoctorHealthAspectAllProperties):
    pydantic_type = create_seedoctorhealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
