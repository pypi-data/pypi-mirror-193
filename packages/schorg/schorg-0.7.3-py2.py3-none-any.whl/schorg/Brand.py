"""
A brand is a name used by an organization or business person for labeling a product, product group, or similar.

https://schema.org/Brand
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BrandInheritedProperties(TypedDict):
    """A brand is a name used by an organization or business person for labeling a product, product group, or similar.

    References:
        https://schema.org/Brand
    Note:
        Model Depth 3
    Attributes:
    """


class BrandProperties(TypedDict):
    """A brand is a name used by an organization or business person for labeling a product, product group, or similar.

    References:
        https://schema.org/Brand
    Note:
        Model Depth 3
    Attributes:
        slogan: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A slogan or motto associated with the item.
        review: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A review of the item.
        logo: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): An associated logo.
        aggregateRating: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The overall rating, based on a collection of reviews or ratings, of the item.
    """

    slogan: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    review: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    logo: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    aggregateRating: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class BrandAllProperties(BrandInheritedProperties, BrandProperties, TypedDict):
    pass


class BrandBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Brand", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"slogan": {"exclude": True}}
        fields = {"review": {"exclude": True}}
        fields = {"logo": {"exclude": True}}
        fields = {"aggregateRating": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BrandProperties, BrandInheritedProperties, BrandAllProperties
    ] = BrandAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Brand"
    return model


Brand = create_schema_org_model()


def create_brand_model(
    model: Union[BrandProperties, BrandInheritedProperties, BrandAllProperties]
):
    _type = deepcopy(BrandAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BrandAllProperties):
    pydantic_type = create_brand_model(model=model)
    return pydantic_type(model).schema_json()
