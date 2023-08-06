"""
A system of medicine that originated in India over thousands of years and that focuses on integrating and balancing the body, mind, and spirit.

https://schema.org/Ayurvedic
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AyurvedicInheritedProperties(TypedDict):
    """A system of medicine that originated in India over thousands of years and that focuses on integrating and balancing the body, mind, and spirit.

    References:
        https://schema.org/Ayurvedic
    Note:
        Model Depth 6
    Attributes:
    """


class AyurvedicProperties(TypedDict):
    """A system of medicine that originated in India over thousands of years and that focuses on integrating and balancing the body, mind, and spirit.

    References:
        https://schema.org/Ayurvedic
    Note:
        Model Depth 6
    Attributes:
    """


class AyurvedicAllProperties(
    AyurvedicInheritedProperties, AyurvedicProperties, TypedDict
):
    pass


class AyurvedicBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Ayurvedic", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AyurvedicProperties, AyurvedicInheritedProperties, AyurvedicAllProperties
    ] = AyurvedicAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Ayurvedic"
    return model


Ayurvedic = create_schema_org_model()


def create_ayurvedic_model(
    model: Union[
        AyurvedicProperties, AyurvedicInheritedProperties, AyurvedicAllProperties
    ]
):
    _type = deepcopy(AyurvedicAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AyurvedicAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AyurvedicAllProperties):
    pydantic_type = create_ayurvedic_model(model=model)
    return pydantic_type(model).schema_json()
