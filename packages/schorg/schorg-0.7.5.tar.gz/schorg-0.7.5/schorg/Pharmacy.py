"""
A pharmacy or drugstore.

https://schema.org/Pharmacy
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PharmacyInheritedProperties(TypedDict):
    """A pharmacy or drugstore.

    References:
        https://schema.org/Pharmacy
    Note:
        Model Depth 4
    Attributes:
        healthPlanNetworkId: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Name or unique ID of network. (Networks are often reused across different insurance plans.)
        medicalSpecialty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical specialty of the provider.
        isAcceptingNewPatients: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]]): Whether the provider is accepting new patients.
    """

    healthPlanNetworkId: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    medicalSpecialty: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    isAcceptingNewPatients: NotRequired[
        Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]
    ]


class PharmacyProperties(TypedDict):
    """A pharmacy or drugstore.

    References:
        https://schema.org/Pharmacy
    Note:
        Model Depth 4
    Attributes:
    """


class PharmacyAllProperties(PharmacyInheritedProperties, PharmacyProperties, TypedDict):
    pass


class PharmacyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Pharmacy", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"healthPlanNetworkId": {"exclude": True}}
        fields = {"medicalSpecialty": {"exclude": True}}
        fields = {"isAcceptingNewPatients": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PharmacyProperties, PharmacyInheritedProperties, PharmacyAllProperties
    ] = PharmacyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Pharmacy"
    return model


Pharmacy = create_schema_org_model()


def create_pharmacy_model(
    model: Union[PharmacyProperties, PharmacyInheritedProperties, PharmacyAllProperties]
):
    _type = deepcopy(PharmacyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Pharmacy. Please see: https://schema.org/Pharmacy"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PharmacyAllProperties):
    pydantic_type = create_pharmacy_model(model=model)
    return pydantic_type(model).schema_json()
