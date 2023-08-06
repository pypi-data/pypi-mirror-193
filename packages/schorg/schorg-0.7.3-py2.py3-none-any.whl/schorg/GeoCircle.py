"""
A GeoCircle is a GeoShape representing a circular geographic area. As it is a GeoShape          it provides the simple textual property 'circle', but also allows the combination of postalCode alongside geoRadius.          The center of the circle can be indicated via the 'geoMidpoint' property, or more approximately using 'address', 'postalCode'.       

https://schema.org/GeoCircle
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GeoCircleInheritedProperties(TypedDict):
    """A GeoCircle is a GeoShape representing a circular geographic area. As it is a GeoShape          it provides the simple textual property 'circle', but also allows the combination of postalCode alongside geoRadius.          The center of the circle can be indicated via the 'geoMidpoint' property, or more approximately using 'address', 'postalCode'.

    References:
        https://schema.org/GeoCircle
    Note:
        Model Depth 5
    Attributes:
        polygon: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more space delimited points where the first and final points are identical.
        circle: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A circle is the circular region of a specified radius centered at a specified latitude and longitude. A circle is expressed as a pair followed by a radius in meters.
        elevation: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The elevation of a location ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)). Values may be of the form 'NUMBER UNIT\_OF\_MEASUREMENT' (e.g., '1,000 m', '3,200 ft') while numbers alone should be assumed to be a value in meters.
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
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    addressCountry: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    postalCode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    address: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    line: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    box: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class GeoCircleProperties(TypedDict):
    """A GeoCircle is a GeoShape representing a circular geographic area. As it is a GeoShape          it provides the simple textual property 'circle', but also allows the combination of postalCode alongside geoRadius.          The center of the circle can be indicated via the 'geoMidpoint' property, or more approximately using 'address', 'postalCode'.

    References:
        https://schema.org/GeoCircle
    Note:
        Model Depth 5
    Attributes:
        geoMidpoint: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the GeoCoordinates at the centre of a GeoShape, e.g. GeoCircle.
        geoRadius: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): Indicates the approximate radius of a GeoCircle (metres unless indicated otherwise via Distance notation).
    """

    geoMidpoint: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoRadius: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]


class GeoCircleAllProperties(
    GeoCircleInheritedProperties, GeoCircleProperties, TypedDict
):
    pass


class GeoCircleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GeoCircle", alias="@id")
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
        fields = {"geoMidpoint": {"exclude": True}}
        fields = {"geoRadius": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        GeoCircleProperties, GeoCircleInheritedProperties, GeoCircleAllProperties
    ] = GeoCircleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GeoCircle"
    return model


GeoCircle = create_schema_org_model()


def create_geocircle_model(
    model: Union[
        GeoCircleProperties, GeoCircleInheritedProperties, GeoCircleAllProperties
    ]
):
    _type = deepcopy(GeoCircleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GeoCircleAllProperties):
    pydantic_type = create_geocircle_model(model=model)
    return pydantic_type(model).schema_json()
