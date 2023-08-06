"""
Size group "Petite" for wearables.

https://schema.org/WearableSizeGroupPetite
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(WearableSizeGroupPetiteInheritedProperties , WearableSizeGroupPetiteProperties, TypedDict):
    pass


class WearableSizeGroupPetiteBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeGroupPetite",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeGroupPetiteProperties, WearableSizeGroupPetiteInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupPetite"
    return model
    

WearableSizeGroupPetite = create_schema_org_model()


def create_wearablesizegrouppetite_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizegrouppetite_model(model=model)
    return pydantic_type(model).schema_json()


