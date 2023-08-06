"""
Enumeration of considerations that make a product relevant or potentially restricted for adults only.

https://schema.org/AdultOrientedEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AdultOrientedEnumerationInheritedProperties(TypedDict):
    """Enumeration of considerations that make a product relevant or potentially restricted for adults only.

    References:
        https://schema.org/AdultOrientedEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class AdultOrientedEnumerationProperties(TypedDict):
    """Enumeration of considerations that make a product relevant or potentially restricted for adults only.

    References:
        https://schema.org/AdultOrientedEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class AdultOrientedEnumerationAllProperties(
    AdultOrientedEnumerationInheritedProperties,
    AdultOrientedEnumerationProperties,
    TypedDict,
):
    pass


class AdultOrientedEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AdultOrientedEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        AdultOrientedEnumerationProperties,
        AdultOrientedEnumerationInheritedProperties,
        AdultOrientedEnumerationAllProperties,
    ] = AdultOrientedEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AdultOrientedEnumeration"
    return model


AdultOrientedEnumeration = create_schema_org_model()


def create_adultorientedenumeration_model(
    model: Union[
        AdultOrientedEnumerationProperties,
        AdultOrientedEnumerationInheritedProperties,
        AdultOrientedEnumerationAllProperties,
    ]
):
    _type = deepcopy(AdultOrientedEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AdultOrientedEnumerationAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AdultOrientedEnumerationAllProperties):
    pydantic_type = create_adultorientedenumeration_model(model=model)
    return pydantic_type(model).schema_json()
