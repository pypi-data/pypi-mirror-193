"""
ATM/cash machine.

https://schema.org/AutomatedTeller
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AutomatedTellerInheritedProperties(TypedDict):
    """ATM/cash machine.

    References:
        https://schema.org/AutomatedTeller
    Note:
        Model Depth 5
    Attributes:
        feesAndCommissionsSpecification: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    """

    feesAndCommissionsSpecification: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    


class AutomatedTellerProperties(TypedDict):
    """ATM/cash machine.

    References:
        https://schema.org/AutomatedTeller
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(AutomatedTellerInheritedProperties , AutomatedTellerProperties, TypedDict):
    pass


class AutomatedTellerBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AutomatedTeller",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'feesAndCommissionsSpecification': {'exclude': True}}
        


def create_schema_org_model(type_: Union[AutomatedTellerProperties, AutomatedTellerInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AutomatedTeller"
    return model
    

AutomatedTeller = create_schema_org_model()


def create_automatedteller_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_automatedteller_model(model=model)
    return pydantic_type(model).schema_json()


