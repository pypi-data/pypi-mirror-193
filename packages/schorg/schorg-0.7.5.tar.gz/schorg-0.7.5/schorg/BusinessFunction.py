"""
The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the organization or business person through the offer. Typical are sell, rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering / construction, or installation. Proprietary specifications of access rights are also instances of this class.Commonly used values:* http://purl.org/goodrelations/v1#ConstructionInstallation* http://purl.org/goodrelations/v1#Dispose* http://purl.org/goodrelations/v1#LeaseOut* http://purl.org/goodrelations/v1#Maintain* http://purl.org/goodrelations/v1#ProvideService* http://purl.org/goodrelations/v1#Repair* http://purl.org/goodrelations/v1#Sell* http://purl.org/goodrelations/v1#Buy        

https://schema.org/BusinessFunction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BusinessFunctionInheritedProperties(TypedDict):
    """The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the organization or business person through the offer. Typical are sell, rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering / construction, or installation. Proprietary specifications of access rights are also instances of this class.Commonly used values:* http://purl.org/goodrelations/v1#ConstructionInstallation* http://purl.org/goodrelations/v1#Dispose* http://purl.org/goodrelations/v1#LeaseOut* http://purl.org/goodrelations/v1#Maintain* http://purl.org/goodrelations/v1#ProvideService* http://purl.org/goodrelations/v1#Repair* http://purl.org/goodrelations/v1#Sell* http://purl.org/goodrelations/v1#Buy

    References:
        https://schema.org/BusinessFunction
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class BusinessFunctionProperties(TypedDict):
    """The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the organization or business person through the offer. Typical are sell, rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering / construction, or installation. Proprietary specifications of access rights are also instances of this class.Commonly used values:* http://purl.org/goodrelations/v1#ConstructionInstallation* http://purl.org/goodrelations/v1#Dispose* http://purl.org/goodrelations/v1#LeaseOut* http://purl.org/goodrelations/v1#Maintain* http://purl.org/goodrelations/v1#ProvideService* http://purl.org/goodrelations/v1#Repair* http://purl.org/goodrelations/v1#Sell* http://purl.org/goodrelations/v1#Buy

    References:
        https://schema.org/BusinessFunction
    Note:
        Model Depth 4
    Attributes:
    """


class BusinessFunctionAllProperties(
    BusinessFunctionInheritedProperties, BusinessFunctionProperties, TypedDict
):
    pass


class BusinessFunctionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BusinessFunction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BusinessFunctionProperties,
        BusinessFunctionInheritedProperties,
        BusinessFunctionAllProperties,
    ] = BusinessFunctionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BusinessFunction"
    return model


BusinessFunction = create_schema_org_model()


def create_businessfunction_model(
    model: Union[
        BusinessFunctionProperties,
        BusinessFunctionInheritedProperties,
        BusinessFunctionAllProperties,
    ]
):
    _type = deepcopy(BusinessFunctionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BusinessFunction. Please see: https://schema.org/BusinessFunction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BusinessFunctionAllProperties):
    pydantic_type = create_businessfunction_model(model=model)
    return pydantic_type(model).schema_json()
