"""
The mailing address.

https://schema.org/PostalAddress
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PostalAddressInheritedProperties(TypedDict):
    """The mailing address.

    References:
        https://schema.org/PostalAddress
    Note:
        Model Depth 5
    Attributes:
        serviceArea: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area where the service is provided.
        availableLanguage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].
        productSupported: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").
        areaServed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area where a service or offered item is provided.
        contactOption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).
        email: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Email address.
        contactType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.
        hoursAvailable: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The hours during which this service or contact is available.
        faxNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The fax number.
        telephone: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The telephone number.
    """

    serviceArea: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    availableLanguage: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    productSupported: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    areaServed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    contactOption: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    email: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    contactType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hoursAvailable: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    faxNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    telephone: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class PostalAddressProperties(TypedDict):
    """The mailing address.

    References:
        https://schema.org/PostalAddress
    Note:
        Model Depth 5
    Attributes:
        addressLocality: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The locality in which the street address is, and which is in the region. For example, Mountain View.
        postOfficeBoxNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The post office box number for PO box addresses.
        streetAddress: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The street address. For example, 1600 Amphitheatre Pkwy.
        addressCountry: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1).
        postalCode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The postal code. For example, 94043.
        addressRegion: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The region in which the locality is, and which is in the country. For example, California or another appropriate first-level [Administrative division](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country).
    """

    addressLocality: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    postOfficeBoxNumber: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    streetAddress: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    addressCountry: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    postalCode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    addressRegion: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class PostalAddressAllProperties(
    PostalAddressInheritedProperties, PostalAddressProperties, TypedDict
):
    pass


class PostalAddressBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PostalAddress", alias="@id")
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
        fields = {"addressLocality": {"exclude": True}}
        fields = {"postOfficeBoxNumber": {"exclude": True}}
        fields = {"streetAddress": {"exclude": True}}
        fields = {"addressCountry": {"exclude": True}}
        fields = {"postalCode": {"exclude": True}}
        fields = {"addressRegion": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PostalAddressProperties,
        PostalAddressInheritedProperties,
        PostalAddressAllProperties,
    ] = PostalAddressAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PostalAddress"
    return model


PostalAddress = create_schema_org_model()


def create_postaladdress_model(
    model: Union[
        PostalAddressProperties,
        PostalAddressInheritedProperties,
        PostalAddressAllProperties,
    ]
):
    _type = deepcopy(PostalAddressAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PostalAddressAllProperties):
    pydantic_type = create_postaladdress_model(model=model)
    return pydantic_type(model).schema_json()
