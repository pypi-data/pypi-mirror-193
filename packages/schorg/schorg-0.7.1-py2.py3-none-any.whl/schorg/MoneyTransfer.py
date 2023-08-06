"""
The act of transferring money from one place to another place. This may occur electronically or physically.

https://schema.org/MoneyTransfer
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MoneyTransferInheritedProperties(TypedDict):
    """The act of transferring money from one place to another place. This may occur electronically or physically.

    References:
        https://schema.org/MoneyTransfer
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
        fromLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The original location of the object or the agent before the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fromLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class MoneyTransferProperties(TypedDict):
    """The act of transferring money from one place to another place. This may occur electronically or physically.

    References:
        https://schema.org/MoneyTransfer
    Note:
        Model Depth 4
    Attributes:
        amount: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The amount of money.
        beneficiaryBank: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A bank or bank’s branch, financial institution or international financial institution operating the beneficiary’s bank account or releasing funds for the beneficiary.
    """

    amount: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    beneficiaryBank: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(MoneyTransferInheritedProperties , MoneyTransferProperties, TypedDict):
    pass


class MoneyTransferBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MoneyTransfer",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'toLocation': {'exclude': True}}
        fields = {'fromLocation': {'exclude': True}}
        fields = {'amount': {'exclude': True}}
        fields = {'beneficiaryBank': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MoneyTransferProperties, MoneyTransferInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MoneyTransfer"
    return model
    

MoneyTransfer = create_schema_org_model()


def create_moneytransfer_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_moneytransfer_model(model=model)
    return pydantic_type(model).schema_json()


