"""
Treatments or related therapies for a Topic.

https://schema.org/TreatmentsHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TreatmentsHealthAspectInheritedProperties(TypedDict):
    """Treatments or related therapies for a Topic.

    References:
        https://schema.org/TreatmentsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class TreatmentsHealthAspectProperties(TypedDict):
    """Treatments or related therapies for a Topic.

    References:
        https://schema.org/TreatmentsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class TreatmentsHealthAspectAllProperties(
    TreatmentsHealthAspectInheritedProperties,
    TreatmentsHealthAspectProperties,
    TypedDict,
):
    pass


class TreatmentsHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TreatmentsHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TreatmentsHealthAspectProperties,
        TreatmentsHealthAspectInheritedProperties,
        TreatmentsHealthAspectAllProperties,
    ] = TreatmentsHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TreatmentsHealthAspect"
    return model


TreatmentsHealthAspect = create_schema_org_model()


def create_treatmentshealthaspect_model(
    model: Union[
        TreatmentsHealthAspectProperties,
        TreatmentsHealthAspectInheritedProperties,
        TreatmentsHealthAspectAllProperties,
    ]
):
    _type = deepcopy(TreatmentsHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TreatmentsHealthAspect. Please see: https://schema.org/TreatmentsHealthAspect"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TreatmentsHealthAspectAllProperties):
    pydantic_type = create_treatmentshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
