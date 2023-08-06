"""
For a given health insurance plan, the specification for costs and coverage of prescription drugs. 

https://schema.org/HealthPlanFormulary
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HealthPlanFormularyInheritedProperties(TypedDict):
    """For a given health insurance plan, the specification for costs and coverage of prescription drugs. 

    References:
        https://schema.org/HealthPlanFormulary
    Note:
        Model Depth 3
    Attributes:
    """

    


class HealthPlanFormularyProperties(TypedDict):
    """For a given health insurance plan, the specification for costs and coverage of prescription drugs. 

    References:
        https://schema.org/HealthPlanFormulary
    Note:
        Model Depth 3
    Attributes:
        healthPlanCostSharing: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): The costs to the patient for services under this network or formulary.
        offersPrescriptionByMail: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Whether prescriptions can be delivered by mail.
        healthPlanDrugTier: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The tier(s) of drugs offered by this formulary or insurance plan.
    """

    healthPlanCostSharing: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    offersPrescriptionByMail: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    healthPlanDrugTier: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(HealthPlanFormularyInheritedProperties , HealthPlanFormularyProperties, TypedDict):
    pass


class HealthPlanFormularyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HealthPlanFormulary",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'healthPlanCostSharing': {'exclude': True}}
        fields = {'offersPrescriptionByMail': {'exclude': True}}
        fields = {'healthPlanDrugTier': {'exclude': True}}
        


def create_schema_org_model(type_: Union[HealthPlanFormularyProperties, HealthPlanFormularyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HealthPlanFormulary"
    return model
    

HealthPlanFormulary = create_schema_org_model()


def create_healthplanformulary_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_healthplanformulary_model(model=model)
    return pydantic_type(model).schema_json()


