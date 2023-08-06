"""
A set of characteristics belonging to people, e.g. who compose an item's target audience.

https://schema.org/PeopleAudience
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PeopleAudienceInheritedProperties(TypedDict):
    """A set of characteristics belonging to people, e.g. who compose an item's target audience.

    References:
        https://schema.org/PeopleAudience
    Note:
        Model Depth 4
    Attributes:
        audienceType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).
        geographicArea: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area associated with the audience.
    """

    audienceType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geographicArea: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class PeopleAudienceProperties(TypedDict):
    """A set of characteristics belonging to people, e.g. who compose an item's target audience.

    References:
        https://schema.org/PeopleAudience
    Note:
        Model Depth 4
    Attributes:
        healthCondition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifying the health condition(s) of a patient, medical study, or other target audience.
        requiredGender: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Audiences defined by a person's gender.
        suggestedMinAge: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): Minimum recommended age in years for the audience or user.
        requiredMinAge: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): Audiences defined by a person's minimum age.
        suggestedMeasurement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A suggested range of body measurements for the intended audience or person, for example inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size chart for wearable products.
        suggestedGender: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The suggested gender of the intended person or audience, for example "male", "female", or "unisex".
        requiredMaxAge: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): Audiences defined by a person's maximum age.
        suggestedAge: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The age or age range for the intended audience or person, for example 3-12 months for infants, 1-5 years for toddlers.
        suggestedMaxAge: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): Maximum recommended age in years for the audience or user.
    """

    healthCondition: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    requiredGender: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    suggestedMinAge: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    requiredMinAge: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    suggestedMeasurement: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    suggestedGender: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    requiredMaxAge: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    suggestedAge: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    suggestedMaxAge: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class PeopleAudienceAllProperties(
    PeopleAudienceInheritedProperties, PeopleAudienceProperties, TypedDict
):
    pass


class PeopleAudienceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PeopleAudience", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"audienceType": {"exclude": True}}
        fields = {"geographicArea": {"exclude": True}}
        fields = {"healthCondition": {"exclude": True}}
        fields = {"requiredGender": {"exclude": True}}
        fields = {"suggestedMinAge": {"exclude": True}}
        fields = {"requiredMinAge": {"exclude": True}}
        fields = {"suggestedMeasurement": {"exclude": True}}
        fields = {"suggestedGender": {"exclude": True}}
        fields = {"requiredMaxAge": {"exclude": True}}
        fields = {"suggestedAge": {"exclude": True}}
        fields = {"suggestedMaxAge": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PeopleAudienceProperties,
        PeopleAudienceInheritedProperties,
        PeopleAudienceAllProperties,
    ] = PeopleAudienceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PeopleAudience"
    return model


PeopleAudience = create_schema_org_model()


def create_peopleaudience_model(
    model: Union[
        PeopleAudienceProperties,
        PeopleAudienceInheritedProperties,
        PeopleAudienceAllProperties,
    ]
):
    _type = deepcopy(PeopleAudienceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of PeopleAudience. Please see: https://schema.org/PeopleAudience"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PeopleAudienceAllProperties):
    pydantic_type = create_peopleaudience_model(model=model)
    return pydantic_type(model).schema_json()
