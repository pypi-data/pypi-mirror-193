"""
Bank or credit union.

https://schema.org/BankOrCreditUnion
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BankOrCreditUnionInheritedProperties(TypedDict):
    """Bank or credit union.

    References:
        https://schema.org/BankOrCreditUnion
    Note:
        Model Depth 5
    Attributes:
        feesAndCommissionsSpecification: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    """

    feesAndCommissionsSpecification: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    


class BankOrCreditUnionProperties(TypedDict):
    """Bank or credit union.

    References:
        https://schema.org/BankOrCreditUnion
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(BankOrCreditUnionInheritedProperties , BankOrCreditUnionProperties, TypedDict):
    pass


class BankOrCreditUnionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BankOrCreditUnion",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'feesAndCommissionsSpecification': {'exclude': True}}
        


def create_schema_org_model(type_: Union[BankOrCreditUnionProperties, BankOrCreditUnionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BankOrCreditUnion"
    return model
    

BankOrCreditUnion = create_schema_org_model()


def create_bankorcreditunion_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bankorcreditunion_model(model=model)
    return pydantic_type(model).schema_json()


