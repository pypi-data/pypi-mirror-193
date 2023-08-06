"""
A structured value providing information about when a certain organization or person owned a certain product.

https://schema.org/OwnershipInfo
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OwnershipInfoInheritedProperties(TypedDict):
    """A structured value providing information about when a certain organization or person owned a certain product.

    References:
        https://schema.org/OwnershipInfo
    Note:
        Model Depth 4
    Attributes:
    """


class OwnershipInfoProperties(TypedDict):
    """A structured value providing information about when a certain organization or person owned a certain product.

    References:
        https://schema.org/OwnershipInfo
    Note:
        Model Depth 4
    Attributes:
        ownedThrough: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The date and time of giving up ownership on the product.
        ownedFrom: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The date and time of obtaining the product.
        acquiredFrom: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The organization or person from which the product was acquired.
        typeOfGood: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The product that this structured value is referring to.
    """

    ownedThrough: NotRequired[
        Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]
    ]
    ownedFrom: NotRequired[
        Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]
    ]
    acquiredFrom: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    typeOfGood: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class OwnershipInfoAllProperties(
    OwnershipInfoInheritedProperties, OwnershipInfoProperties, TypedDict
):
    pass


class OwnershipInfoBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OwnershipInfo", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"ownedThrough": {"exclude": True}}
        fields = {"ownedFrom": {"exclude": True}}
        fields = {"acquiredFrom": {"exclude": True}}
        fields = {"typeOfGood": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        OwnershipInfoProperties,
        OwnershipInfoInheritedProperties,
        OwnershipInfoAllProperties,
    ] = OwnershipInfoAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OwnershipInfo"
    return model


OwnershipInfo = create_schema_org_model()


def create_ownershipinfo_model(
    model: Union[
        OwnershipInfoProperties,
        OwnershipInfoInheritedProperties,
        OwnershipInfoAllProperties,
    ]
):
    _type = deepcopy(OwnershipInfoAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OwnershipInfoAllProperties):
    pydantic_type = create_ownershipinfo_model(model=model)
    return pydantic_type(model).schema_json()
