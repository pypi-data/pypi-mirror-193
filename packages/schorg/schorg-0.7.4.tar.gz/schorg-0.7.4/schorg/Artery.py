"""
A type of blood vessel that specifically carries blood away from the heart.

https://schema.org/Artery
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ArteryInheritedProperties(TypedDict):
    """A type of blood vessel that specifically carries blood away from the heart.

    References:
        https://schema.org/Artery
    Note:
        Model Depth 5
    Attributes:
    """


class ArteryProperties(TypedDict):
    """A type of blood vessel that specifically carries blood away from the heart.

    References:
        https://schema.org/Artery
    Note:
        Model Depth 5
    Attributes:
        arterialBranch: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The branches that comprise the arterial structure.
        supplyTo: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The area to which the artery supplies blood.
    """

    arterialBranch: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    supplyTo: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class ArteryAllProperties(ArteryInheritedProperties, ArteryProperties, TypedDict):
    pass


class ArteryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Artery", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"arterialBranch": {"exclude": True}}
        fields = {"supplyTo": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ArteryProperties, ArteryInheritedProperties, ArteryAllProperties
    ] = ArteryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Artery"
    return model


Artery = create_schema_org_model()


def create_artery_model(
    model: Union[ArteryProperties, ArteryInheritedProperties, ArteryAllProperties]
):
    _type = deepcopy(ArteryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ArteryAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ArteryAllProperties):
    pydantic_type = create_artery_model(model=model)
    return pydantic_type(model).schema_json()
