"""
A contact point&#x2014;for example, a Customer Complaints department.

https://schema.org/ContactPoint
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ContactPointInheritedProperties(TypedDict):
    """A contact point&#x2014;for example, a Customer Complaints department.

    References:
        https://schema.org/ContactPoint
    Note:
        Model Depth 4
    Attributes:
    """


class ContactPointProperties(TypedDict):
    """A contact point&#x2014;for example, a Customer Complaints department.

    References:
        https://schema.org/ContactPoint
    Note:
        Model Depth 4
    Attributes:
        serviceArea: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The geographic area where the service is provided.
        availableLanguage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].
        productSupported: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").
        areaServed: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The geographic area where a service or offered item is provided.
        contactOption: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).
        email: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Email address.
        contactType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.
        hoursAvailable: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The hours during which this service or contact is available.
        faxNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The fax number.
        telephone: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The telephone number.
    """

    serviceArea: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    availableLanguage: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    productSupported: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    areaServed: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    contactOption: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    email: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    contactType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    hoursAvailable: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    faxNumber: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    telephone: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class ContactPointAllProperties(
    ContactPointInheritedProperties, ContactPointProperties, TypedDict
):
    pass


class ContactPointBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ContactPoint", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"serviceArea": {"exclude": True}}
        fields = {"availableLanguage": {"exclude": True}}
        fields = {"productSupported": {"exclude": True}}
        fields = {"areaServed": {"exclude": True}}
        fields = {"contactOption": {"exclude": True}}
        fields = {"email": {"exclude": True}}
        fields = {"contactType": {"exclude": True}}
        fields = {"hoursAvailable": {"exclude": True}}
        fields = {"faxNumber": {"exclude": True}}
        fields = {"telephone": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ContactPointProperties,
        ContactPointInheritedProperties,
        ContactPointAllProperties,
    ] = ContactPointAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ContactPoint"
    return model


ContactPoint = create_schema_org_model()


def create_contactpoint_model(
    model: Union[
        ContactPointProperties,
        ContactPointInheritedProperties,
        ContactPointAllProperties,
    ]
):
    _type = deepcopy(ContactPointAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ContactPointAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ContactPointAllProperties):
    pydantic_type = create_contactpoint_model(model=model)
    return pydantic_type(model).schema_json()
