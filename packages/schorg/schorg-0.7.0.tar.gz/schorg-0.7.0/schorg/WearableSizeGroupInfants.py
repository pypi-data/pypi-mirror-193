"""
Size group "Infants" for wearables.

https://schema.org/WearableSizeGroupInfants
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(WearableSizeGroupInfantsInheritedProperties , WearableSizeGroupInfantsProperties, TypedDict):
    pass


class WearableSizeGroupInfantsBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeGroupInfants",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeGroupInfantsProperties, WearableSizeGroupInfantsInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupInfants"
    return model
    

WearableSizeGroupInfants = create_schema_org_model()


def create_wearablesizegroupinfants_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizegroupinfants_model(model=model)
    return pydantic_type(model).schema_json()


