"""
A bar or pub.

https://schema.org/BarOrPub
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BarOrPubInheritedProperties(TypedDict):
    """A bar or pub.

    References:
        https://schema.org/BarOrPub
    Note:
        Model Depth 5
    Attributes:
        starRating: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An official rating for a lodging business or food establishment, e.g. from national associations or standards bodies. Use the author property to indicate the rating organization, e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).
        servesCuisine: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The cuisine of the restaurant.
        acceptsReservations: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str, StrictBool]], AnyUrl, SchemaOrgObj, str, StrictBool]]): Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean, an URL at which reservations can be made or (for backwards compatibility) the strings ```Yes``` or ```No```.
        menu: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Either the actual menu as a structured representation, as text, or a URL of the menu.
        hasMenu: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Either the actual menu as a structured representation, as text, or a URL of the menu.
    """

    starRating: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    servesCuisine: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    acceptsReservations: NotRequired[
        Union[
            List[Union[AnyUrl, SchemaOrgObj, str, StrictBool]],
            AnyUrl,
            SchemaOrgObj,
            str,
            StrictBool,
        ]
    ]
    menu: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    hasMenu: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]


class BarOrPubProperties(TypedDict):
    """A bar or pub.

    References:
        https://schema.org/BarOrPub
    Note:
        Model Depth 5
    Attributes:
    """


class BarOrPubAllProperties(BarOrPubInheritedProperties, BarOrPubProperties, TypedDict):
    pass


class BarOrPubBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BarOrPub", alias="@id")
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
        BarOrPubProperties, BarOrPubInheritedProperties, BarOrPubAllProperties
    ] = BarOrPubAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BarOrPub"
    return model


BarOrPub = create_schema_org_model()


def create_barorpub_model(
    model: Union[BarOrPubProperties, BarOrPubInheritedProperties, BarOrPubAllProperties]
):
    _type = deepcopy(BarOrPubAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of BarOrPubAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BarOrPubAllProperties):
    pydantic_type = create_barorpub_model(model=model)
    return pydantic_type(model).schema_json()
