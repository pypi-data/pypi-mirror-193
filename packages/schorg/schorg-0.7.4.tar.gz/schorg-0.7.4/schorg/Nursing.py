"""
A health profession of a person formally educated and trained in the care of the sick or infirm person.

https://schema.org/Nursing
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NursingInheritedProperties(TypedDict):
    """A health profession of a person formally educated and trained in the care of the sick or infirm person.

    References:
        https://schema.org/Nursing
    Note:
        Model Depth 5
    Attributes:
    """


class NursingProperties(TypedDict):
    """A health profession of a person formally educated and trained in the care of the sick or infirm person.

    References:
        https://schema.org/Nursing
    Note:
        Model Depth 5
    Attributes:
    """


class NursingAllProperties(NursingInheritedProperties, NursingProperties, TypedDict):
    pass


class NursingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nursing", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NursingProperties, NursingInheritedProperties, NursingAllProperties
    ] = NursingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nursing"
    return model


Nursing = create_schema_org_model()


def create_nursing_model(
    model: Union[NursingProperties, NursingInheritedProperties, NursingAllProperties]
):
    _type = deepcopy(NursingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of NursingAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NursingAllProperties):
    pydantic_type = create_nursing_model(model=model)
    return pydantic_type(model).schema_json()
