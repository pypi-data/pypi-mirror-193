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
        inker: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The individual who traces over the pencil drawings in ink after pencils are complete.
        width: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The width of the item.
        letterer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The individual who adds lettering, including speech balloons and sound effects, to artwork.
        depth: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The depth of the item.
        penciler: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The individual who draws the primary narrative artwork.
        artist: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The primary artist for a work    	in a medium other than pencils or digital line art--for example, if the    	primary artwork is done in watercolors or digital paints.
        height: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The height of the item.
        colorist: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The individual who adds color to inked drawings.
        artMedium: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The material used. (E.g. Oil, Watercolour, Acrylic, Linoprint, Marble, Cyanotype, Digital, Lithograph, DryPoint, Intaglio, Pastel, Woodcut, Pencil, Mixed Media, etc.)
        surface: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A material used as a surface in some artwork, e.g. Canvas, Paper, Wood, Board, etc.
        artform: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): e.g. Painting, Drawing, Sculpture, Print, Photograph, Assemblage, Collage, etc.
        artEdition: (Optional[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]): The number of copies when multiple copies of a piece of artwork are produced - e.g. for a limited edition of 20 prints, 'artEdition' refers to the total number of copies (in this example "20").
        artworkSurface: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The supporting materials for the artwork, e.g. Canvas, Paper, Wood, Board, etc.
    """

    inker: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    width: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    letterer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    depth: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    penciler: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    artist: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    height: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    colorist: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    artMedium: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    surface: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    artform: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    artEdition: NotRequired[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]
    artworkSurface: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    


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
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_coverart_model(model=model)
    return pydantic_type(model).schema_json()


