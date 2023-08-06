"""
Represents the manufacturer suggested retail price ("MSRP") of an offered product.

https://schema.org/MSRP
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MSRPInheritedProperties(TypedDict):
    """Represents the manufacturer suggested retail price ("MSRP") of an offered product.

    References:
        https://schema.org/MSRP
    Note:
        Model Depth 5
    Attributes:
    """


class MSRPProperties(TypedDict):
    """Represents the manufacturer suggested retail price ("MSRP") of an offered product.

    References:
        https://schema.org/MSRP
    Note:
        Model Depth 5
    Attributes:
    """


class MSRPAllProperties(MSRPInheritedProperties, MSRPProperties, TypedDict):
    pass


class MSRPBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MSRP", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MSRPProperties, MSRPInheritedProperties, MSRPAllProperties
    ] = MSRPAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MSRP"
    return model


MSRP = create_schema_org_model()


def create_msrp_model(
    model: Union[MSRPProperties, MSRPInheritedProperties, MSRPAllProperties]
):
    _type = deepcopy(MSRPAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MSRPAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MSRPAllProperties):
    pydantic_type = create_msrp_model(model=model)
    return pydantic_type(model).schema_json()
