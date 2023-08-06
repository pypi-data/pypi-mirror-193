"""
An indication for treating an underlying condition, symptom, etc.

https://schema.org/TreatmentIndication
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TreatmentIndicationInheritedProperties(TypedDict):
    """An indication for treating an underlying condition, symptom, etc.

    References:
        https://schema.org/TreatmentIndication
    Note:
        Model Depth 4
    Attributes:
    """


class TreatmentIndicationProperties(TypedDict):
    """An indication for treating an underlying condition, symptom, etc.

    References:
        https://schema.org/TreatmentIndication
    Note:
        Model Depth 4
    Attributes:
    """


class TreatmentIndicationAllProperties(
    TreatmentIndicationInheritedProperties, TreatmentIndicationProperties, TypedDict
):
    pass


class TreatmentIndicationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TreatmentIndication", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TreatmentIndicationProperties,
        TreatmentIndicationInheritedProperties,
        TreatmentIndicationAllProperties,
    ] = TreatmentIndicationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TreatmentIndication"
    return model


TreatmentIndication = create_schema_org_model()


def create_treatmentindication_model(
    model: Union[
        TreatmentIndicationProperties,
        TreatmentIndicationInheritedProperties,
        TreatmentIndicationAllProperties,
    ]
):
    _type = deepcopy(TreatmentIndicationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TreatmentIndication. Please see: https://schema.org/TreatmentIndication"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TreatmentIndicationAllProperties):
    pydantic_type = create_treatmentindication_model(model=model)
    return pydantic_type(model).schema_json()
