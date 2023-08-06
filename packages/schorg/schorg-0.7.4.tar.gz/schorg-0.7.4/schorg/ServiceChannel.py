"""
A means for accessing a service, e.g. a government office location, web site, or phone number.

https://schema.org/ServiceChannel
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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
        servicePhone: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The phone number to use to access the service.
        availableLanguage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].
        serviceUrl: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The website to access the service.
        processingTime: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Estimated processing time for the service using this channel.
        servicePostalAddress: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The address for accessing the service by mail.
        providesService: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The service provided by this channel.
        serviceSmsNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The number to access the service by text message.
        serviceLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The location (e.g. civic structure, local business, etc.) where a person can go to access the service.
    """

    servicePhone: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    availableLanguage: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    serviceUrl: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    processingTime: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    servicePostalAddress: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    providesService: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    serviceSmsNumber: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    serviceLocation: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class ServiceChannelAllProperties(
    ServiceChannelInheritedProperties, ServiceChannelProperties, TypedDict
):
    pass


class ServiceChannelBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ServiceChannel", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"servicePhone": {"exclude": True}}
        fields = {"availableLanguage": {"exclude": True}}
        fields = {"serviceUrl": {"exclude": True}}
        fields = {"processingTime": {"exclude": True}}
        fields = {"servicePostalAddress": {"exclude": True}}
        fields = {"providesService": {"exclude": True}}
        fields = {"serviceSmsNumber": {"exclude": True}}
        fields = {"serviceLocation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ServiceChannelProperties,
        ServiceChannelInheritedProperties,
        ServiceChannelAllProperties,
    ] = ServiceChannelAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ServiceChannel"
    return model


ServiceChannel = create_schema_org_model()


def create_servicechannel_model(
    model: Union[
        ServiceChannelProperties,
        ServiceChannelInheritedProperties,
        ServiceChannelAllProperties,
    ]
):
    _type = deepcopy(ServiceChannelAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ServiceChannelAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ServiceChannelAllProperties):
    pydantic_type = create_servicechannel_model(model=model)
    return pydantic_type(model).schema_json()
