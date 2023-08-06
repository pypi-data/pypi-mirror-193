"""
A specific branch of medical science that is concerned with poisons, their nature, effects and detection and involved in the treatment of poisoning.

https://schema.org/Toxicologic
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ToxicologicInheritedProperties(TypedDict):
    """A specific branch of medical science that is concerned with poisons, their nature, effects and detection and involved in the treatment of poisoning.

    References:
        https://schema.org/Toxicologic
    Note:
        Model Depth 6
    Attributes:
    """


class ToxicologicProperties(TypedDict):
    """A specific branch of medical science that is concerned with poisons, their nature, effects and detection and involved in the treatment of poisoning.

    References:
        https://schema.org/Toxicologic
    Note:
        Model Depth 6
    Attributes:
    """


class ToxicologicAllProperties(
    ToxicologicInheritedProperties, ToxicologicProperties, TypedDict
):
    pass


class ToxicologicBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Toxicologic", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ToxicologicProperties, ToxicologicInheritedProperties, ToxicologicAllProperties
    ] = ToxicologicAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Toxicologic"
    return model


Toxicologic = create_schema_org_model()


def create_toxicologic_model(
    model: Union[
        ToxicologicProperties, ToxicologicInheritedProperties, ToxicologicAllProperties
    ]
):
    _type = deepcopy(ToxicologicAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Toxicologic. Please see: https://schema.org/Toxicologic"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ToxicologicAllProperties):
    pydantic_type = create_toxicologic_model(model=model)
    return pydantic_type(model).schema_json()
