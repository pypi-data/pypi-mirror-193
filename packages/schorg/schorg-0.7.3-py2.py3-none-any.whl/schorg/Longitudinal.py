"""
Unlike cross-sectional studies, longitudinal studies track the same people, and therefore the differences observed in those people are less likely to be the result of cultural differences across generations. Longitudinal studies are also used in medicine to uncover predictors of certain diseases.

https://schema.org/Longitudinal
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LongitudinalInheritedProperties(TypedDict):
    """Unlike cross-sectional studies, longitudinal studies track the same people, and therefore the differences observed in those people are less likely to be the result of cultural differences across generations. Longitudinal studies are also used in medicine to uncover predictors of certain diseases.

    References:
        https://schema.org/Longitudinal
    Note:
        Model Depth 6
    Attributes:
    """


class LongitudinalProperties(TypedDict):
    """Unlike cross-sectional studies, longitudinal studies track the same people, and therefore the differences observed in those people are less likely to be the result of cultural differences across generations. Longitudinal studies are also used in medicine to uncover predictors of certain diseases.

    References:
        https://schema.org/Longitudinal
    Note:
        Model Depth 6
    Attributes:
    """


class LongitudinalAllProperties(
    LongitudinalInheritedProperties, LongitudinalProperties, TypedDict
):
    pass


class LongitudinalBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Longitudinal", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LongitudinalProperties,
        LongitudinalInheritedProperties,
        LongitudinalAllProperties,
    ] = LongitudinalAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Longitudinal"
    return model


Longitudinal = create_schema_org_model()


def create_longitudinal_model(
    model: Union[
        LongitudinalProperties,
        LongitudinalInheritedProperties,
        LongitudinalAllProperties,
    ]
):
    _type = deepcopy(LongitudinalAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LongitudinalAllProperties):
    pydantic_type = create_longitudinal_model(model=model)
    return pydantic_type(model).schema_json()
