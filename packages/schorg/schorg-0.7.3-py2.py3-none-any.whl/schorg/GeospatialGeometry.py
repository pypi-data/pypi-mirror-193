"""
(Eventually to be defined as) a supertype of GeoShape designed to accommodate definitions from Geo-Spatial best practices.

https://schema.org/GeospatialGeometry
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GeospatialGeometryInheritedProperties(TypedDict):
    """(Eventually to be defined as) a supertype of GeoShape designed to accommodate definitions from Geo-Spatial best practices.

    References:
        https://schema.org/GeospatialGeometry
    Note:
        Model Depth 3
    Attributes:
    """


class GeospatialGeometryProperties(TypedDict):
    """(Eventually to be defined as) a supertype of GeoShape designed to accommodate definitions from Geo-Spatial best practices.

    References:
        https://schema.org/GeospatialGeometry
    Note:
        Model Depth 3
    Attributes:
        geoCovers: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a covering geometry to a covered geometry. "Every point of b is a point of (the interior or boundary of) a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoWithin: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a geometry to one that contains it, i.e. it is inside (i.e. within) its interior. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoOverlaps: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a geometry to another that geospatially overlaps it, i.e. they have some but not all points in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoEquals: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents spatial relations in which two geometries (or the places they represent) are topologically equal, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM). "Two geometries are topologically equal if their interiors intersect and no part of the interior or boundary of one geometry intersects the exterior of the other" (a symmetric relationship).
        geoCrosses: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a geometry to another that crosses it: "a crosses b: they have some but not all interior points in common, and the dimension of the intersection is less than that of at least one of them". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoDisjoint: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents spatial relations in which two geometries (or the places they represent) are topologically disjoint: "they have no point in common. They form a set of disconnected geometries." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)
        geoIntersects: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents spatial relations in which two geometries (or the places they represent) have at least one point in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoTouches: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents spatial relations in which two geometries (or the places they represent) touch: "they have at least one boundary point in common, but no interior points." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)
        geoCoveredBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a geometry to another that covers it. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoContains: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a containing geometry to a contained geometry. "a contains b iff no points of b lie in the exterior of a, and at least one point of the interior of b lies in the interior of a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
    """

    geoCovers: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoWithin: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoOverlaps: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoEquals: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoCrosses: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoDisjoint: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoIntersects: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoTouches: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoCoveredBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoContains: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class GeospatialGeometryAllProperties(
    GeospatialGeometryInheritedProperties, GeospatialGeometryProperties, TypedDict
):
    pass


class GeospatialGeometryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GeospatialGeometry", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"geoCovers": {"exclude": True}}
        fields = {"geoWithin": {"exclude": True}}
        fields = {"geoOverlaps": {"exclude": True}}
        fields = {"geoEquals": {"exclude": True}}
        fields = {"geoCrosses": {"exclude": True}}
        fields = {"geoDisjoint": {"exclude": True}}
        fields = {"geoIntersects": {"exclude": True}}
        fields = {"geoTouches": {"exclude": True}}
        fields = {"geoCoveredBy": {"exclude": True}}
        fields = {"geoContains": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        GeospatialGeometryProperties,
        GeospatialGeometryInheritedProperties,
        GeospatialGeometryAllProperties,
    ] = GeospatialGeometryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GeospatialGeometry"
    return model


GeospatialGeometry = create_schema_org_model()


def create_geospatialgeometry_model(
    model: Union[
        GeospatialGeometryProperties,
        GeospatialGeometryInheritedProperties,
        GeospatialGeometryAllProperties,
    ]
):
    _type = deepcopy(GeospatialGeometryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GeospatialGeometryAllProperties):
    pydantic_type = create_geospatialgeometry_model(model=model)
    return pydantic_type(model).schema_json()
