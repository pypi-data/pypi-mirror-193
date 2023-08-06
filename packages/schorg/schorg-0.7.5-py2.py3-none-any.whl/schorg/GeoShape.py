"""
The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points.

https://schema.org/GeoShape
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GeoShapeInheritedProperties(TypedDict):
    """The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points.

    References:
        https://schema.org/GeoShape
    Note:
        Model Depth 4
    Attributes:
    """


class GeoShapeProperties(TypedDict):
    """The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points.

    References:
        https://schema.org/GeoShape
    Note:
        Model Depth 4
    Attributes:
        polygon: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more space delimited points where the first and final points are identical.
        circle: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A circle is the circular region of a specified radius centered at a specified latitude and longitude. A circle is expressed as a pair followed by a radius in meters.
        elevation: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The elevation of a location ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)). Values may be of the form 'NUMBER UNIT\_OF\_MEASUREMENT' (e.g., '1,000 m', '3,200 ft') while numbers alone should be assumed to be a value in meters.
        addressCountry: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1).
        postalCode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The postal code. For example, 94043.
        address: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Physical address of the item.
        line: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A line is a point-to-point path consisting of two or more points. A line is expressed as a series of two or more point objects separated by space.
        box: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A box is the area enclosed by the rectangle formed by two points. The first point is the lower corner, the second point is the upper corner. A box is expressed as two points separated by a space character.
    """

    polygon: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    circle: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    elevation: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    addressCountry: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    postalCode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    address: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    line: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    box: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class GeoShapeAllProperties(GeoShapeInheritedProperties, GeoShapeProperties, TypedDict):
    pass


class GeoShapeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GeoShape", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"polygon": {"exclude": True}}
        fields = {"circle": {"exclude": True}}
        fields = {"elevation": {"exclude": True}}
        fields = {"addressCountry": {"exclude": True}}
        fields = {"postalCode": {"exclude": True}}
        fields = {"address": {"exclude": True}}
        fields = {"line": {"exclude": True}}
        fields = {"box": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        GeoShapeProperties, GeoShapeInheritedProperties, GeoShapeAllProperties
    ] = GeoShapeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GeoShape"
    return model


GeoShape = create_schema_org_model()


def create_geoshape_model(
    model: Union[GeoShapeProperties, GeoShapeInheritedProperties, GeoShapeAllProperties]
):
    _type = deepcopy(GeoShapeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of GeoShape. Please see: https://schema.org/GeoShape"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: GeoShapeAllProperties):
    pydantic_type = create_geoshape_model(model=model)
    return pydantic_type(model).schema_json()
