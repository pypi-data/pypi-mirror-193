"""
A description of costs to the patient under a given network or formulary.

https://schema.org/HealthPlanCostSharingSpecification
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HealthPlanCostSharingSpecificationInheritedProperties(TypedDict):
    """A description of costs to the patient under a given network or formulary.

    References:
        https://schema.org/HealthPlanCostSharingSpecification
    Note:
        Model Depth 3
    Attributes:
    """


class HealthPlanCostSharingSpecificationProperties(TypedDict):
    """A description of costs to the patient under a given network or formulary.

    References:
        https://schema.org/HealthPlanCostSharingSpecification
    Note:
        Model Depth 3
    Attributes:
        healthPlanCoinsuranceRate: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The rate of coinsurance expressed as a number between 0.0 and 1.0.
        healthPlanCopayOption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Whether the copay is before or after deductible, etc. TODO: Is this a closed set?
        healthPlanPharmacyCategory: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The category or type of pharmacy associated with this cost sharing.
        healthPlanCopay: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The copay amount.
        healthPlanCoinsuranceOption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Whether the coinsurance applies before or after deductible, etc. TODO: Is this a closed set?
    """

    healthPlanCoinsuranceRate: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    healthPlanCopayOption: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    healthPlanPharmacyCategory: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    healthPlanCopay: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    healthPlanCoinsuranceOption: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class HealthPlanCostSharingSpecificationAllProperties(
    HealthPlanCostSharingSpecificationInheritedProperties,
    HealthPlanCostSharingSpecificationProperties,
    TypedDict,
):
    pass


class HealthPlanCostSharingSpecificationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(
        default="HealthPlanCostSharingSpecification", alias="@id"
    )
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"healthPlanCoinsuranceRate": {"exclude": True}}
        fields = {"healthPlanCopayOption": {"exclude": True}}
        fields = {"healthPlanPharmacyCategory": {"exclude": True}}
        fields = {"healthPlanCopay": {"exclude": True}}
        fields = {"healthPlanCoinsuranceOption": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        HealthPlanCostSharingSpecificationProperties,
        HealthPlanCostSharingSpecificationInheritedProperties,
        HealthPlanCostSharingSpecificationAllProperties,
    ] = HealthPlanCostSharingSpecificationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HealthPlanCostSharingSpecification"
    return model


HealthPlanCostSharingSpecification = create_schema_org_model()


def create_healthplancostsharingspecification_model(
    model: Union[
        HealthPlanCostSharingSpecificationProperties,
        HealthPlanCostSharingSpecificationInheritedProperties,
        HealthPlanCostSharingSpecificationAllProperties,
    ]
):
    _type = deepcopy(HealthPlanCostSharingSpecificationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of HealthPlanCostSharingSpecification. Please see: https://schema.org/HealthPlanCostSharingSpecification"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: HealthPlanCostSharingSpecificationAllProperties):
    pydantic_type = create_healthplancostsharingspecification_model(model=model)
    return pydantic_type(model).schema_json()
