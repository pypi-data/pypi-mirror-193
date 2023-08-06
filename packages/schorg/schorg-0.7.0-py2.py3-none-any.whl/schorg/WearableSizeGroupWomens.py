"""
Size group "Womens" for wearables.

https://schema.org/WearableSizeGroupWomens
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(WearableSizeGroupWomensInheritedProperties , WearableSizeGroupWomensProperties, TypedDict):
    pass


class WearableSizeGroupWomensBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeGroupWomens",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeGroupWomensProperties, WearableSizeGroupWomensInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupWomens"
    return model
    

WearableSizeGroupWomens = create_schema_org_model()


def create_wearablesizegroupwomens_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizegroupwomens_model(model=model)
    return pydantic_type(model).schema_json()


