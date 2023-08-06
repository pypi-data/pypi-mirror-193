"""
A monetary grant.

https://schema.org/MonetaryGrant
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MonetaryGrantInheritedProperties(TypedDict):
    """A monetary grant.

    References:
        https://schema.org/MonetaryGrant
    Note:
        Model Depth 4
    Attributes:
        fundedItem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates something directly or indirectly funded or sponsored through a [[Grant]]. See also [[ownershipFundingInfo]].
        funder: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person or organization that supports (sponsors) something through some kind of financial contribution.
        sponsor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
    """

    fundedItem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    funder: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sponsor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class MonetaryGrantProperties(TypedDict):
    """A monetary grant.

    References:
        https://schema.org/MonetaryGrant
    Note:
        Model Depth 4
    Attributes:
        funder: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person or organization that supports (sponsors) something through some kind of financial contribution.
        amount: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The amount of money.
    """

    funder: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    amount: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]


class MonetaryGrantAllProperties(
    MonetaryGrantInheritedProperties, MonetaryGrantProperties, TypedDict
):
    pass


class MonetaryGrantBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MonetaryGrant", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"fundedItem": {"exclude": True}}
        fields = {"funder": {"exclude": True}}
        fields = {"sponsor": {"exclude": True}}
        fields = {"funder": {"exclude": True}}
        fields = {"amount": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MonetaryGrantProperties,
        MonetaryGrantInheritedProperties,
        MonetaryGrantAllProperties,
    ] = MonetaryGrantAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MonetaryGrant"
    return model


MonetaryGrant = create_schema_org_model()


def create_monetarygrant_model(
    model: Union[
        MonetaryGrantProperties,
        MonetaryGrantInheritedProperties,
        MonetaryGrantAllProperties,
    ]
):
    _type = deepcopy(MonetaryGrantAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MonetaryGrantAllProperties):
    pydantic_type = create_monetarygrant_model(model=model)
    return pydantic_type(model).schema_json()
