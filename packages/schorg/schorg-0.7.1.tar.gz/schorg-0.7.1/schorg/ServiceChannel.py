"""
A means for accessing a service, e.g. a government office location, web site, or phone number.

https://schema.org/ServiceChannel
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ServiceChannelInheritedProperties(TypedDict):
    """A means for accessing a service, e.g. a government office location, web site, or phone number.

    References:
        https://schema.org/ServiceChannel
    Note:
        Model Depth 3
    Attributes:
    """

    


class ServiceChannelProperties(TypedDict):
    """A means for accessing a service, e.g. a government office location, web site, or phone number.

    References:
        https://schema.org/ServiceChannel
    Note:
        Model Depth 3
    Attributes:
        servicePhone: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The phone number to use to access the service.
        availableLanguage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].
        serviceUrl: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The website to access the service.
        processingTime: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Estimated processing time for the service using this channel.
        servicePostalAddress: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The address for accessing the service by mail.
        providesService: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The service provided by this channel.
        serviceSmsNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number to access the service by text message.
        serviceLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The location (e.g. civic structure, local business, etc.) where a person can go to access the service.
    """

    servicePhone: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    availableLanguage: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    serviceUrl: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    processingTime: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    servicePostalAddress: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    providesService: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    serviceSmsNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    serviceLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(ServiceChannelInheritedProperties , ServiceChannelProperties, TypedDict):
    pass


class ServiceChannelBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ServiceChannel",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'servicePhone': {'exclude': True}}
        fields = {'availableLanguage': {'exclude': True}}
        fields = {'serviceUrl': {'exclude': True}}
        fields = {'processingTime': {'exclude': True}}
        fields = {'servicePostalAddress': {'exclude': True}}
        fields = {'providesService': {'exclude': True}}
        fields = {'serviceSmsNumber': {'exclude': True}}
        fields = {'serviceLocation': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ServiceChannelProperties, ServiceChannelInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ServiceChannel"
    return model
    

ServiceChannel = create_schema_org_model()


def create_servicechannel_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_servicechannel_model(model=model)
    return pydantic_type(model).schema_json()


