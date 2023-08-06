"""
A store that sells mobile phones and related accessories.

https://schema.org/MobilePhoneStore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MobilePhoneStoreInheritedProperties(TypedDict):
    """A store that sells mobile phones and related accessories.

    References:
        https://schema.org/MobilePhoneStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class MobilePhoneStoreProperties(TypedDict):
    """A store that sells mobile phones and related accessories.

    References:
        https://schema.org/MobilePhoneStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MobilePhoneStoreInheritedProperties , MobilePhoneStoreProperties, TypedDict):
    pass


class MobilePhoneStoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MobilePhoneStore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MobilePhoneStoreProperties, MobilePhoneStoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MobilePhoneStore"
    return model
    

MobilePhoneStore = create_schema_org_model()


def create_mobilephonestore_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_mobilephonestore_model(model=model)
    return pydantic_type(model).schema_json()


