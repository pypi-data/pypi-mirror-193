"""
Represents EnergyStar certification.

https://schema.org/EnergyStarCertified
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EnergyStarCertifiedInheritedProperties(TypedDict):
    """Represents EnergyStar certification.

    References:
        https://schema.org/EnergyStarCertified
    Note:
        Model Depth 6
    Attributes:
    """


class EnergyStarCertifiedProperties(TypedDict):
    """Represents EnergyStar certification.

    References:
        https://schema.org/EnergyStarCertified
    Note:
        Model Depth 6
    Attributes:
    """


class EnergyStarCertifiedAllProperties(
    EnergyStarCertifiedInheritedProperties, EnergyStarCertifiedProperties, TypedDict
):
    pass


class EnergyStarCertifiedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EnergyStarCertified", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EnergyStarCertifiedProperties,
        EnergyStarCertifiedInheritedProperties,
        EnergyStarCertifiedAllProperties,
    ] = EnergyStarCertifiedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EnergyStarCertified"
    return model


EnergyStarCertified = create_schema_org_model()


def create_energystarcertified_model(
    model: Union[
        EnergyStarCertifiedProperties,
        EnergyStarCertifiedInheritedProperties,
        EnergyStarCertifiedAllProperties,
    ]
):
    _type = deepcopy(EnergyStarCertifiedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of EnergyStarCertifiedAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EnergyStarCertifiedAllProperties):
    pydantic_type = create_energystarcertified_model(model=model)
    return pydantic_type(model).schema_json()
