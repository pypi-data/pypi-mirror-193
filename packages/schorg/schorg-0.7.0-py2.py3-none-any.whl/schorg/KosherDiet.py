"""
A diet conforming to Jewish dietary practices.

https://schema.org/KosherDiet
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class KosherDietInheritedProperties(TypedDict):
    """A diet conforming to Jewish dietary practices.

    References:
        https://schema.org/KosherDiet
    Note:
        Model Depth 5
    Attributes:
    """

    


class KosherDietProperties(TypedDict):
    """A diet conforming to Jewish dietary practices.

    References:
        https://schema.org/KosherDiet
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(KosherDietInheritedProperties , KosherDietProperties, TypedDict):
    pass


class KosherDietBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="KosherDiet",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[KosherDietProperties, KosherDietInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "KosherDiet"
    return model
    

KosherDiet = create_schema_org_model()


def create_kosherdiet_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_kosherdiet_model(model=model)
    return pydantic_type(model).schema_json()


