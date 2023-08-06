"""
X-ray imaging.

https://schema.org/XRay
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class XRayInheritedProperties(TypedDict):
    """X-ray imaging.

    References:
        https://schema.org/XRay
    Note:
        Model Depth 6
    Attributes:
    """


class XRayProperties(TypedDict):
    """X-ray imaging.

    References:
        https://schema.org/XRay
    Note:
        Model Depth 6
    Attributes:
    """


class XRayAllProperties(XRayInheritedProperties, XRayProperties, TypedDict):
    pass


class XRayBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="XRay", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        XRayProperties, XRayInheritedProperties, XRayAllProperties
    ] = XRayAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "XRay"
    return model


XRay = create_schema_org_model()


def create_xray_model(
    model: Union[XRayProperties, XRayInheritedProperties, XRayAllProperties]
):
    _type = deepcopy(XRayAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of XRayAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: XRayAllProperties):
    pydantic_type = create_xray_model(model=model)
    return pydantic_type(model).schema_json()
