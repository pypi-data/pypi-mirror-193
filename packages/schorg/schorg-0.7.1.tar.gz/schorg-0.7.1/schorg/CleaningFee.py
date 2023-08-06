"""
Represents the cleaning fee part of the total price for an offered product, for example a vacation rental.

https://schema.org/CleaningFee
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CleaningFeeInheritedProperties(TypedDict):
    """Represents the cleaning fee part of the total price for an offered product, for example a vacation rental.

    References:
        https://schema.org/CleaningFee
    Note:
        Model Depth 5
    Attributes:
    """

    


class CleaningFeeProperties(TypedDict):
    """Represents the cleaning fee part of the total price for an offered product, for example a vacation rental.

    References:
        https://schema.org/CleaningFee
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(CleaningFeeInheritedProperties , CleaningFeeProperties, TypedDict):
    pass


class CleaningFeeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CleaningFee",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[CleaningFeeProperties, CleaningFeeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CleaningFee"
    return model
    

CleaningFee = create_schema_org_model()


def create_cleaningfee_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_cleaningfee_model(model=model)
    return pydantic_type(model).schema_json()


