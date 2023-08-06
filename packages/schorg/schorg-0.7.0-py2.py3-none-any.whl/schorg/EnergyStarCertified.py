"""
Represents EnergyStar certification.

https://schema.org/EnergyStarCertified
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(EnergyStarCertifiedInheritedProperties , EnergyStarCertifiedProperties, TypedDict):
    pass


class EnergyStarCertifiedBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EnergyStarCertified",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EnergyStarCertifiedProperties, EnergyStarCertifiedInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EnergyStarCertified"
    return model
    

EnergyStarCertified = create_schema_org_model()


def create_energystarcertified_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_energystarcertified_model(model=model)
    return pydantic_type(model).schema_json()


