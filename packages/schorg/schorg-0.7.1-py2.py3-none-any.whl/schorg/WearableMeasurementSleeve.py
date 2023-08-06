"""
Measurement of the sleeve length, for example of a shirt

https://schema.org/WearableMeasurementSleeve
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementSleeveInheritedProperties(TypedDict):
    """Measurement of the sleeve length, for example of a shirt

    References:
        https://schema.org/WearableMeasurementSleeve
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableMeasurementSleeveProperties(TypedDict):
    """Measurement of the sleeve length, for example of a shirt

    References:
        https://schema.org/WearableMeasurementSleeve
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableMeasurementSleeveInheritedProperties , WearableMeasurementSleeveProperties, TypedDict):
    pass


class WearableMeasurementSleeveBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableMeasurementSleeve",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableMeasurementSleeveProperties, WearableMeasurementSleeveInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementSleeve"
    return model
    

WearableMeasurementSleeve = create_schema_org_model()


def create_wearablemeasurementsleeve_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablemeasurementsleeve_model(model=model)
    return pydantic_type(model).schema_json()


