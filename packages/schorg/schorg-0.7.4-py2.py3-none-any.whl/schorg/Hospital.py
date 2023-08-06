"""
A hospital.

https://schema.org/Hospital
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HospitalInheritedProperties(TypedDict):
    """A hospital.

    References:
        https://schema.org/Hospital
    Note:
        Model Depth 4
    Attributes:
        healthPlanNetworkId: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Name or unique ID of network. (Networks are often reused across different insurance plans.)
        medicalSpecialty: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical specialty of the provider.
        isAcceptingNewPatients: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Whether the provider is accepting new patients.
        openingHours: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.* Days are specified using the following two-letter combinations: ```Mo```, ```Tu```, ```We```, ```Th```, ```Fr```, ```Sa```, ```Su```.* Times are specified using 24:00 format. For example, 3pm is specified as ```15:00```, 10am as ```10:00```. * Here is an example: <code>&lt;time itemprop="openingHours" datetime=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays and Thursdays 4-8pm&lt;/time&gt;</code>.* If a business is open 7 days a week, then it can be specified as <code>&lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Mo-Su&quot;&gt;Monday through Sunday, all day&lt;/time&gt;</code>.
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
    openingHours: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class HospitalProperties(TypedDict):
    """A hospital.

    References:
        https://schema.org/Hospital
    Note:
        Model Depth 4
    Attributes:
        healthcareReportingData: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates data describing a hospital, e.g. a CDC [[CDCPMDRecord]] or as some kind of [[Dataset]].
        medicalSpecialty: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical specialty of the provider.
        availableService: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A medical service available from this provider.
    """

    healthcareReportingData: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    medicalSpecialty: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    availableService: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class HospitalAllProperties(HospitalInheritedProperties, HospitalProperties, TypedDict):
    pass


class HospitalBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Hospital", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"healthPlanNetworkId": {"exclude": True}}
        fields = {"medicalSpecialty": {"exclude": True}}
        fields = {"isAcceptingNewPatients": {"exclude": True}}
        fields = {"openingHours": {"exclude": True}}
        fields = {"healthcareReportingData": {"exclude": True}}
        fields = {"medicalSpecialty": {"exclude": True}}
        fields = {"availableService": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        HospitalProperties, HospitalInheritedProperties, HospitalAllProperties
    ] = HospitalAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Hospital"
    return model


Hospital = create_schema_org_model()


def create_hospital_model(
    model: Union[HospitalProperties, HospitalInheritedProperties, HospitalAllProperties]
):
    _type = deepcopy(HospitalAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of HospitalAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HospitalAllProperties):
    pydantic_type = create_hospital_model(model=model)
    return pydantic_type(model).schema_json()
