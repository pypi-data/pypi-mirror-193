"""
A MerchantReturnPolicy provides information about product return policies associated with an [[Organization]], [[Product]], or [[Offer]].

https://schema.org/MerchantReturnPolicy
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MerchantReturnPolicyInheritedProperties(TypedDict):
    """A MerchantReturnPolicy provides information about product return policies associated with an [[Organization]], [[Product]], or [[Offer]].

    References:
        https://schema.org/MerchantReturnPolicy
    Note:
        Model Depth 3
    Attributes:
    """


class MerchantReturnPolicyProperties(TypedDict):
    """A MerchantReturnPolicy provides information about product return policies associated with an [[Organization]], [[Product]], or [[Offer]].

    References:
        https://schema.org/MerchantReturnPolicy
    Note:
        Model Depth 3
    Attributes:
        refundType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A refund type, from an enumerated list.
        customerRemorseReturnFees: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type of return fees if the product is returned due to customer remorse.
        additionalProperty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
        itemDefectReturnLabelSource: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The method (from an enumeration) by which the customer obtains a return shipping label for a defect product.
        inStoreReturnsOffered: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]]): Are in-store returns offered? (For more advanced return methods use the [[returnMethod]] property.)
        itemCondition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.
        restockingFee: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): Use [[MonetaryAmount]] to specify a fixed restocking fee for product returns, or use [[Number]] to specify a percentage of the product price paid by the customer.
        returnPolicyCategory: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifies an applicable return policy (from an enumeration).
        returnLabelSource: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The method (from an enumeration) by which the customer obtains a return shipping label for a product returned for any reason.
        applicableCountry: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A country where a particular merchant return policy applies to, for example the two-letter ISO 3166-1 alpha-2 country code.
        returnMethod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type of return method offered, specified from an enumeration.
        returnShippingFeesAmount: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Amount of shipping costs for product returns (for any reason). Applicable when property [[returnFees]] equals [[ReturnShippingFees]].
        itemDefectReturnShippingFeesAmount: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Amount of shipping costs for defect product returns. Applicable when property [[itemDefectReturnFees]] equals [[ReturnShippingFees]].
        returnPolicySeasonalOverride: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Seasonal override of a return policy.
        customerRemorseReturnShippingFeesAmount: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The amount of shipping costs if a product is returned due to customer remorse. Applicable when property [[customerRemorseReturnFees]] equals [[ReturnShippingFees]].
        returnFees: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type of return fees for purchased products (for any return reason).
        customerRemorseReturnLabelSource: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The method (from an enumeration) by which the customer obtains a return shipping label for a product returned due to customer remorse.
        merchantReturnLink: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Specifies a Web page or service by URL, for product returns.
        itemDefectReturnFees: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type of return fees for returns of defect products.
        merchantReturnDays: (Optional[Union[List[Union[str, int, SchemaOrgObj, datetime, date]], str, int, SchemaOrgObj, datetime, date]]): Specifies either a fixed return date or the number of days (from the delivery date) that a product can be returned. Used when the [[returnPolicyCategory]] property is specified as [[MerchantReturnFiniteReturnWindow]].
        returnPolicyCountry: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The country where the product has to be sent to for returns, for example "Ireland" using the [[name]] property of [[Country]]. You can also provide the two-letter [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1). Note that this can be different from the country where the product was originally shipped from or sent to.
    """

    refundType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    customerRemorseReturnFees: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    additionalProperty: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    itemDefectReturnLabelSource: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    inStoreReturnsOffered: NotRequired[
        Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]
    ]
    itemCondition: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    restockingFee: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    returnPolicyCategory: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    returnLabelSource: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    applicableCountry: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    returnMethod: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    returnShippingFeesAmount: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    itemDefectReturnShippingFeesAmount: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    returnPolicySeasonalOverride: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    customerRemorseReturnShippingFeesAmount: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    returnFees: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    customerRemorseReturnLabelSource: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    merchantReturnLink: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    itemDefectReturnFees: NotRequired[
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
    returnPolicyCountry: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class MerchantReturnPolicyAllProperties(
    MerchantReturnPolicyInheritedProperties, MerchantReturnPolicyProperties, TypedDict
):
    pass


class MerchantReturnPolicyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MerchantReturnPolicy", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"refundType": {"exclude": True}}
        fields = {"customerRemorseReturnFees": {"exclude": True}}
        fields = {"additionalProperty": {"exclude": True}}
        fields = {"itemDefectReturnLabelSource": {"exclude": True}}
        fields = {"inStoreReturnsOffered": {"exclude": True}}
        fields = {"itemCondition": {"exclude": True}}
        fields = {"restockingFee": {"exclude": True}}
        fields = {"returnPolicyCategory": {"exclude": True}}
        fields = {"returnLabelSource": {"exclude": True}}
        fields = {"applicableCountry": {"exclude": True}}
        fields = {"returnMethod": {"exclude": True}}
        fields = {"returnShippingFeesAmount": {"exclude": True}}
        fields = {"itemDefectReturnShippingFeesAmount": {"exclude": True}}
        fields = {"returnPolicySeasonalOverride": {"exclude": True}}
        fields = {"customerRemorseReturnShippingFeesAmount": {"exclude": True}}
        fields = {"returnFees": {"exclude": True}}
        fields = {"customerRemorseReturnLabelSource": {"exclude": True}}
        fields = {"merchantReturnLink": {"exclude": True}}
        fields = {"itemDefectReturnFees": {"exclude": True}}
        fields = {"merchantReturnDays": {"exclude": True}}
        fields = {"returnPolicyCountry": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MerchantReturnPolicyProperties,
        MerchantReturnPolicyInheritedProperties,
        MerchantReturnPolicyAllProperties,
    ] = MerchantReturnPolicyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MerchantReturnPolicy"
    return model


MerchantReturnPolicy = create_schema_org_model()


def create_merchantreturnpolicy_model(
    model: Union[
        MerchantReturnPolicyProperties,
        MerchantReturnPolicyInheritedProperties,
        MerchantReturnPolicyAllProperties,
    ]
):
    _type = deepcopy(MerchantReturnPolicyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MerchantReturnPolicy. Please see: https://schema.org/MerchantReturnPolicy"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MerchantReturnPolicyAllProperties):
    pydantic_type = create_merchantreturnpolicy_model(model=model)
    return pydantic_type(model).schema_json()
