"""
Radiography is an imaging technique that uses electromagnetic radiation other than visible light, especially X-rays, to view the internal structure of a non-uniformly composed and opaque object such as the human body.

https://schema.org/Radiography
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(RadiographyInheritedProperties , RadiographyProperties, TypedDict):
    pass


class RadiographyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Radiography",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RadiographyProperties, RadiographyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Radiography"
    return model
    

Radiography = create_schema_org_model()


def create_radiography_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_radiography_model(model=model)
    return pydantic_type(model).schema_json()


