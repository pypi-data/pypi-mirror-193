"""
A list of possible conditions for the item.

https://schema.org/OfferItemCondition
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OfferItemConditionInheritedProperties(TypedDict):
    """A list of possible conditions for the item.

    References:
        https://schema.org/OfferItemCondition
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class OfferItemConditionProperties(TypedDict):
    """A list of possible conditions for the item.

    References:
        https://schema.org/OfferItemCondition
    Note:
        Model Depth 4
    Attributes:
    """


class OfferItemConditionAllProperties(
    OfferItemConditionInheritedProperties, OfferItemConditionProperties, TypedDict
):
    pass


class OfferItemConditionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OfferItemCondition", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        OfferItemConditionProperties,
        OfferItemConditionInheritedProperties,
        OfferItemConditionAllProperties,
    ] = OfferItemConditionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OfferItemCondition"
    return model


OfferItemCondition = create_schema_org_model()


def create_offeritemcondition_model(
    model: Union[
        OfferItemConditionProperties,
        OfferItemConditionInheritedProperties,
        OfferItemConditionAllProperties,
    ]
):
    _type = deepcopy(OfferItemConditionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OfferItemConditionAllProperties):
    pydantic_type = create_offeritemcondition_model(model=model)
    return pydantic_type(model).schema_json()
