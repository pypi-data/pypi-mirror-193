"""
 Codes for use with the [[mediaAuthenticityCategory]] property, indicating the authenticity of a media object (in the context of how it was published or shared). In general these codes are not mutually exclusive, although some combinations (such as 'original' versus 'transformed', 'edited' and 'staged') would be contradictory if applied in the same [[MediaReview]]. Note that the application of these codes is with regard to a piece of media shared or published in a particular context.

https://schema.org/MediaManipulationRatingEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MediaManipulationRatingEnumerationInheritedProperties(TypedDict):
    """Codes for use with the [[mediaAuthenticityCategory]] property, indicating the authenticity of a media object (in the context of how it was published or shared). In general these codes are not mutually exclusive, although some combinations (such as 'original' versus 'transformed', 'edited' and 'staged') would be contradictory if applied in the same [[MediaReview]]. Note that the application of these codes is with regard to a piece of media shared or published in a particular context.

    References:
        https://schema.org/MediaManipulationRatingEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class MediaManipulationRatingEnumerationProperties(TypedDict):
    """Codes for use with the [[mediaAuthenticityCategory]] property, indicating the authenticity of a media object (in the context of how it was published or shared). In general these codes are not mutually exclusive, although some combinations (such as 'original' versus 'transformed', 'edited' and 'staged') would be contradictory if applied in the same [[MediaReview]]. Note that the application of these codes is with regard to a piece of media shared or published in a particular context.

    References:
        https://schema.org/MediaManipulationRatingEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class MediaManipulationRatingEnumerationAllProperties(
    MediaManipulationRatingEnumerationInheritedProperties,
    MediaManipulationRatingEnumerationProperties,
    TypedDict,
):
    pass


class MediaManipulationRatingEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(
        default="MediaManipulationRatingEnumeration", alias="@id"
    )
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MediaManipulationRatingEnumerationProperties,
        MediaManipulationRatingEnumerationInheritedProperties,
        MediaManipulationRatingEnumerationAllProperties,
    ] = MediaManipulationRatingEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MediaManipulationRatingEnumeration"
    return model


MediaManipulationRatingEnumeration = create_schema_org_model()


def create_mediamanipulationratingenumeration_model(
    model: Union[
        MediaManipulationRatingEnumerationProperties,
        MediaManipulationRatingEnumerationInheritedProperties,
        MediaManipulationRatingEnumerationAllProperties,
    ]
):
    _type = deepcopy(MediaManipulationRatingEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MediaManipulationRatingEnumeration. Please see: https://schema.org/MediaManipulationRatingEnumeration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MediaManipulationRatingEnumerationAllProperties):
    pydantic_type = create_mediamanipulationratingenumeration_model(model=model)
    return pydantic_type(model).schema_json()
