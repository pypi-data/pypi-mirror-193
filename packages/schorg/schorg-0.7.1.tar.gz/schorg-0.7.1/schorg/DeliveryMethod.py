"""
A delivery method is a standardized procedure for transferring the product or service to the destination of fulfillment chosen by the customer. Delivery methods are characterized by the means of transportation used, and by the organization or group that is the contracting party for the sending organization or person.Commonly used values:* http://purl.org/goodrelations/v1#DeliveryModeDirectDownload* http://purl.org/goodrelations/v1#DeliveryModeFreight* http://purl.org/goodrelations/v1#DeliveryModeMail* http://purl.org/goodrelations/v1#DeliveryModeOwnFleet* http://purl.org/goodrelations/v1#DeliveryModePickUp* http://purl.org/goodrelations/v1#DHL* http://purl.org/goodrelations/v1#FederalExpress* http://purl.org/goodrelations/v1#UPS        

https://schema.org/DeliveryMethod
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DeliveryMethodInheritedProperties(TypedDict):
    """A delivery method is a standardized procedure for transferring the product or service to the destination of fulfillment chosen by the customer. Delivery methods are characterized by the means of transportation used, and by the organization or group that is the contracting party for the sending organization or person.Commonly used values:* http://purl.org/goodrelations/v1#DeliveryModeDirectDownload* http://purl.org/goodrelations/v1#DeliveryModeFreight* http://purl.org/goodrelations/v1#DeliveryModeMail* http://purl.org/goodrelations/v1#DeliveryModeOwnFleet* http://purl.org/goodrelations/v1#DeliveryModePickUp* http://purl.org/goodrelations/v1#DHL* http://purl.org/goodrelations/v1#FederalExpress* http://purl.org/goodrelations/v1#UPS        

    References:
        https://schema.org/DeliveryMethod
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class DeliveryMethodProperties(TypedDict):
    """A delivery method is a standardized procedure for transferring the product or service to the destination of fulfillment chosen by the customer. Delivery methods are characterized by the means of transportation used, and by the organization or group that is the contracting party for the sending organization or person.Commonly used values:* http://purl.org/goodrelations/v1#DeliveryModeDirectDownload* http://purl.org/goodrelations/v1#DeliveryModeFreight* http://purl.org/goodrelations/v1#DeliveryModeMail* http://purl.org/goodrelations/v1#DeliveryModeOwnFleet* http://purl.org/goodrelations/v1#DeliveryModePickUp* http://purl.org/goodrelations/v1#DHL* http://purl.org/goodrelations/v1#FederalExpress* http://purl.org/goodrelations/v1#UPS        

    References:
        https://schema.org/DeliveryMethod
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(DeliveryMethodInheritedProperties , DeliveryMethodProperties, TypedDict):
    pass


class DeliveryMethodBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DeliveryMethod",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DeliveryMethodProperties, DeliveryMethodInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DeliveryMethod"
    return model
    

DeliveryMethod = create_schema_org_model()


def create_deliverymethod_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_deliverymethod_model(model=model)
    return pydantic_type(model).schema_json()


