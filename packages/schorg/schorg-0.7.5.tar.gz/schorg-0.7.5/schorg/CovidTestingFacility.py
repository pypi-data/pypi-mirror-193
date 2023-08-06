"""
A CovidTestingFacility is a [[MedicalClinic]] where testing for the COVID-19 Coronavirus      disease is available. If the facility is being made available from an established [[Pharmacy]], [[Hotel]], or other      non-medical organization, multiple types can be listed. This makes it easier to re-use existing schema.org information      about that place, e.g. contact info, address, opening hours. Note that in an emergency, such information may not always be reliable.      

https://schema.org/CovidTestingFacility
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CovidTestingFacilityInheritedProperties(TypedDict):
    """A CovidTestingFacility is a [[MedicalClinic]] where testing for the COVID-19 Coronavirus      disease is available. If the facility is being made available from an established [[Pharmacy]], [[Hotel]], or other      non-medical organization, multiple types can be listed. This makes it easier to re-use existing schema.org information      about that place, e.g. contact info, address, opening hours. Note that in an emergency, such information may not always be reliable.

    References:
        https://schema.org/CovidTestingFacility
    Note:
        Model Depth 5
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


class CovidTestingFacilityProperties(TypedDict):
    """A CovidTestingFacility is a [[MedicalClinic]] where testing for the COVID-19 Coronavirus      disease is available. If the facility is being made available from an established [[Pharmacy]], [[Hotel]], or other      non-medical organization, multiple types can be listed. This makes it easier to re-use existing schema.org information      about that place, e.g. contact info, address, opening hours. Note that in an emergency, such information may not always be reliable.

    References:
        https://schema.org/CovidTestingFacility
    Note:
        Model Depth 5
    Attributes:
    """


class CovidTestingFacilityAllProperties(
    CovidTestingFacilityInheritedProperties, CovidTestingFacilityProperties, TypedDict
):
    pass


class CovidTestingFacilityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CovidTestingFacility", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"medicalSpecialty": {"exclude": True}}
        fields = {"availableService": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        CovidTestingFacilityProperties,
        CovidTestingFacilityInheritedProperties,
        CovidTestingFacilityAllProperties,
    ] = CovidTestingFacilityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CovidTestingFacility"
    return model


CovidTestingFacility = create_schema_org_model()


def create_covidtestingfacility_model(
    model: Union[
        CovidTestingFacilityProperties,
        CovidTestingFacilityInheritedProperties,
        CovidTestingFacilityAllProperties,
    ]
):
    _type = deepcopy(CovidTestingFacilityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of CovidTestingFacility. Please see: https://schema.org/CovidTestingFacility"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CovidTestingFacilityAllProperties):
    pydantic_type = create_covidtestingfacility_model(model=model)
    return pydantic_type(model).schema_json()
