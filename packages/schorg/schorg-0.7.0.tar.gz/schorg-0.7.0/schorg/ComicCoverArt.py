"""
The artwork on the cover of a comic.

https://schema.org/ComicCoverArt
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ComicCoverArtInheritedProperties(TypedDict):
    """The artwork on the cover of a comic.

    References:
        https://schema.org/ComicCoverArt
    Note:
        Model Depth 4
    Attributes:
        inker: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The individual who traces over the pencil drawings in ink after pencils are complete.
        letterer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The individual who adds lettering, including speech balloons and sound effects, to artwork.
        penciler: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The individual who draws the primary narrative artwork.
        artist: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The primary artist for a work    	in a medium other than pencils or digital line art--for example, if the    	primary artwork is done in watercolors or digital paints.
        colorist: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The individual who adds color to inked drawings.
    """

    inker: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    letterer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    penciler: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    artist: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    colorist: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class ComicCoverArtProperties(TypedDict):
    """The artwork on the cover of a comic.

    References:
        https://schema.org/ComicCoverArt
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(ComicCoverArtInheritedProperties , ComicCoverArtProperties, TypedDict):
    pass


class ComicCoverArtBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ComicCoverArt",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'inker': {'exclude': True}}
        fields = {'letterer': {'exclude': True}}
        fields = {'penciler': {'exclude': True}}
        fields = {'artist': {'exclude': True}}
        fields = {'colorist': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ComicCoverArtProperties, ComicCoverArtInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ComicCoverArt"
    return model
    

ComicCoverArt = create_schema_org_model()


def create_comiccoverart_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_comiccoverart_model(model=model)
    return pydantic_type(model).schema_json()


