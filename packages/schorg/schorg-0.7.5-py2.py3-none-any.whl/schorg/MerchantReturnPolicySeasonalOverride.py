"""
A seasonal override of a return policy, for example used for holidays.

https://schema.org/MerchantReturnPolicySeasonalOverride
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MerchantReturnPolicySeasonalOverrideInheritedProperties(TypedDict):
    """A seasonal override of a return policy, for example used for holidays.

    References:
        https://schema.org/MerchantReturnPolicySeasonalOverride
    Note:
        Model Depth 3
    Attributes:
    """


class MerchantReturnPolicySeasonalOverrideProperties(TypedDict):
    """A seasonal override of a return policy, for example used for holidays.

    References:
        https://schema.org/MerchantReturnPolicySeasonalOverride
    Note:
        Model Depth 3
    Attributes:
        returnPolicyCategory: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifies an applicable return policy (from an enumeration).
        merchantReturnDays: (Optional[Union[List[Union[str, int, SchemaOrgObj, datetime, date]], str, int, SchemaOrgObj, datetime, date]]): Specifies either a fixed return date or the number of days (from the delivery date) that a product can be returned. Used when the [[returnPolicyCategory]] property is specified as [[MerchantReturnFiniteReturnWindow]].
        startDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    returnPolicyCategory: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    merchantReturnDays: NotRequired[
        Union[
            List[Union[str, int, SchemaOrgObj, datetime, date]],
            str,
            int,
            SchemaOrgObj,
            datetime,
            date,
        ]
    ]
    startDate: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    endDate: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]


class MerchantReturnPolicySeasonalOverrideAllProperties(
    MerchantReturnPolicySeasonalOverrideInheritedProperties,
    MerchantReturnPolicySeasonalOverrideProperties,
    TypedDict,
):
    pass


class MerchantReturnPolicySeasonalOverrideBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(
        default="MerchantReturnPolicySeasonalOverride", alias="@id"
    )
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"returnPolicyCategory": {"exclude": True}}
        fields = {"merchantReturnDays": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MerchantReturnPolicySeasonalOverrideProperties,
        MerchantReturnPolicySeasonalOverrideInheritedProperties,
        MerchantReturnPolicySeasonalOverrideAllProperties,
    ] = MerchantReturnPolicySeasonalOverrideAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MerchantReturnPolicySeasonalOverride"
    return model


MerchantReturnPolicySeasonalOverride = create_schema_org_model()


def create_merchantreturnpolicyseasonaloverride_model(
    model: Union[
        MerchantReturnPolicySeasonalOverrideProperties,
        MerchantReturnPolicySeasonalOverrideInheritedProperties,
        MerchantReturnPolicySeasonalOverrideAllProperties,
    ]
):
    _type = deepcopy(MerchantReturnPolicySeasonalOverrideAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MerchantReturnPolicySeasonalOverride. Please see: https://schema.org/MerchantReturnPolicySeasonalOverride"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MerchantReturnPolicySeasonalOverrideAllProperties):
    pydantic_type = create_merchantreturnpolicyseasonaloverride_model(model=model)
    return pydantic_type(model).schema_json()
