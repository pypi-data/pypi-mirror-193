"""
A set of requirements that must be fulfilled in order to perform an Action.

https://schema.org/ActionAccessSpecification
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ActionAccessSpecificationInheritedProperties(TypedDict):
    """A set of requirements that must be fulfilled in order to perform an Action.

    References:
        https://schema.org/ActionAccessSpecification
    Note:
        Model Depth 3
    Attributes:
    """


class ActionAccessSpecificationProperties(TypedDict):
    """A set of requirements that must be fulfilled in order to perform an Action.

    References:
        https://schema.org/ActionAccessSpecification
    Note:
        Model Depth 3
    Attributes:
        availabilityEnds: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The end of the availability of the product or service included in the offer.
        expectsAcceptanceOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.
        availabilityStarts: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The beginning of the availability of the product or service included in the offer.
        requiresSubscription: (Optional[Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]]): Indicates if use of the media require a subscription  (either paid or free). Allowed values are ```true``` or ```false``` (note that an earlier version had 'yes', 'no').
        eligibleRegion: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.See also [[ineligibleRegion]].
        ineligibleRegion: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.See also [[eligibleRegion]].
        category: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
    """

    availabilityEnds: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    expectsAcceptanceOf: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    availabilityStarts: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    requiresSubscription: NotRequired[
        Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]
    ]
    eligibleRegion: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    ineligibleRegion: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    category: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]


class ActionAccessSpecificationAllProperties(
    ActionAccessSpecificationInheritedProperties,
    ActionAccessSpecificationProperties,
    TypedDict,
):
    pass


class ActionAccessSpecificationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ActionAccessSpecification", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"availabilityEnds": {"exclude": True}}
        fields = {"expectsAcceptanceOf": {"exclude": True}}
        fields = {"availabilityStarts": {"exclude": True}}
        fields = {"requiresSubscription": {"exclude": True}}
        fields = {"eligibleRegion": {"exclude": True}}
        fields = {"ineligibleRegion": {"exclude": True}}
        fields = {"category": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ActionAccessSpecificationProperties,
        ActionAccessSpecificationInheritedProperties,
        ActionAccessSpecificationAllProperties,
    ] = ActionAccessSpecificationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ActionAccessSpecification"
    return model


ActionAccessSpecification = create_schema_org_model()


def create_actionaccessspecification_model(
    model: Union[
        ActionAccessSpecificationProperties,
        ActionAccessSpecificationInheritedProperties,
        ActionAccessSpecificationAllProperties,
    ]
):
    _type = deepcopy(ActionAccessSpecificationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ActionAccessSpecificationAllProperties):
    pydantic_type = create_actionaccessspecification_model(model=model)
    return pydantic_type(model).schema_json()
