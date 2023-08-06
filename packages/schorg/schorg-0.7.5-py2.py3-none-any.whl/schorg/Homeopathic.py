"""
A system of medicine based on the principle that a disease can be cured by a substance that produces similar symptoms in healthy people.

https://schema.org/Homeopathic
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HomeopathicInheritedProperties(TypedDict):
    """A system of medicine based on the principle that a disease can be cured by a substance that produces similar symptoms in healthy people.

    References:
        https://schema.org/Homeopathic
    Note:
        Model Depth 6
    Attributes:
    """


class HomeopathicProperties(TypedDict):
    """A system of medicine based on the principle that a disease can be cured by a substance that produces similar symptoms in healthy people.

    References:
        https://schema.org/Homeopathic
    Note:
        Model Depth 6
    Attributes:
    """


class HomeopathicAllProperties(
    HomeopathicInheritedProperties, HomeopathicProperties, TypedDict
):
    pass


class HomeopathicBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Homeopathic", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HomeopathicProperties, HomeopathicInheritedProperties, HomeopathicAllProperties
    ] = HomeopathicAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Homeopathic"
    return model


Homeopathic = create_schema_org_model()


def create_homeopathic_model(
    model: Union[
        HomeopathicProperties, HomeopathicInheritedProperties, HomeopathicAllProperties
    ]
):
    _type = deepcopy(HomeopathicAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Homeopathic. Please see: https://schema.org/Homeopathic"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: HomeopathicAllProperties):
    pydantic_type = create_homeopathic_model(model=model)
    return pydantic_type(model).schema_json()
