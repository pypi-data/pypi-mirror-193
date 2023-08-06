"""
Magnetic resonance imaging.

https://schema.org/MRI
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class MRIAllProperties(MRIInheritedProperties, MRIProperties, TypedDict):
    pass


class MRIBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MRI", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MRIProperties, MRIInheritedProperties, MRIAllProperties
    ] = MRIAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MRI"
    return model


MRI = create_schema_org_model()


def create_mri_model(
    model: Union[MRIProperties, MRIInheritedProperties, MRIAllProperties]
):
    _type = deepcopy(MRIAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MRIAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MRIAllProperties):
    pydantic_type = create_mri_model(model=model)
    return pydantic_type(model).schema_json()
