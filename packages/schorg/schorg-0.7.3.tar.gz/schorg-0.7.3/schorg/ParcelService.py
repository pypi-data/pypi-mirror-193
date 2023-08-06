"""
A private parcel service as the delivery mode available for a certain offer.Commonly used values:* http://purl.org/goodrelations/v1#DHL* http://purl.org/goodrelations/v1#FederalExpress* http://purl.org/goodrelations/v1#UPS      

https://schema.org/ParcelService
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ParcelServiceInheritedProperties(TypedDict):
    """A private parcel service as the delivery mode available for a certain offer.Commonly used values:* http://purl.org/goodrelations/v1#DHL* http://purl.org/goodrelations/v1#FederalExpress* http://purl.org/goodrelations/v1#UPS

    References:
        https://schema.org/ParcelService
    Note:
        Model Depth 5
    Attributes:
    """


class ParcelServiceProperties(TypedDict):
    """A private parcel service as the delivery mode available for a certain offer.Commonly used values:* http://purl.org/goodrelations/v1#DHL* http://purl.org/goodrelations/v1#FederalExpress* http://purl.org/goodrelations/v1#UPS

    References:
        https://schema.org/ParcelService
    Note:
        Model Depth 5
    Attributes:
    """


class ParcelServiceAllProperties(
    ParcelServiceInheritedProperties, ParcelServiceProperties, TypedDict
):
    pass


class ParcelServiceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ParcelService", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ParcelServiceProperties,
        ParcelServiceInheritedProperties,
        ParcelServiceAllProperties,
    ] = ParcelServiceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ParcelService"
    return model


ParcelService = create_schema_org_model()


def create_parcelservice_model(
    model: Union[
        ParcelServiceProperties,
        ParcelServiceInheritedProperties,
        ParcelServiceAllProperties,
    ]
):
    _type = deepcopy(ParcelServiceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ParcelServiceAllProperties):
    pydantic_type = create_parcelservice_model(model=model)
    return pydantic_type(model).schema_json()
