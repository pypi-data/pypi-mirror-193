"""
Size group "Womens" for wearables.

https://schema.org/WearableSizeGroupWomens
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupWomensInheritedProperties(TypedDict):
    """Size group "Womens" for wearables.

    References:
        https://schema.org/WearableSizeGroupWomens
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupWomensProperties(TypedDict):
    """Size group "Womens" for wearables.

    References:
        https://schema.org/WearableSizeGroupWomens
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupWomensAllProperties(
    WearableSizeGroupWomensInheritedProperties,
    WearableSizeGroupWomensProperties,
    TypedDict,
):
    pass


class WearableSizeGroupWomensBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupWomens", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupWomensProperties,
        WearableSizeGroupWomensInheritedProperties,
        WearableSizeGroupWomensAllProperties,
    ] = WearableSizeGroupWomensAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupWomens"
    return model


WearableSizeGroupWomens = create_schema_org_model()


def create_wearablesizegroupwomens_model(
    model: Union[
        WearableSizeGroupWomensProperties,
        WearableSizeGroupWomensInheritedProperties,
        WearableSizeGroupWomensAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupWomensAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WearableSizeGroupWomensAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeGroupWomensAllProperties):
    pydantic_type = create_wearablesizegroupwomens_model(model=model)
    return pydantic_type(model).schema_json()
