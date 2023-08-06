"""
The artwork on the cover of a comic.

https://schema.org/ComicCoverArt
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ComicCoverArtInheritedProperties(TypedDict):
    """The artwork on the cover of a comic.

    References:
        https://schema.org/ComicCoverArt
    Note:
        Model Depth 4
    Attributes:
        inker: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual who traces over the pencil drawings in ink after pencils are complete.
        letterer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual who adds lettering, including speech balloons and sound effects, to artwork.
        penciler: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual who draws the primary narrative artwork.
        artist: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The primary artist for a work    	in a medium other than pencils or digital line art--for example, if the    	primary artwork is done in watercolors or digital paints.
        colorist: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual who adds color to inked drawings.
    """

    inker: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    letterer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    penciler: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    artist: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    colorist: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ComicCoverArtProperties(TypedDict):
    """The artwork on the cover of a comic.

    References:
        https://schema.org/ComicCoverArt
    Note:
        Model Depth 4
    Attributes:
    """


class ComicCoverArtAllProperties(
    ComicCoverArtInheritedProperties, ComicCoverArtProperties, TypedDict
):
    pass


class ComicCoverArtBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ComicCoverArt", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"inker": {"exclude": True}}
        fields = {"letterer": {"exclude": True}}
        fields = {"penciler": {"exclude": True}}
        fields = {"artist": {"exclude": True}}
        fields = {"colorist": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ComicCoverArtProperties,
        ComicCoverArtInheritedProperties,
        ComicCoverArtAllProperties,
    ] = ComicCoverArtAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ComicCoverArt"
    return model


ComicCoverArt = create_schema_org_model()


def create_comiccoverart_model(
    model: Union[
        ComicCoverArtProperties,
        ComicCoverArtInheritedProperties,
        ComicCoverArtAllProperties,
    ]
):
    _type = deepcopy(ComicCoverArtAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ComicCoverArtAllProperties):
    pydantic_type = create_comiccoverart_model(model=model)
    return pydantic_type(model).schema_json()
