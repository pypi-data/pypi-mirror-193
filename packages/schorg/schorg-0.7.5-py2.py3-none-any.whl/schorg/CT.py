"""
X-ray computed tomography imaging.

https://schema.org/CT
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CTInheritedProperties(TypedDict):
    """X-ray computed tomography imaging.

    References:
        https://schema.org/CT
    Note:
        Model Depth 6
    Attributes:
    """


class CTProperties(TypedDict):
    """X-ray computed tomography imaging.

    References:
        https://schema.org/CT
    Note:
        Model Depth 6
    Attributes:
    """


class CTAllProperties(CTInheritedProperties, CTProperties, TypedDict):
    pass


class CTBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CT", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[CTProperties, CTInheritedProperties, CTAllProperties] = CTAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CT"
    return model


CT = create_schema_org_model()


def create_ct_model(model: Union[CTProperties, CTInheritedProperties, CTAllProperties]):
    _type = deepcopy(CTAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of CT. Please see: https://schema.org/CT")
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CTAllProperties):
    pydantic_type = create_ct_model(model=model)
    return pydantic_type(model).schema_json()
