"""
Specifies that a product return policy is not provided.

https://schema.org/MerchantReturnUnspecified
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MerchantReturnUnspecifiedInheritedProperties(TypedDict):
    """Specifies that a product return policy is not provided.

    References:
        https://schema.org/MerchantReturnUnspecified
    Note:
        Model Depth 5
    Attributes:
    """

    


class MerchantReturnUnspecifiedProperties(TypedDict):
    """Specifies that a product return policy is not provided.

    References:
        https://schema.org/MerchantReturnUnspecified
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MerchantReturnUnspecifiedInheritedProperties , MerchantReturnUnspecifiedProperties, TypedDict):
    pass


class MerchantReturnUnspecifiedBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MerchantReturnUnspecified",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MerchantReturnUnspecifiedProperties, MerchantReturnUnspecifiedInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MerchantReturnUnspecified"
    return model
    

MerchantReturnUnspecified = create_schema_org_model()


def create_merchantreturnunspecified_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_merchantreturnunspecified_model(model=model)
    return pydantic_type(model).schema_json()


