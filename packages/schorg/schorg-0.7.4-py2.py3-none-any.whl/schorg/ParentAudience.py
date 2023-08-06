"""
A set of characteristics describing parents, who can be interested in viewing some content.

https://schema.org/ParentAudience
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ParentAudienceInheritedProperties(TypedDict):
    """A set of characteristics describing parents, who can be interested in viewing some content.

    References:
        https://schema.org/ParentAudience
    Note:
        Model Depth 5
    Attributes:
        healthCondition: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifying the health condition(s) of a patient, medical study, or other target audience.
        requiredGender: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Audiences defined by a person's gender.
        suggestedMinAge: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): Minimum recommended age in years for the audience or user.
        requiredMinAge: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): Audiences defined by a person's minimum age.
        suggestedMeasurement: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A suggested range of body measurements for the intended audience or person, for example inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size chart for wearable products.
        suggestedGender: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The suggested gender of the intended person or audience, for example "male", "female", or "unisex".
        requiredMaxAge: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): Audiences defined by a person's maximum age.
        suggestedAge: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The age or age range for the intended audience or person, for example 3-12 months for infants, 1-5 years for toddlers.
        suggestedMaxAge: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): Maximum recommended age in years for the audience or user.
    """

    healthCondition: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    requiredGender: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    suggestedMinAge: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    requiredMinAge: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    suggestedMeasurement: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    suggestedGender: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    requiredMaxAge: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    suggestedAge: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    suggestedMaxAge: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]


class ParentAudienceProperties(TypedDict):
    """A set of characteristics describing parents, who can be interested in viewing some content.

    References:
        https://schema.org/ParentAudience
    Note:
        Model Depth 5
    Attributes:
        childMinAge: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): Minimal age of the child.
        childMaxAge: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): Maximal age of the child.
    """

    childMinAge: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    childMaxAge: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]


class ParentAudienceAllProperties(
    ParentAudienceInheritedProperties, ParentAudienceProperties, TypedDict
):
    pass


class ParentAudienceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ParentAudience", alias="@id")
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
        fields = {"childMinAge": {"exclude": True}}
        fields = {"childMaxAge": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ParentAudienceProperties,
        ParentAudienceInheritedProperties,
        ParentAudienceAllProperties,
    ] = ParentAudienceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ParentAudience"
    return model


ParentAudience = create_schema_org_model()


def create_parentaudience_model(
    model: Union[
        ParentAudienceProperties,
        ParentAudienceInheritedProperties,
        ParentAudienceAllProperties,
    ]
):
    _type = deepcopy(ParentAudienceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ParentAudienceAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ParentAudienceAllProperties):
    pydantic_type = create_parentaudience_model(model=model)
    return pydantic_type(model).schema_json()
