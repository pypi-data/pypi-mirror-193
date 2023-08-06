"""
Target audiences for medical web pages.

https://schema.org/MedicalAudience
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalAudienceInheritedProperties(TypedDict):
    """Target audiences for medical web pages.

    References:
        https://schema.org/MedicalAudience
    Note:
        Model Depth 4
    Attributes:
        healthCondition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifying the health condition(s) of a patient, medical study, or other target audience.
        requiredGender: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Audiences defined by a person's gender.
        suggestedMinAge: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): Minimum recommended age in years for the audience or user.
        requiredMinAge: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): Audiences defined by a person's minimum age.
        suggestedMeasurement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A suggested range of body measurements for the intended audience or person, for example inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size chart for wearable products.
        suggestedGender: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The suggested gender of the intended person or audience, for example "male", "female", or "unisex".
        requiredMaxAge: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): Audiences defined by a person's maximum age.
        suggestedAge: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The age or age range for the intended audience or person, for example 3-12 months for infants, 1-5 years for toddlers.
        suggestedMaxAge: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): Maximum recommended age in years for the audience or user.
        audienceType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).
        geographicArea: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area associated with the audience.
    """

    healthCondition: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    requiredGender: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    suggestedMinAge: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    requiredMinAge: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]
    suggestedMeasurement: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    suggestedGender: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    requiredMaxAge: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]
    suggestedAge: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    suggestedMaxAge: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    audienceType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geographicArea: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class MedicalAudienceProperties(TypedDict):
    """Target audiences for medical web pages.

    References:
        https://schema.org/MedicalAudience
    Note:
        Model Depth 4
    Attributes:
    """


class MedicalAudienceAllProperties(
    MedicalAudienceInheritedProperties, MedicalAudienceProperties, TypedDict
):
    pass


class MedicalAudienceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalAudience", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"healthCondition": {"exclude": True}}
        fields = {"requiredGender": {"exclude": True}}
        fields = {"suggestedMinAge": {"exclude": True}}
        fields = {"requiredMinAge": {"exclude": True}}
        fields = {"suggestedMeasurement": {"exclude": True}}
        fields = {"suggestedGender": {"exclude": True}}
        fields = {"requiredMaxAge": {"exclude": True}}
        fields = {"suggestedAge": {"exclude": True}}
        fields = {"suggestedMaxAge": {"exclude": True}}
        fields = {"audienceType": {"exclude": True}}
        fields = {"geographicArea": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalAudienceProperties,
        MedicalAudienceInheritedProperties,
        MedicalAudienceAllProperties,
    ] = MedicalAudienceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalAudience"
    return model


MedicalAudience = create_schema_org_model()


def create_medicalaudience_model(
    model: Union[
        MedicalAudienceProperties,
        MedicalAudienceInheritedProperties,
        MedicalAudienceAllProperties,
    ]
):
    _type = deepcopy(MedicalAudienceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalAudienceAllProperties):
    pydantic_type = create_medicalaudience_model(model=model)
    return pydantic_type(model).schema_json()
