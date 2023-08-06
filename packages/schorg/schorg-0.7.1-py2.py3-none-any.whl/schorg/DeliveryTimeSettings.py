"""
A DeliveryTimeSettings represents re-usable pieces of shipping information, relating to timing. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished (and identified/referenced) by their different values for [[transitTimeLabel]].

https://schema.org/DeliveryTimeSettings
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DeliveryTimeSettingsInheritedProperties(TypedDict):
    """A DeliveryTimeSettings represents re-usable pieces of shipping information, relating to timing. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished (and identified/referenced) by their different values for [[transitTimeLabel]].

    References:
        https://schema.org/DeliveryTimeSettings
    Note:
        Model Depth 4
    Attributes:
    """

    


class DeliveryTimeSettingsProperties(TypedDict):
    """A DeliveryTimeSettings represents re-usable pieces of shipping information, relating to timing. It is designed for publication on an URL that may be referenced via the [[shippingSettingsLink]] property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished (and identified/referenced) by their different values for [[transitTimeLabel]].

    References:
        https://schema.org/DeliveryTimeSettings
    Note:
        Model Depth 4
    Attributes:
        shippingDestination: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): indicates (possibly multiple) shipping destinations. These can be defined in several ways, e.g. postalCode ranges.
        deliveryTime: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The total delay between the receipt of the order and the goods reaching the final customer.
        transitTimeLabel: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Label to match an [[OfferShippingDetails]] with a [[DeliveryTimeSettings]] (within the context of a [[shippingSettingsLink]] cross-reference).
        isUnlabelledFallback: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): This can be marked 'true' to indicate that some published [[DeliveryTimeSettings]] or [[ShippingRateSettings]] are intended to apply to all [[OfferShippingDetails]] published by the same merchant, when referenced by a [[shippingSettingsLink]] in those settings. It is not meaningful to use a 'true' value for this property alongside a transitTimeLabel (for [[DeliveryTimeSettings]]) or shippingLabel (for [[ShippingRateSettings]]), since this property is for use with unlabelled settings.
    """

    shippingDestination: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    deliveryTime: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    transitTimeLabel: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    isUnlabelledFallback: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    


class AllProperties(DeliveryTimeSettingsInheritedProperties , DeliveryTimeSettingsProperties, TypedDict):
    pass


class DeliveryTimeSettingsBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DeliveryTimeSettings",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'shippingDestination': {'exclude': True}}
        fields = {'deliveryTime': {'exclude': True}}
        fields = {'transitTimeLabel': {'exclude': True}}
        fields = {'isUnlabelledFallback': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DeliveryTimeSettingsProperties, DeliveryTimeSettingsInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DeliveryTimeSettings"
    return model
    

DeliveryTimeSettings = create_schema_org_model()


def create_deliverytimesettings_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_deliverytimesettings_model(model=model)
    return pydantic_type(model).schema_json()


