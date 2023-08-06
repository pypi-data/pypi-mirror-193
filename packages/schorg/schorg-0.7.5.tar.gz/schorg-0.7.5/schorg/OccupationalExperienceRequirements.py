"""
Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

https://schema.org/OccupationalExperienceRequirements
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OccupationalExperienceRequirementsInheritedProperties(TypedDict):
    """Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

    References:
        https://schema.org/OccupationalExperienceRequirements
    Note:
        Model Depth 3
    Attributes:
    """


class OccupationalExperienceRequirementsProperties(TypedDict):
    """Indicates employment-related experience requirements, e.g. [[monthsOfExperience]].

    References:
        https://schema.org/OccupationalExperienceRequirements
    Note:
        Model Depth 3
    Attributes:
        monthsOfExperience: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): Indicates the minimal number of months of experience required for a position.
    """

    monthsOfExperience: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class OccupationalExperienceRequirementsAllProperties(
    OccupationalExperienceRequirementsInheritedProperties,
    OccupationalExperienceRequirementsProperties,
    TypedDict,
):
    pass


class OccupationalExperienceRequirementsBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(
        default="OccupationalExperienceRequirements", alias="@id"
    )
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"monthsOfExperience": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        OccupationalExperienceRequirementsProperties,
        OccupationalExperienceRequirementsInheritedProperties,
        OccupationalExperienceRequirementsAllProperties,
    ] = OccupationalExperienceRequirementsAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OccupationalExperienceRequirements"
    return model


OccupationalExperienceRequirements = create_schema_org_model()


def create_occupationalexperiencerequirements_model(
    model: Union[
        OccupationalExperienceRequirementsProperties,
        OccupationalExperienceRequirementsInheritedProperties,
        OccupationalExperienceRequirementsAllProperties,
    ]
):
    _type = deepcopy(OccupationalExperienceRequirementsAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of OccupationalExperienceRequirements. Please see: https://schema.org/OccupationalExperienceRequirements"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: OccupationalExperienceRequirementsAllProperties):
    pydantic_type = create_occupationalexperiencerequirements_model(model=model)
    return pydantic_type(model).schema_json()
