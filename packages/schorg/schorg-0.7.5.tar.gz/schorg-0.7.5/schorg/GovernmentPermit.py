"""
A permit issued by a government agency.

https://schema.org/GovernmentPermit
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GovernmentPermitInheritedProperties(TypedDict):
    """A permit issued by a government agency.

    References:
        https://schema.org/GovernmentPermit
    Note:
        Model Depth 4
    Attributes:
        permitAudience: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The target audience for this permit.
        issuedBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The organization issuing the ticket or permit.
        validUntil: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): The date when the item is no longer valid.
        validFor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The duration of validity of a permit or similar thing.
        validIn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area where a permit or similar thing is valid.
        validFrom: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The date when the item becomes valid.
        issuedThrough: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The service through which the permit was granted.
    """

    permitAudience: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    issuedBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    validUntil: NotRequired[
        Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]
    ]
    validFor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    validIn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    validFrom: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    issuedThrough: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class GovernmentPermitProperties(TypedDict):
    """A permit issued by a government agency.

    References:
        https://schema.org/GovernmentPermit
    Note:
        Model Depth 4
    Attributes:
    """


class GovernmentPermitAllProperties(
    GovernmentPermitInheritedProperties, GovernmentPermitProperties, TypedDict
):
    pass


class GovernmentPermitBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GovernmentPermit", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"permitAudience": {"exclude": True}}
        fields = {"issuedBy": {"exclude": True}}
        fields = {"validUntil": {"exclude": True}}
        fields = {"validFor": {"exclude": True}}
        fields = {"validIn": {"exclude": True}}
        fields = {"validFrom": {"exclude": True}}
        fields = {"issuedThrough": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        GovernmentPermitProperties,
        GovernmentPermitInheritedProperties,
        GovernmentPermitAllProperties,
    ] = GovernmentPermitAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GovernmentPermit"
    return model


GovernmentPermit = create_schema_org_model()


def create_governmentpermit_model(
    model: Union[
        GovernmentPermitProperties,
        GovernmentPermitInheritedProperties,
        GovernmentPermitAllProperties,
    ]
):
    _type = deepcopy(GovernmentPermitAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of GovernmentPermit. Please see: https://schema.org/GovernmentPermit"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: GovernmentPermitAllProperties):
    pydantic_type = create_governmentpermit_model(model=model)
    return pydantic_type(model).schema_json()
