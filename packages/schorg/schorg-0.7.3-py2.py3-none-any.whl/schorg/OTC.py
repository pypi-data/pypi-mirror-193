"""
The character of a medical substance, typically a medicine, of being available over the counter or not.

https://schema.org/OTC
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OTCInheritedProperties(TypedDict):
    """The character of a medical substance, typically a medicine, of being available over the counter or not.

    References:
        https://schema.org/OTC
    Note:
        Model Depth 6
    Attributes:
    """


class OTCProperties(TypedDict):
    """The character of a medical substance, typically a medicine, of being available over the counter or not.

    References:
        https://schema.org/OTC
    Note:
        Model Depth 6
    Attributes:
    """


class OTCAllProperties(OTCInheritedProperties, OTCProperties, TypedDict):
    pass


class OTCBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OTC", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OTCProperties, OTCInheritedProperties, OTCAllProperties
    ] = OTCAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OTC"
    return model


OTC = create_schema_org_model()


def create_otc_model(
    model: Union[OTCProperties, OTCInheritedProperties, OTCAllProperties]
):
    _type = deepcopy(OTCAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OTCAllProperties):
    pydantic_type = create_otc_model(model=model)
    return pydantic_type(model).schema_json()
