"""
A structured value providing information about the opening hours of a place or a certain service inside a place.The place is __open__ if the [[opens]] property is specified, and __closed__ otherwise.If the value for the [[closes]] property is less than the value for the [[opens]] property then the hour range is assumed to span over the next day.      

https://schema.org/OpeningHoursSpecification
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OpeningHoursSpecificationInheritedProperties(TypedDict):
    """A structured value providing information about the opening hours of a place or a certain service inside a place.The place is __open__ if the [[opens]] property is specified, and __closed__ otherwise.If the value for the [[closes]] property is less than the value for the [[opens]] property then the hour range is assumed to span over the next day.

    References:
        https://schema.org/OpeningHoursSpecification
    Note:
        Model Depth 4
    Attributes:
    """


class OpeningHoursSpecificationProperties(TypedDict):
    """A structured value providing information about the opening hours of a place or a certain service inside a place.The place is __open__ if the [[opens]] property is specified, and __closed__ otherwise.If the value for the [[closes]] property is less than the value for the [[opens]] property then the hour range is assumed to span over the next day.

    References:
        https://schema.org/OpeningHoursSpecification
    Note:
        Model Depth 4
    Attributes:
        closes: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The closing hour of the place or service on the given day(s) of the week.
        validThrough: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        opens: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The opening hour of the place or service on the given day(s) of the week.
        validFrom: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The date when the item becomes valid.
        dayOfWeek: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The day of the week for which these opening hours are valid.
    """

    closes: NotRequired[
        Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]
    ]
    validThrough: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    opens: NotRequired[
        Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]
    ]
    validFrom: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    dayOfWeek: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class OpeningHoursSpecificationAllProperties(
    OpeningHoursSpecificationInheritedProperties,
    OpeningHoursSpecificationProperties,
    TypedDict,
):
    pass


class OpeningHoursSpecificationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OpeningHoursSpecification", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"closes": {"exclude": True}}
        fields = {"validThrough": {"exclude": True}}
        fields = {"opens": {"exclude": True}}
        fields = {"validFrom": {"exclude": True}}
        fields = {"dayOfWeek": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        OpeningHoursSpecificationProperties,
        OpeningHoursSpecificationInheritedProperties,
        OpeningHoursSpecificationAllProperties,
    ] = OpeningHoursSpecificationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OpeningHoursSpecification"
    return model


OpeningHoursSpecification = create_schema_org_model()


def create_openinghoursspecification_model(
    model: Union[
        OpeningHoursSpecificationProperties,
        OpeningHoursSpecificationInheritedProperties,
        OpeningHoursSpecificationAllProperties,
    ]
):
    _type = deepcopy(OpeningHoursSpecificationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OpeningHoursSpecificationAllProperties):
    pydantic_type = create_openinghoursspecification_model(model=model)
    return pydantic_type(model).schema_json()
