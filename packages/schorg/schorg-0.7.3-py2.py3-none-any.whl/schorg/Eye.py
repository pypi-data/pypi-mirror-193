"""
Eye or ophthalmological function assessment with clinical examination.

https://schema.org/Eye
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EyeInheritedProperties(TypedDict):
    """Eye or ophthalmological function assessment with clinical examination.

    References:
        https://schema.org/Eye
    Note:
        Model Depth 5
    Attributes:
    """


class EyeProperties(TypedDict):
    """Eye or ophthalmological function assessment with clinical examination.

    References:
        https://schema.org/Eye
    Note:
        Model Depth 5
    Attributes:
    """


class EyeAllProperties(EyeInheritedProperties, EyeProperties, TypedDict):
    pass


class EyeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Eye", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EyeProperties, EyeInheritedProperties, EyeAllProperties
    ] = EyeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Eye"
    return model


Eye = create_schema_org_model()


def create_eye_model(
    model: Union[EyeProperties, EyeInheritedProperties, EyeAllProperties]
):
    _type = deepcopy(EyeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EyeAllProperties):
    pydantic_type = create_eye_model(model=model)
    return pydantic_type(model).schema_json()
