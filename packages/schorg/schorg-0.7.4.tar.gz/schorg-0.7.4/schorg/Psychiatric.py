"""
A specific branch of medical science that is concerned with the study, treatment, and prevention of mental illness, using both medical and psychological therapies.

https://schema.org/Psychiatric
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PsychiatricInheritedProperties(TypedDict):
    """A specific branch of medical science that is concerned with the study, treatment, and prevention of mental illness, using both medical and psychological therapies.

    References:
        https://schema.org/Psychiatric
    Note:
        Model Depth 5
    Attributes:
    """


class PsychiatricProperties(TypedDict):
    """A specific branch of medical science that is concerned with the study, treatment, and prevention of mental illness, using both medical and psychological therapies.

    References:
        https://schema.org/Psychiatric
    Note:
        Model Depth 5
    Attributes:
    """


class PsychiatricAllProperties(
    PsychiatricInheritedProperties, PsychiatricProperties, TypedDict
):
    pass


class PsychiatricBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Psychiatric", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PsychiatricProperties, PsychiatricInheritedProperties, PsychiatricAllProperties
    ] = PsychiatricAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Psychiatric"
    return model


Psychiatric = create_schema_org_model()


def create_psychiatric_model(
    model: Union[
        PsychiatricProperties, PsychiatricInheritedProperties, PsychiatricAllProperties
    ]
):
    _type = deepcopy(PsychiatricAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PsychiatricAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PsychiatricAllProperties):
    pydantic_type = create_psychiatric_model(model=model)
    return pydantic_type(model).schema_json()
