"""
A specific branch of medical science that is concerned with the ear, nose and throat and their respective disease states.

https://schema.org/Otolaryngologic
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OtolaryngologicInheritedProperties(TypedDict):
    """A specific branch of medical science that is concerned with the ear, nose and throat and their respective disease states.

    References:
        https://schema.org/Otolaryngologic
    Note:
        Model Depth 5
    Attributes:
    """


class OtolaryngologicProperties(TypedDict):
    """A specific branch of medical science that is concerned with the ear, nose and throat and their respective disease states.

    References:
        https://schema.org/Otolaryngologic
    Note:
        Model Depth 5
    Attributes:
    """


class OtolaryngologicAllProperties(
    OtolaryngologicInheritedProperties, OtolaryngologicProperties, TypedDict
):
    pass


class OtolaryngologicBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Otolaryngologic", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OtolaryngologicProperties,
        OtolaryngologicInheritedProperties,
        OtolaryngologicAllProperties,
    ] = OtolaryngologicAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Otolaryngologic"
    return model


Otolaryngologic = create_schema_org_model()


def create_otolaryngologic_model(
    model: Union[
        OtolaryngologicProperties,
        OtolaryngologicInheritedProperties,
        OtolaryngologicAllProperties,
    ]
):
    _type = deepcopy(OtolaryngologicAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OtolaryngologicAllProperties):
    pydantic_type = create_otolaryngologic_model(model=model)
    return pydantic_type(model).schema_json()
