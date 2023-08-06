"""
A doctor's office.

https://schema.org/Physician
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PhysicianInheritedProperties(TypedDict):
    """A doctor's office.

    References:
        https://schema.org/Physician
    Note:
        Model Depth 4
    Attributes:
        healthPlanNetworkId: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Name or unique ID of network. (Networks are often reused across different insurance plans.)
        medicalSpecialty: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical specialty of the provider.
        isAcceptingNewPatients: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Whether the provider is accepting new patients.
    """

    healthPlanNetworkId: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    medicalSpecialty: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    isAcceptingNewPatients: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]


class PhysicianProperties(TypedDict):
    """A doctor's office.

    References:
        https://schema.org/Physician
    Note:
        Model Depth 4
    Attributes:
        hospitalAffiliation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A hospital with which the physician or office is affiliated.
        medicalSpecialty: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical specialty of the provider.
        availableService: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical service available from this provider.
    """

    hospitalAffiliation: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    medicalSpecialty: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    availableService: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class PhysicianAllProperties(
    PhysicianInheritedProperties, PhysicianProperties, TypedDict
):
    pass


class PhysicianBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Physician", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"healthPlanNetworkId": {"exclude": True}}
        fields = {"medicalSpecialty": {"exclude": True}}
        fields = {"isAcceptingNewPatients": {"exclude": True}}
        fields = {"hospitalAffiliation": {"exclude": True}}
        fields = {"medicalSpecialty": {"exclude": True}}
        fields = {"availableService": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PhysicianProperties, PhysicianInheritedProperties, PhysicianAllProperties
    ] = PhysicianAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Physician"
    return model


Physician = create_schema_org_model()


def create_physician_model(
    model: Union[
        PhysicianProperties, PhysicianInheritedProperties, PhysicianAllProperties
    ]
):
    _type = deepcopy(PhysicianAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PhysicianAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PhysicianAllProperties):
    pydantic_type = create_physician_model(model=model)
    return pydantic_type(model).schema_json()
