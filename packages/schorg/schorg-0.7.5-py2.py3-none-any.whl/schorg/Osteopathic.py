"""
A system of medicine focused on promoting the body's innate ability to heal itself.

https://schema.org/Osteopathic
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OsteopathicInheritedProperties(TypedDict):
    """A system of medicine focused on promoting the body's innate ability to heal itself.

    References:
        https://schema.org/Osteopathic
    Note:
        Model Depth 6
    Attributes:
    """


class OsteopathicProperties(TypedDict):
    """A system of medicine focused on promoting the body's innate ability to heal itself.

    References:
        https://schema.org/Osteopathic
    Note:
        Model Depth 6
    Attributes:
    """


class OsteopathicAllProperties(
    OsteopathicInheritedProperties, OsteopathicProperties, TypedDict
):
    pass


class OsteopathicBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Osteopathic", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OsteopathicProperties, OsteopathicInheritedProperties, OsteopathicAllProperties
    ] = OsteopathicAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Osteopathic"
    return model


Osteopathic = create_schema_org_model()


def create_osteopathic_model(
    model: Union[
        OsteopathicProperties, OsteopathicInheritedProperties, OsteopathicAllProperties
    ]
):
    _type = deepcopy(OsteopathicAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Osteopathic. Please see: https://schema.org/Osteopathic"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: OsteopathicAllProperties):
    pydantic_type = create_osteopathic_model(model=model)
    return pydantic_type(model).schema_json()
