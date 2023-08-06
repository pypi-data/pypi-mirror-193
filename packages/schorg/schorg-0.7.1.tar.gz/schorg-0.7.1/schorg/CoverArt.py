"""
The artwork on the outer surface of a CreativeWork.

https://schema.org/CoverArt
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CoverArtInheritedProperties(TypedDict):
    """The artwork on the outer surface of a CreativeWork.

    References:
        https://schema.org/CoverArt
    Note:
        Model Depth 4
    Attributes:
        inker: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual who traces over the pencil drawings in ink after pencils are complete.
        width: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The width of the item.
        letterer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual who adds lettering, including speech balloons and sound effects, to artwork.
        depth: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The depth of the item.
        penciler: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual who draws the primary narrative artwork.
        artist: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The primary artist for a work    	in a medium other than pencils or digital line art--for example, if the    	primary artwork is done in watercolors or digital paints.
        height: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The height of the item.
        colorist: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual who adds color to inked drawings.
        artMedium: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The material used. (E.g. Oil, Watercolour, Acrylic, Linoprint, Marble, Cyanotype, Digital, Lithograph, DryPoint, Intaglio, Pastel, Woodcut, Pencil, Mixed Media, etc.)
        surface: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A material used as a surface in some artwork, e.g. Canvas, Paper, Wood, Board, etc.
        artform: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): e.g. Painting, Drawing, Sculpture, Print, Photograph, Assemblage, Collage, etc.
        artEdition: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The number of copies when multiple copies of a piece of artwork are produced - e.g. for a limited edition of 20 prints, 'artEdition' refers to the total number of copies (in this example "20").
        artworkSurface: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The supporting materials for the artwork, e.g. Canvas, Paper, Wood, Board, etc.
    """

    inker: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    width: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    letterer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    depth: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    penciler: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    artist: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    height: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    colorist: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    artMedium: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    surface: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    artform: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    artEdition: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    artworkSurface: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    


class CoverArtProperties(TypedDict):
    """The artwork on the outer surface of a CreativeWork.

    References:
        https://schema.org/CoverArt
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(CoverArtInheritedProperties , CoverArtProperties, TypedDict):
    pass


class CoverArtBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CoverArt",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'inker': {'exclude': True}}
        fields = {'width': {'exclude': True}}
        fields = {'letterer': {'exclude': True}}
        fields = {'depth': {'exclude': True}}
        fields = {'penciler': {'exclude': True}}
        fields = {'artist': {'exclude': True}}
        fields = {'height': {'exclude': True}}
        fields = {'colorist': {'exclude': True}}
        fields = {'artMedium': {'exclude': True}}
        fields = {'surface': {'exclude': True}}
        fields = {'artform': {'exclude': True}}
        fields = {'artEdition': {'exclude': True}}
        fields = {'artworkSurface': {'exclude': True}}
        


def create_schema_org_model(type_: Union[CoverArtProperties, CoverArtInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CoverArt"
    return model
    

CoverArt = create_schema_org_model()


def create_coverart_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_coverart_model(model=model)
    return pydantic_type(model).schema_json()


