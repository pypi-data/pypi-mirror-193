"""
Size group "Infants" for wearables.

https://schema.org/WearableSizeGroupInfants
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupInfantsInheritedProperties(TypedDict):
    """Size group "Infants" for wearables.

    References:
        https://schema.org/WearableSizeGroupInfants
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupInfantsProperties(TypedDict):
    """Size group "Infants" for wearables.

    References:
        https://schema.org/WearableSizeGroupInfants
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupInfantsAllProperties(
    WearableSizeGroupInfantsInheritedProperties,
    WearableSizeGroupInfantsProperties,
    TypedDict,
):
    pass


class WearableSizeGroupInfantsBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupInfants", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupInfantsProperties,
        WearableSizeGroupInfantsInheritedProperties,
        WearableSizeGroupInfantsAllProperties,
    ] = WearableSizeGroupInfantsAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupInfants"
    return model


WearableSizeGroupInfants = create_schema_org_model()


def create_wearablesizegroupinfants_model(
    model: Union[
        WearableSizeGroupInfantsProperties,
        WearableSizeGroupInfantsInheritedProperties,
        WearableSizeGroupInfantsAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupInfantsAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableSizeGroupInfants. Please see: https://schema.org/WearableSizeGroupInfants"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WearableSizeGroupInfantsAllProperties):
    pydantic_type = create_wearablesizegroupinfants_model(model=model)
    return pydantic_type(model).schema_json()
