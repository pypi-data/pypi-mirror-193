"""
Specifies that product returns are free of charge for the customer.

https://schema.org/FreeReturn
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FreeReturnInheritedProperties(TypedDict):
    """Specifies that product returns are free of charge for the customer.

    References:
        https://schema.org/FreeReturn
    Note:
        Model Depth 5
    Attributes:
    """


class FreeReturnProperties(TypedDict):
    """Specifies that product returns are free of charge for the customer.

    References:
        https://schema.org/FreeReturn
    Note:
        Model Depth 5
    Attributes:
    """


class FreeReturnAllProperties(
    FreeReturnInheritedProperties, FreeReturnProperties, TypedDict
):
    pass


class FreeReturnBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FreeReturn", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FreeReturnProperties, FreeReturnInheritedProperties, FreeReturnAllProperties
    ] = FreeReturnAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FreeReturn"
    return model


FreeReturn = create_schema_org_model()


def create_freereturn_model(
    model: Union[
        FreeReturnProperties, FreeReturnInheritedProperties, FreeReturnAllProperties
    ]
):
    _type = deepcopy(FreeReturnAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of FreeReturn. Please see: https://schema.org/FreeReturn"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: FreeReturnAllProperties):
    pydantic_type = create_freereturn_model(model=model)
    return pydantic_type(model).schema_json()
