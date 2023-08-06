"""
A specific branch of medical science that pertains to the study of the respiratory system and its respective disease states.

https://schema.org/Pulmonary
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PulmonaryInheritedProperties(TypedDict):
    """A specific branch of medical science that pertains to the study of the respiratory system and its respective disease states.

    References:
        https://schema.org/Pulmonary
    Note:
        Model Depth 6
    Attributes:
    """


class PulmonaryProperties(TypedDict):
    """A specific branch of medical science that pertains to the study of the respiratory system and its respective disease states.

    References:
        https://schema.org/Pulmonary
    Note:
        Model Depth 6
    Attributes:
    """


class PulmonaryAllProperties(
    PulmonaryInheritedProperties, PulmonaryProperties, TypedDict
):
    pass


class PulmonaryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Pulmonary", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PulmonaryProperties, PulmonaryInheritedProperties, PulmonaryAllProperties
    ] = PulmonaryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Pulmonary"
    return model


Pulmonary = create_schema_org_model()


def create_pulmonary_model(
    model: Union[
        PulmonaryProperties, PulmonaryInheritedProperties, PulmonaryAllProperties
    ]
):
    _type = deepcopy(PulmonaryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Pulmonary. Please see: https://schema.org/Pulmonary"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PulmonaryAllProperties):
    pydantic_type = create_pulmonary_model(model=model)
    return pydantic_type(model).schema_json()
