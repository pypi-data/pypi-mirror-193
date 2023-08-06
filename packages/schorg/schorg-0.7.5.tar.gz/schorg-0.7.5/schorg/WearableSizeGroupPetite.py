"""
Size group "Petite" for wearables.

https://schema.org/WearableSizeGroupPetite
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupPetiteInheritedProperties(TypedDict):
    """Size group "Petite" for wearables.

    References:
        https://schema.org/WearableSizeGroupPetite
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupPetiteProperties(TypedDict):
    """Size group "Petite" for wearables.

    References:
        https://schema.org/WearableSizeGroupPetite
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupPetiteAllProperties(
    WearableSizeGroupPetiteInheritedProperties,
    WearableSizeGroupPetiteProperties,
    TypedDict,
):
    pass


class WearableSizeGroupPetiteBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupPetite", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupPetiteProperties,
        WearableSizeGroupPetiteInheritedProperties,
        WearableSizeGroupPetiteAllProperties,
    ] = WearableSizeGroupPetiteAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupPetite"
    return model


WearableSizeGroupPetite = create_schema_org_model()


def create_wearablesizegrouppetite_model(
    model: Union[
        WearableSizeGroupPetiteProperties,
        WearableSizeGroupPetiteInheritedProperties,
        WearableSizeGroupPetiteAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupPetiteAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableSizeGroupPetite. Please see: https://schema.org/WearableSizeGroupPetite"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WearableSizeGroupPetiteAllProperties):
    pydantic_type = create_wearablesizegrouppetite_model(model=model)
    return pydantic_type(model).schema_json()
