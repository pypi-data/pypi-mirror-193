"""
A US-style health insurance plan network. 

https://schema.org/HealthPlanNetwork
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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
        healthPlanNetworkTier: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The tier(s) for this network.
        healthPlanNetworkId: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Name or unique ID of network. (Networks are often reused across different insurance plans.)
        healthPlanCostSharing: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]]): The costs to the patient for services under this network or formulary.
    """

    healthPlanNetworkTier: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    healthPlanNetworkId: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    healthPlanCostSharing: NotRequired[
        Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]
    ]


class HealthPlanNetworkAllProperties(
    HealthPlanNetworkInheritedProperties, HealthPlanNetworkProperties, TypedDict
):
    pass


class HealthPlanNetworkBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HealthPlanNetwork", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"healthPlanNetworkTier": {"exclude": True}}
        fields = {"healthPlanNetworkId": {"exclude": True}}
        fields = {"healthPlanCostSharing": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        HealthPlanNetworkProperties,
        HealthPlanNetworkInheritedProperties,
        HealthPlanNetworkAllProperties,
    ] = HealthPlanNetworkAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HealthPlanNetwork"
    return model


HealthPlanNetwork = create_schema_org_model()


def create_healthplannetwork_model(
    model: Union[
        HealthPlanNetworkProperties,
        HealthPlanNetworkInheritedProperties,
        HealthPlanNetworkAllProperties,
    ]
):
    _type = deepcopy(HealthPlanNetworkAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of HealthPlanNetwork. Please see: https://schema.org/HealthPlanNetwork"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: HealthPlanNetworkAllProperties):
    pydantic_type = create_healthplannetwork_model(model=model)
    return pydantic_type(model).schema_json()
