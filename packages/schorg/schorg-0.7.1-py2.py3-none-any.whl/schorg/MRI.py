"""
Magnetic resonance imaging.

https://schema.org/MRI
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MRIInheritedProperties(TypedDict):
    """Magnetic resonance imaging.

    References:
        https://schema.org/MRI
    Note:
        Model Depth 6
    Attributes:
    """

    


class MRIProperties(TypedDict):
    """Magnetic resonance imaging.

    References:
        https://schema.org/MRI
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(MRIInheritedProperties , MRIProperties, TypedDict):
    pass


class MRIBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MRI",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MRIProperties, MRIInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MRI"
    return model
    

MRI = create_schema_org_model()


def create_mri_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_mri_model(model=model)
    return pydantic_type(model).schema_json()


