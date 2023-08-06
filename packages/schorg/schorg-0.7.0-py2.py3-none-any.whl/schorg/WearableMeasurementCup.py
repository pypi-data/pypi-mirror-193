"""
Measurement of the cup, for example of a bra

https://schema.org/WearableMeasurementCup
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementCupInheritedProperties(TypedDict):
    """Measurement of the cup, for example of a bra

    References:
        https://schema.org/WearableMeasurementCup
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableMeasurementCupProperties(TypedDict):
    """Measurement of the cup, for example of a bra

    References:
        https://schema.org/WearableMeasurementCup
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableMeasurementCupInheritedProperties , WearableMeasurementCupProperties, TypedDict):
    pass


class WearableMeasurementCupBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableMeasurementCup",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableMeasurementCupProperties, WearableMeasurementCupInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementCup"
    return model
    

WearableMeasurementCup = create_schema_org_model()


def create_wearablemeasurementcup_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablemeasurementcup_model(model=model)
    return pydantic_type(model).schema_json()


