"""
The medical care by a physician, or other health-care professional, who is the patient's first contact with the health-care system and who may recommend a specialist if necessary.

https://schema.org/PrimaryCare
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PrimaryCareInheritedProperties(TypedDict):
    """The medical care by a physician, or other health-care professional, who is the patient's first contact with the health-care system and who may recommend a specialist if necessary.

    References:
        https://schema.org/PrimaryCare
    Note:
        Model Depth 5
    Attributes:
    """


class PrimaryCareProperties(TypedDict):
    """The medical care by a physician, or other health-care professional, who is the patient's first contact with the health-care system and who may recommend a specialist if necessary.

    References:
        https://schema.org/PrimaryCare
    Note:
        Model Depth 5
    Attributes:
    """


class PrimaryCareAllProperties(
    PrimaryCareInheritedProperties, PrimaryCareProperties, TypedDict
):
    pass


class PrimaryCareBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PrimaryCare", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PrimaryCareProperties, PrimaryCareInheritedProperties, PrimaryCareAllProperties
    ] = PrimaryCareAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PrimaryCare"
    return model


PrimaryCare = create_schema_org_model()


def create_primarycare_model(
    model: Union[
        PrimaryCareProperties, PrimaryCareInheritedProperties, PrimaryCareAllProperties
    ]
):
    _type = deepcopy(PrimaryCareAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PrimaryCareAllProperties):
    pydantic_type = create_primarycare_model(model=model)
    return pydantic_type(model).schema_json()
