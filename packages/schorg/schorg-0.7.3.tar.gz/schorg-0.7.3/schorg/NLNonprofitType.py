"""
NLNonprofitType: Non-profit organization type originating from the Netherlands.

https://schema.org/NLNonprofitType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NLNonprofitTypeInheritedProperties(TypedDict):
    """NLNonprofitType: Non-profit organization type originating from the Netherlands.

    References:
        https://schema.org/NLNonprofitType
    Note:
        Model Depth 5
    Attributes:
    """


class NLNonprofitTypeProperties(TypedDict):
    """NLNonprofitType: Non-profit organization type originating from the Netherlands.

    References:
        https://schema.org/NLNonprofitType
    Note:
        Model Depth 5
    Attributes:
    """


class NLNonprofitTypeAllProperties(
    NLNonprofitTypeInheritedProperties, NLNonprofitTypeProperties, TypedDict
):
    pass


class NLNonprofitTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NLNonprofitType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NLNonprofitTypeProperties,
        NLNonprofitTypeInheritedProperties,
        NLNonprofitTypeAllProperties,
    ] = NLNonprofitTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NLNonprofitType"
    return model


NLNonprofitType = create_schema_org_model()


def create_nlnonprofittype_model(
    model: Union[
        NLNonprofitTypeProperties,
        NLNonprofitTypeInheritedProperties,
        NLNonprofitTypeAllProperties,
    ]
):
    _type = deepcopy(NLNonprofitTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NLNonprofitTypeAllProperties):
    pydantic_type = create_nlnonprofittype_model(model=model)
    return pydantic_type(model).schema_json()
