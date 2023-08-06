"""
A ShippingRateSettings represents re-usable pieces of shipping information. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished and matched (i.e. identified/referenced) by their different values for [[shippingLabel]].

https://schema.org/ShippingRateSettings
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ShippingRateSettingsInheritedProperties(TypedDict):
    """A ShippingRateSettings represents re-usable pieces of shipping information. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished and matched (i.e. identified/referenced) by their different values for [[shippingLabel]].

    References:
        https://schema.org/ShippingRateSettings
    Note:
        Model Depth 4
    Attributes:
    """

    


class ShippingRateSettingsProperties(TypedDict):
    """A ShippingRateSettings represents re-usable pieces of shipping information. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished and matched (i.e. identified/referenced) by their different values for [[shippingLabel]].

    References:
        https://schema.org/ShippingRateSettings
    Note:
        Model Depth 4
    Attributes:
        shippingDestination: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): indicates (possibly multiple) shipping destinations. These can be defined in several ways, e.g. postalCode ranges.
        shippingLabel: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Label to match an [[OfferShippingDetails]] with a [[ShippingRateSettings]] (within the context of a [[shippingSettingsLink]] cross-reference).
        doesNotShip: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates when shipping to a particular [[shippingDestination]] is not available.
        freeShippingThreshold: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A monetary value above (or at) which the shipping rate becomes free. Intended to be used via an [[OfferShippingDetails]] with [[shippingSettingsLink]] matching this [[ShippingRateSettings]].
        shippingRate: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The shipping rate is the cost of shipping to the specified destination. Typically, the maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate.
        isUnlabelledFallback: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): This can be marked 'true' to indicate that some published [[DeliveryTimeSettings]] or [[ShippingRateSettings]] are intended to apply to all [[OfferShippingDetails]] published by the same merchant, when referenced by a [[shippingSettingsLink]] in those settings. It is not meaningful to use a 'true' value for this property alongside a transitTimeLabel (for [[DeliveryTimeSettings]]) or shippingLabel (for [[ShippingRateSettings]]), since this property is for use with unlabelled settings.
    """

    shippingDestination: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    shippingLabel: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    doesNotShip: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    freeShippingThreshold: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    shippingRate: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isUnlabelledFallback: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    


class AllProperties(ShippingRateSettingsInheritedProperties , ShippingRateSettingsProperties, TypedDict):
    pass


class ShippingRateSettingsBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ShippingRateSettings",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'shippingDestination': {'exclude': True}}
        fields = {'shippingLabel': {'exclude': True}}
        fields = {'doesNotShip': {'exclude': True}}
        fields = {'freeShippingThreshold': {'exclude': True}}
        fields = {'shippingRate': {'exclude': True}}
        fields = {'isUnlabelledFallback': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ShippingRateSettingsProperties, ShippingRateSettingsInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ShippingRateSettings"
    return model
    

ShippingRateSettings = create_schema_org_model()


def create_shippingratesettings_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_shippingratesettings_model(model=model)
    return pydantic_type(model).schema_json()


