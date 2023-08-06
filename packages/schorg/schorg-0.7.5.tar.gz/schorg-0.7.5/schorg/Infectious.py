"""
Something in medical science that pertains to infectious diseases, i.e. caused by bacterial, viral, fungal or parasitic infections.

https://schema.org/Infectious
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InfectiousInheritedProperties(TypedDict):
    """Something in medical science that pertains to infectious diseases, i.e. caused by bacterial, viral, fungal or parasitic infections.

    References:
        https://schema.org/Infectious
    Note:
        Model Depth 6
    Attributes:
    """


class InfectiousProperties(TypedDict):
    """Something in medical science that pertains to infectious diseases, i.e. caused by bacterial, viral, fungal or parasitic infections.

    References:
        https://schema.org/Infectious
    Note:
        Model Depth 6
    Attributes:
    """


class InfectiousAllProperties(
    InfectiousInheritedProperties, InfectiousProperties, TypedDict
):
    pass


class InfectiousBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Infectious", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        InfectiousProperties, InfectiousInheritedProperties, InfectiousAllProperties
    ] = InfectiousAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Infectious"
    return model


Infectious = create_schema_org_model()


def create_infectious_model(
    model: Union[
        InfectiousProperties, InfectiousInheritedProperties, InfectiousAllProperties
    ]
):
    _type = deepcopy(InfectiousAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Infectious. Please see: https://schema.org/Infectious"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: InfectiousAllProperties):
    pydantic_type = create_infectious_model(model=model)
    return pydantic_type(model).schema_json()
