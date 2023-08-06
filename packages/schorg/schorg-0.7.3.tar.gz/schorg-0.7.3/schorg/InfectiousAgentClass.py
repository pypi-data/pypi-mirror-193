"""
Classes of agents or pathogens that transmit infectious diseases. Enumerated type.

https://schema.org/InfectiousAgentClass
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InfectiousAgentClassInheritedProperties(TypedDict):
    """Classes of agents or pathogens that transmit infectious diseases. Enumerated type.

    References:
        https://schema.org/InfectiousAgentClass
    Note:
        Model Depth 5
    Attributes:
    """


class InfectiousAgentClassProperties(TypedDict):
    """Classes of agents or pathogens that transmit infectious diseases. Enumerated type.

    References:
        https://schema.org/InfectiousAgentClass
    Note:
        Model Depth 5
    Attributes:
    """


class InfectiousAgentClassAllProperties(
    InfectiousAgentClassInheritedProperties, InfectiousAgentClassProperties, TypedDict
):
    pass


class InfectiousAgentClassBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="InfectiousAgentClass", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        InfectiousAgentClassProperties,
        InfectiousAgentClassInheritedProperties,
        InfectiousAgentClassAllProperties,
    ] = InfectiousAgentClassAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InfectiousAgentClass"
    return model


InfectiousAgentClass = create_schema_org_model()


def create_infectiousagentclass_model(
    model: Union[
        InfectiousAgentClassProperties,
        InfectiousAgentClassInheritedProperties,
        InfectiousAgentClassAllProperties,
    ]
):
    _type = deepcopy(InfectiousAgentClassAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: InfectiousAgentClassAllProperties):
    pydantic_type = create_infectiousagentclass_model(model=model)
    return pydantic_type(model).schema_json()
