"""
LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that is limited by guarantee (UK).

https://schema.org/LimitedByGuaranteeCharity
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LimitedByGuaranteeCharityInheritedProperties(TypedDict):
    """LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that is limited by guarantee (UK).

    References:
        https://schema.org/LimitedByGuaranteeCharity
    Note:
        Model Depth 6
    Attributes:
    """


class LimitedByGuaranteeCharityProperties(TypedDict):
    """LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that is limited by guarantee (UK).

    References:
        https://schema.org/LimitedByGuaranteeCharity
    Note:
        Model Depth 6
    Attributes:
    """


class LimitedByGuaranteeCharityAllProperties(
    LimitedByGuaranteeCharityInheritedProperties,
    LimitedByGuaranteeCharityProperties,
    TypedDict,
):
    pass


class LimitedByGuaranteeCharityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LimitedByGuaranteeCharity", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LimitedByGuaranteeCharityProperties,
        LimitedByGuaranteeCharityInheritedProperties,
        LimitedByGuaranteeCharityAllProperties,
    ] = LimitedByGuaranteeCharityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LimitedByGuaranteeCharity"
    return model


LimitedByGuaranteeCharity = create_schema_org_model()


def create_limitedbyguaranteecharity_model(
    model: Union[
        LimitedByGuaranteeCharityProperties,
        LimitedByGuaranteeCharityInheritedProperties,
        LimitedByGuaranteeCharityAllProperties,
    ]
):
    _type = deepcopy(LimitedByGuaranteeCharityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of LimitedByGuaranteeCharityAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LimitedByGuaranteeCharityAllProperties):
    pydantic_type = create_limitedbyguaranteecharity_model(model=model)
    return pydantic_type(model).schema_json()
