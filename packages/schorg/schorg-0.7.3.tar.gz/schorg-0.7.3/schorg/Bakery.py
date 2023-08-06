"""
A bakery.

https://schema.org/Bakery
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BakeryInheritedProperties(TypedDict):
    """A bakery.

    References:
        https://schema.org/Bakery
    Note:
        Model Depth 5
    Attributes:
        starRating: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An official rating for a lodging business or food establishment, e.g. from national associations or standards bodies. Use the author property to indicate the rating organization, e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).
        servesCuisine: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The cuisine of the restaurant.
        acceptsReservations: (Optional[Union[List[Union[AnyUrl, str, StrictBool, SchemaOrgObj]], AnyUrl, str, StrictBool, SchemaOrgObj]]): Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean, an URL at which reservations can be made or (for backwards compatibility) the strings ```Yes``` or ```No```.
        menu: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Either the actual menu as a structured representation, as text, or a URL of the menu.
        hasMenu: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Either the actual menu as a structured representation, as text, or a URL of the menu.
    """

    starRating: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    servesCuisine: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    acceptsReservations: NotRequired[
        Union[
            List[Union[AnyUrl, str, StrictBool, SchemaOrgObj]],
            AnyUrl,
            str,
            StrictBool,
            SchemaOrgObj,
        ]
    ]
    menu: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    hasMenu: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]


class BakeryProperties(TypedDict):
    """A bakery.

    References:
        https://schema.org/Bakery
    Note:
        Model Depth 5
    Attributes:
    """


class BakeryAllProperties(BakeryInheritedProperties, BakeryProperties, TypedDict):
    pass


class BakeryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Bakery", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"starRating": {"exclude": True}}
        fields = {"servesCuisine": {"exclude": True}}
        fields = {"acceptsReservations": {"exclude": True}}
        fields = {"menu": {"exclude": True}}
        fields = {"hasMenu": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BakeryProperties, BakeryInheritedProperties, BakeryAllProperties
    ] = BakeryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Bakery"
    return model


Bakery = create_schema_org_model()


def create_bakery_model(
    model: Union[BakeryProperties, BakeryInheritedProperties, BakeryAllProperties]
):
    _type = deepcopy(BakeryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BakeryAllProperties):
    pydantic_type = create_bakery_model(model=model)
    return pydantic_type(model).schema_json()
