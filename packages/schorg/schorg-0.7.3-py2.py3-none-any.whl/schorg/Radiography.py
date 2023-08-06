"""
Radiography is an imaging technique that uses electromagnetic radiation other than visible light, especially X-rays, to view the internal structure of a non-uniformly composed and opaque object such as the human body.

https://schema.org/Radiography
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RadiographyInheritedProperties(TypedDict):
    """Radiography is an imaging technique that uses electromagnetic radiation other than visible light, especially X-rays, to view the internal structure of a non-uniformly composed and opaque object such as the human body.

    References:
        https://schema.org/Radiography
    Note:
        Model Depth 6
    Attributes:
    """


class RadiographyProperties(TypedDict):
    """Radiography is an imaging technique that uses electromagnetic radiation other than visible light, especially X-rays, to view the internal structure of a non-uniformly composed and opaque object such as the human body.

    References:
        https://schema.org/Radiography
    Note:
        Model Depth 6
    Attributes:
    """


class RadiographyAllProperties(
    RadiographyInheritedProperties, RadiographyProperties, TypedDict
):
    pass


class RadiographyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Radiography", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RadiographyProperties, RadiographyInheritedProperties, RadiographyAllProperties
    ] = RadiographyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Radiography"
    return model


Radiography = create_schema_org_model()


def create_radiography_model(
    model: Union[
        RadiographyProperties, RadiographyInheritedProperties, RadiographyAllProperties
    ]
):
    _type = deepcopy(RadiographyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RadiographyAllProperties):
    pydantic_type = create_radiography_model(model=model)
    return pydantic_type(model).schema_json()
