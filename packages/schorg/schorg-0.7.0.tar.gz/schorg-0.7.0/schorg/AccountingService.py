"""
Accountancy business.As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\(s).      

https://schema.org/AccountingService
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AccountingServiceInheritedProperties(TypedDict):
    """Accountancy business.As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\(s).      

    References:
        https://schema.org/AccountingService
    Note:
        Model Depth 5
    Attributes:
        feesAndCommissionsSpecification: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    """

    feesAndCommissionsSpecification: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    


class AccountingServiceProperties(TypedDict):
    """Accountancy business.As a [[LocalBusiness]] it can be described as a [[provider]] of one or more [[Service]]\(s).      

    References:
        https://schema.org/AccountingService
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(AccountingServiceInheritedProperties , AccountingServiceProperties, TypedDict):
    pass


class AccountingServiceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AccountingService",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'feesAndCommissionsSpecification': {'exclude': True}}
        


def create_schema_org_model(type_: Union[AccountingServiceProperties, AccountingServiceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AccountingService"
    return model
    

AccountingService = create_schema_org_model()


def create_accountingservice_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_accountingservice_model(model=model)
    return pydantic_type(model).schema_json()


