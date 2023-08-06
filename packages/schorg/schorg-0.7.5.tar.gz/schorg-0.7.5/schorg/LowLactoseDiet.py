"""
A diet appropriate for people with lactose intolerance.

https://schema.org/LowLactoseDiet
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LowLactoseDietInheritedProperties(TypedDict):
    """A diet appropriate for people with lactose intolerance.

    References:
        https://schema.org/LowLactoseDiet
    Note:
        Model Depth 5
    Attributes:
    """


class LowLactoseDietProperties(TypedDict):
    """A diet appropriate for people with lactose intolerance.

    References:
        https://schema.org/LowLactoseDiet
    Note:
        Model Depth 5
    Attributes:
    """


class LowLactoseDietAllProperties(
    LowLactoseDietInheritedProperties, LowLactoseDietProperties, TypedDict
):
    pass


class LowLactoseDietBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LowLactoseDiet", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LowLactoseDietProperties,
        LowLactoseDietInheritedProperties,
        LowLactoseDietAllProperties,
    ] = LowLactoseDietAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LowLactoseDiet"
    return model


LowLactoseDiet = create_schema_org_model()


def create_lowlactosediet_model(
    model: Union[
        LowLactoseDietProperties,
        LowLactoseDietInheritedProperties,
        LowLactoseDietAllProperties,
    ]
):
    _type = deepcopy(LowLactoseDietAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of LowLactoseDiet. Please see: https://schema.org/LowLactoseDiet"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: LowLactoseDietAllProperties):
    pydantic_type = create_lowlactosediet_model(model=model)
    return pydantic_type(model).schema_json()
