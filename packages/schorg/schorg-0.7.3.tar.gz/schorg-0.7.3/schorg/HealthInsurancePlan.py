"""
A US-style health insurance plan, including PPOs, EPOs, and HMOs. 

https://schema.org/HealthInsurancePlan
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HealthInsurancePlanInheritedProperties(TypedDict):
    """A US-style health insurance plan, including PPOs, EPOs, and HMOs.

    References:
        https://schema.org/HealthInsurancePlan
    Note:
        Model Depth 3
    Attributes:
    """


class HealthInsurancePlanProperties(TypedDict):
    """A US-style health insurance plan, including PPOs, EPOs, and HMOs.

    References:
        https://schema.org/HealthInsurancePlan
    Note:
        Model Depth 3
    Attributes:
        benefitsSummaryUrl: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The URL that goes directly to the summary of benefits and coverage for the specific standard plan or plan variation.
        healthPlanId: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The 14-character, HIOS-generated Plan ID number. (Plan IDs must be unique, even across different markets.)
        healthPlanMarketingUrl: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The URL that goes directly to the plan brochure for the specific standard plan or plan variation.
        includesHealthPlanFormulary: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Formularies covered by this plan.
        contactPoint: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A contact point for a person or organization.
        healthPlanDrugTier: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The tier(s) of drugs offered by this formulary or insurance plan.
        healthPlanDrugOption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): TODO.
        includesHealthPlanNetwork: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Networks covered by this plan.
        usesHealthPlanIdStandard: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The standard for interpreting the Plan ID. The preferred is "HIOS". See the Centers for Medicare & Medicaid Services for more details.
    """

    benefitsSummaryUrl: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    healthPlanId: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    healthPlanMarketingUrl: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    includesHealthPlanFormulary: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    contactPoint: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    healthPlanDrugTier: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    healthPlanDrugOption: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    includesHealthPlanNetwork: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    usesHealthPlanIdStandard: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]


class HealthInsurancePlanAllProperties(
    HealthInsurancePlanInheritedProperties, HealthInsurancePlanProperties, TypedDict
):
    pass


class HealthInsurancePlanBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HealthInsurancePlan", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"benefitsSummaryUrl": {"exclude": True}}
        fields = {"healthPlanId": {"exclude": True}}
        fields = {"healthPlanMarketingUrl": {"exclude": True}}
        fields = {"includesHealthPlanFormulary": {"exclude": True}}
        fields = {"contactPoint": {"exclude": True}}
        fields = {"healthPlanDrugTier": {"exclude": True}}
        fields = {"healthPlanDrugOption": {"exclude": True}}
        fields = {"includesHealthPlanNetwork": {"exclude": True}}
        fields = {"usesHealthPlanIdStandard": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        HealthInsurancePlanProperties,
        HealthInsurancePlanInheritedProperties,
        HealthInsurancePlanAllProperties,
    ] = HealthInsurancePlanAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HealthInsurancePlan"
    return model


HealthInsurancePlan = create_schema_org_model()


def create_healthinsuranceplan_model(
    model: Union[
        HealthInsurancePlanProperties,
        HealthInsurancePlanInheritedProperties,
        HealthInsurancePlanAllProperties,
    ]
):
    _type = deepcopy(HealthInsurancePlanAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HealthInsurancePlanAllProperties):
    pydantic_type = create_healthinsuranceplan_model(model=model)
    return pydantic_type(model).schema_json()
