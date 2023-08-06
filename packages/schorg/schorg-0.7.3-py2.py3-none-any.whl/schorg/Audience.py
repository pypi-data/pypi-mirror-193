"""
Intended audience for an item, i.e. the group for whom the item was created.

https://schema.org/Audience
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AudienceInheritedProperties(TypedDict):
    """Intended audience for an item, i.e. the group for whom the item was created.

    References:
        https://schema.org/Audience
    Note:
        Model Depth 3
    Attributes:
    """


class AudienceProperties(TypedDict):
    """Intended audience for an item, i.e. the group for whom the item was created.

    References:
        https://schema.org/Audience
    Note:
        Model Depth 3
    Attributes:
        audienceType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).
        geographicArea: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area associated with the audience.
    """

    audienceType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geographicArea: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class AudienceAllProperties(AudienceInheritedProperties, AudienceProperties, TypedDict):
    pass


class AudienceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Audience", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"audienceType": {"exclude": True}}
        fields = {"geographicArea": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        AudienceProperties, AudienceInheritedProperties, AudienceAllProperties
    ] = AudienceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Audience"
    return model


Audience = create_schema_org_model()


def create_audience_model(
    model: Union[AudienceProperties, AudienceInheritedProperties, AudienceAllProperties]
):
    _type = deepcopy(AudienceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AudienceAllProperties):
    pydantic_type = create_audience_model(model=model)
    return pydantic_type(model).schema_json()
