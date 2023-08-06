"""
LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that is limited by guarantee (UK).

https://schema.org/LimitedByGuaranteeCharity
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LimitedByGuaranteeCharityInheritedProperties(TypedDict):
    """LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that is limited by guarantee (UK).

    References:
        https://schema.org/LimitedByGuaranteeCharity
    Note:
        Model Depth 6
    Attributes:
    """

    


class LimitedByGuaranteeCharityProperties(TypedDict):
    """LimitedByGuaranteeCharity: Non-profit type referring to a charitable company that is limited by guarantee (UK).

    References:
        https://schema.org/LimitedByGuaranteeCharity
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(LimitedByGuaranteeCharityInheritedProperties , LimitedByGuaranteeCharityProperties, TypedDict):
    pass


class LimitedByGuaranteeCharityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LimitedByGuaranteeCharity",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[LimitedByGuaranteeCharityProperties, LimitedByGuaranteeCharityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LimitedByGuaranteeCharity"
    return model
    

LimitedByGuaranteeCharity = create_schema_org_model()


def create_limitedbyguaranteecharity_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_limitedbyguaranteecharity_model(model=model)
    return pydantic_type(model).schema_json()


