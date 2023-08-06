"""
A specific branch of medical science that pertains to treating diseases, injuries and deformities by manual and instrumental means.

https://schema.org/Surgical
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SurgicalInheritedProperties(TypedDict):
    """A specific branch of medical science that pertains to treating diseases, injuries and deformities by manual and instrumental means.

    References:
        https://schema.org/Surgical
    Note:
        Model Depth 6
    Attributes:
    """


class SurgicalProperties(TypedDict):
    """A specific branch of medical science that pertains to treating diseases, injuries and deformities by manual and instrumental means.

    References:
        https://schema.org/Surgical
    Note:
        Model Depth 6
    Attributes:
    """


class SurgicalAllProperties(SurgicalInheritedProperties, SurgicalProperties, TypedDict):
    pass


class SurgicalBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Surgical", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SurgicalProperties, SurgicalInheritedProperties, SurgicalAllProperties
    ] = SurgicalAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Surgical"
    return model


Surgical = create_schema_org_model()


def create_surgical_model(
    model: Union[SurgicalProperties, SurgicalInheritedProperties, SurgicalAllProperties]
):
    _type = deepcopy(SurgicalAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SurgicalAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SurgicalAllProperties):
    pydantic_type = create_surgical_model(model=model)
    return pydantic_type(model).schema_json()
