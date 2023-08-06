"""
A DatedMoneySpecification represents monetary values with optional start and end dates. For example, this could represent an employee's salary over a specific period of time. __Note:__ This type has been superseded by [[MonetaryAmount]], use of that type is recommended.

https://schema.org/DatedMoneySpecification
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DatedMoneySpecificationInheritedProperties(TypedDict):
    """A DatedMoneySpecification represents monetary values with optional start and end dates. For example, this could represent an employee's salary over a specific period of time. __Note:__ This type has been superseded by [[MonetaryAmount]], use of that type is recommended.

    References:
        https://schema.org/DatedMoneySpecification
    Note:
        Model Depth 4
    Attributes:
    """


class DatedMoneySpecificationProperties(TypedDict):
    """A DatedMoneySpecification represents monetary values with optional start and end dates. For example, this could represent an employee's salary over a specific period of time. __Note:__ This type has been superseded by [[MonetaryAmount]], use of that type is recommended.

    References:
        https://schema.org/DatedMoneySpecification
    Note:
        Model Depth 4
    Attributes:
        currency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency in which the monetary amount is expressed.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        amount: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The amount of money.
        startDate: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    currency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    amount: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    startDate: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    endDate: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]


class DatedMoneySpecificationAllProperties(
    DatedMoneySpecificationInheritedProperties,
    DatedMoneySpecificationProperties,
    TypedDict,
):
    pass


class DatedMoneySpecificationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DatedMoneySpecification", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"currency": {"exclude": True}}
        fields = {"amount": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DatedMoneySpecificationProperties,
        DatedMoneySpecificationInheritedProperties,
        DatedMoneySpecificationAllProperties,
    ] = DatedMoneySpecificationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DatedMoneySpecification"
    return model


DatedMoneySpecification = create_schema_org_model()


def create_datedmoneyspecification_model(
    model: Union[
        DatedMoneySpecificationProperties,
        DatedMoneySpecificationInheritedProperties,
        DatedMoneySpecificationAllProperties,
    ]
):
    _type = deepcopy(DatedMoneySpecificationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DatedMoneySpecificationAllProperties):
    pydantic_type = create_datedmoneyspecification_model(model=model)
    return pydantic_type(model).schema_json()
