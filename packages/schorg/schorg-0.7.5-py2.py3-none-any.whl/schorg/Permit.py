"""
A permit issued by an organization, e.g. a parking pass.

https://schema.org/Permit
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PermitInheritedProperties(TypedDict):
    """A permit issued by an organization, e.g. a parking pass.

    References:
        https://schema.org/Permit
    Note:
        Model Depth 3
    Attributes:
    """


class PermitProperties(TypedDict):
    """A permit issued by an organization, e.g. a parking pass.

    References:
        https://schema.org/Permit
    Note:
        Model Depth 3
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


class PermitAllProperties(PermitInheritedProperties, PermitProperties, TypedDict):
    pass


class PermitBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Permit", alias="@id")
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
        PermitProperties, PermitInheritedProperties, PermitAllProperties
    ] = PermitAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Permit"
    return model


Permit = create_schema_org_model()


def create_permit_model(
    model: Union[PermitProperties, PermitInheritedProperties, PermitAllProperties]
):
    _type = deepcopy(PermitAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Permit. Please see: https://schema.org/Permit"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PermitAllProperties):
    pydantic_type = create_permit_model(model=model)
    return pydantic_type(model).schema_json()
