"""
Individual comic issues are serially published as    	part of a larger series. For the sake of consistency, even one-shot issues    	belong to a series comprised of a single issue. All comic issues can be    	uniquely identified by: the combination of the name and volume number of the    	series to which the issue belongs; the issue number; and the variant    	description of the issue (if any).

https://schema.org/ComicIssue
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ComicIssueInheritedProperties(TypedDict):
    """Individual comic issues are serially published as    	part of a larger series. For the sake of consistency, even one-shot issues    	belong to a series comprised of a single issue. All comic issues can be    	uniquely identified by: the combination of the name and volume number of the    	series to which the issue belongs; the issue number; and the variant    	description of the issue (if any).

    References:
        https://schema.org/ComicIssue
    Note:
        Model Depth 4
    Attributes:
        pageEnd: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The page on which the work ends; for example "138" or "xvi".
        issueNumber: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): Identifies the issue of publication; for example, "iii" or "2".
        pagination: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".
        pageStart: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The page on which the work starts; for example "135" or "xiii".
    """

    pageEnd: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]
    issueNumber: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]
    pagination: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    pageStart: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]


class ComicIssueProperties(TypedDict):
    """Individual comic issues are serially published as    	part of a larger series. For the sake of consistency, even one-shot issues    	belong to a series comprised of a single issue. All comic issues can be    	uniquely identified by: the combination of the name and volume number of the    	series to which the issue belongs; the issue number; and the variant    	description of the issue (if any).

    References:
        https://schema.org/ComicIssue
    Note:
        Model Depth 4
    Attributes:
        inker: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual who traces over the pencil drawings in ink after pencils are complete.
        letterer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual who adds lettering, including speech balloons and sound effects, to artwork.
        penciler: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual who draws the primary narrative artwork.
        variantCover: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A description of the variant cover    	for the issue, if the issue is a variant printing. For example, "Bryan Hitch    	Variant Cover" or "2nd Printing Variant".
        artist: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The primary artist for a work    	in a medium other than pencils or digital line art--for example, if the    	primary artwork is done in watercolors or digital paints.
        colorist: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual who adds color to inked drawings.
    """

    inker: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    letterer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    penciler: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    variantCover: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    artist: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    colorist: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ComicIssueAllProperties(
    ComicIssueInheritedProperties, ComicIssueProperties, TypedDict
):
    pass


class ComicIssueBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ComicIssue", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"pageEnd": {"exclude": True}}
        fields = {"issueNumber": {"exclude": True}}
        fields = {"pagination": {"exclude": True}}
        fields = {"pageStart": {"exclude": True}}
        fields = {"inker": {"exclude": True}}
        fields = {"letterer": {"exclude": True}}
        fields = {"penciler": {"exclude": True}}
        fields = {"variantCover": {"exclude": True}}
        fields = {"artist": {"exclude": True}}
        fields = {"colorist": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ComicIssueProperties, ComicIssueInheritedProperties, ComicIssueAllProperties
    ] = ComicIssueAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ComicIssue"
    return model


ComicIssue = create_schema_org_model()


def create_comicissue_model(
    model: Union[
        ComicIssueProperties, ComicIssueInheritedProperties, ComicIssueAllProperties
    ]
):
    _type = deepcopy(ComicIssueAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ComicIssueAllProperties):
    pydantic_type = create_comicissue_model(model=model)
    return pydantic_type(model).schema_json()
