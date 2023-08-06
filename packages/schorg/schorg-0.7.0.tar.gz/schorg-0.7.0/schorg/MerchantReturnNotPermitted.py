"""
Specifies that product returns are not permitted.

https://schema.org/MerchantReturnNotPermitted
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MerchantReturnNotPermittedInheritedProperties(TypedDict):
    """Specifies that product returns are not permitted.

    References:
        https://schema.org/MerchantReturnNotPermitted
    Note:
        Model Depth 5
    Attributes:
    """

    


class MerchantReturnNotPermittedProperties(TypedDict):
    """Specifies that product returns are not permitted.

    References:
        https://schema.org/MerchantReturnNotPermitted
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MerchantReturnNotPermittedInheritedProperties , MerchantReturnNotPermittedProperties, TypedDict):
    pass


class MerchantReturnNotPermittedBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MerchantReturnNotPermitted",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MerchantReturnNotPermittedProperties, MerchantReturnNotPermittedInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MerchantReturnNotPermitted"
    return model
    

MerchantReturnNotPermitted = create_schema_org_model()


def create_merchantreturnnotpermitted_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_merchantreturnnotpermitted_model(model=model)
    return pydantic_type(model).schema_json()


