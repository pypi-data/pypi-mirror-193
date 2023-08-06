"""
Content about contagion mechanisms and contagiousness information over the topic.

https://schema.org/ContagiousnessHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ContagiousnessHealthAspectInheritedProperties(TypedDict):
    """Content about contagion mechanisms and contagiousness information over the topic.

    References:
        https://schema.org/ContagiousnessHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class ContagiousnessHealthAspectProperties(TypedDict):
    """Content about contagion mechanisms and contagiousness information over the topic.

    References:
        https://schema.org/ContagiousnessHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class ContagiousnessHealthAspectAllProperties(
    ContagiousnessHealthAspectInheritedProperties,
    ContagiousnessHealthAspectProperties,
    TypedDict,
):
    pass


class ContagiousnessHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ContagiousnessHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ContagiousnessHealthAspectProperties,
        ContagiousnessHealthAspectInheritedProperties,
        ContagiousnessHealthAspectAllProperties,
    ] = ContagiousnessHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ContagiousnessHealthAspect"
    return model


ContagiousnessHealthAspect = create_schema_org_model()


def create_contagiousnesshealthaspect_model(
    model: Union[
        ContagiousnessHealthAspectProperties,
        ContagiousnessHealthAspectInheritedProperties,
        ContagiousnessHealthAspectAllProperties,
    ]
):
    _type = deepcopy(ContagiousnessHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ContagiousnessHealthAspectAllProperties):
    pydantic_type = create_contagiousnesshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
