"""
A seasonal override of a return policy, for example used for holidays.

https://schema.org/MerchantReturnPolicySeasonalOverride
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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
        merchantReturnDays: (Optional[Union[List[Union[datetime, int, SchemaOrgObj, str, date]], datetime, int, SchemaOrgObj, str, date]]): Specifies either a fixed return date or the number of days (from the delivery date) that a product can be returned. Used when the [[returnPolicyCategory]] property is specified as [[MerchantReturnFiniteReturnWindow]].
        startDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    returnPolicyCategory: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    merchantReturnDays: NotRequired[Union[List[Union[datetime, int, SchemaOrgObj, str, date]], datetime, int, SchemaOrgObj, str, date]]
    startDate: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    endDate: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    


class AllProperties(MerchantReturnPolicySeasonalOverrideInheritedProperties , MerchantReturnPolicySeasonalOverrideProperties, TypedDict):
    pass


class MerchantReturnPolicySeasonalOverrideBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MerchantReturnPolicySeasonalOverride",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'returnPolicyCategory': {'exclude': True}}
        fields = {'merchantReturnDays': {'exclude': True}}
        fields = {'startDate': {'exclude': True}}
        fields = {'endDate': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MerchantReturnPolicySeasonalOverrideProperties, MerchantReturnPolicySeasonalOverrideInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MerchantReturnPolicySeasonalOverride"
    return model
    

MerchantReturnPolicySeasonalOverride = create_schema_org_model()


def create_merchantreturnpolicyseasonaloverride_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_merchantreturnpolicyseasonaloverride_model(model=model)
    return pydantic_type(model).schema_json()


