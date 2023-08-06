"""
A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare. Previously limited to outpatients but with evolution it may be open to inpatients as well.

https://schema.org/MedicalClinic
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalClinicInheritedProperties(TypedDict):
    """A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare. Previously limited to outpatients but with evolution it may be open to inpatients as well.

    References:
        https://schema.org/MedicalClinic
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


class MedicalClinicProperties(TypedDict):
    """A facility, often associated with a hospital or medical school, that is devoted to the specific diagnosis and/or healthcare. Previously limited to outpatients but with evolution it may be open to inpatients as well.

    References:
        https://schema.org/MedicalClinic
    Note:
        Model Depth 4
    Attributes:
        medicalSpecialty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical specialty of the provider.
        availableService: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical service available from this provider.
    """

    medicalSpecialty: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    availableService: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class MedicalClinicAllProperties(
    MedicalClinicInheritedProperties, MedicalClinicProperties, TypedDict
):
    pass


class MedicalClinicBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalClinic", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"healthPlanNetworkId": {"exclude": True}}
        fields = {"medicalSpecialty": {"exclude": True}}
        fields = {"isAcceptingNewPatients": {"exclude": True}}
        fields = {"medicalSpecialty": {"exclude": True}}
        fields = {"availableService": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalClinicProperties,
        MedicalClinicInheritedProperties,
        MedicalClinicAllProperties,
    ] = MedicalClinicAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalClinic"
    return model


MedicalClinic = create_schema_org_model()


def create_medicalclinic_model(
    model: Union[
        MedicalClinicProperties,
        MedicalClinicInheritedProperties,
        MedicalClinicAllProperties,
    ]
):
    _type = deepcopy(MedicalClinicAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MedicalClinic. Please see: https://schema.org/MedicalClinic"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MedicalClinicAllProperties):
    pydantic_type = create_medicalclinic_model(model=model)
    return pydantic_type(model).schema_json()
