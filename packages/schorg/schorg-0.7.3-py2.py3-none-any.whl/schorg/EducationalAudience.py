"""
An EducationalAudience.

https://schema.org/EducationalAudience
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EducationalAudienceInheritedProperties(TypedDict):
    """An EducationalAudience.

    References:
        https://schema.org/EducationalAudience
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


class EducationalAudienceProperties(TypedDict):
    """An EducationalAudience.

    References:
        https://schema.org/EducationalAudience
    Note:
        Model Depth 4
    Attributes:
        educationalRole: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An educationalRole of an EducationalAudience.
    """

    educationalRole: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class EducationalAudienceAllProperties(
    EducationalAudienceInheritedProperties, EducationalAudienceProperties, TypedDict
):
    pass


class EducationalAudienceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EducationalAudience", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"audienceType": {"exclude": True}}
        fields = {"geographicArea": {"exclude": True}}
        fields = {"educationalRole": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        EducationalAudienceProperties,
        EducationalAudienceInheritedProperties,
        EducationalAudienceAllProperties,
    ] = EducationalAudienceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EducationalAudience"
    return model


EducationalAudience = create_schema_org_model()


def create_educationalaudience_model(
    model: Union[
        EducationalAudienceProperties,
        EducationalAudienceInheritedProperties,
        EducationalAudienceAllProperties,
    ]
):
    _type = deepcopy(EducationalAudienceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EducationalAudienceAllProperties):
    pydantic_type = create_educationalaudience_model(model=model)
    return pydantic_type(model).schema_json()
