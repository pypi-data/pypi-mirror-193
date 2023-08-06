"""
A US-style health insurance plan network. 

https://schema.org/HealthPlanNetwork
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HealthPlanNetworkInheritedProperties(TypedDict):
    """A US-style health insurance plan network. 

    References:
        https://schema.org/HealthPlanNetwork
    Note:
        Model Depth 3
    Attributes:
    """

    


class HealthPlanNetworkProperties(TypedDict):
    """A US-style health insurance plan network. 

    References:
        https://schema.org/HealthPlanNetwork
    Note:
        Model Depth 3
    Attributes:
        healthPlanNetworkTier: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The tier(s) for this network.
        healthPlanNetworkId: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Name or unique ID of network. (Networks are often reused across different insurance plans.)
        healthPlanCostSharing: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): The costs to the patient for services under this network or formulary.
    """

    healthPlanNetworkTier: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    healthPlanNetworkId: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    healthPlanCostSharing: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    


class AllProperties(HealthPlanNetworkInheritedProperties , HealthPlanNetworkProperties, TypedDict):
    pass


class HealthPlanNetworkBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HealthPlanNetwork",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'healthPlanNetworkTier': {'exclude': True}}
        fields = {'healthPlanNetworkId': {'exclude': True}}
        fields = {'healthPlanCostSharing': {'exclude': True}}
        


def create_schema_org_model(type_: Union[HealthPlanNetworkProperties, HealthPlanNetworkInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HealthPlanNetwork"
    return model
    

HealthPlanNetwork = create_schema_org_model()


def create_healthplannetwork_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_healthplannetwork_model(model=model)
    return pydantic_type(model).schema_json()


