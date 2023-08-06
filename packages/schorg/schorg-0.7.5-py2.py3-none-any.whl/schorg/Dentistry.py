"""
A branch of medicine that is involved in the dental care.

https://schema.org/Dentistry
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DentistryInheritedProperties(TypedDict):
    """A branch of medicine that is involved in the dental care.

    References:
        https://schema.org/Dentistry
    Note:
        Model Depth 6
    Attributes:
    """


class DentistryProperties(TypedDict):
    """A branch of medicine that is involved in the dental care.

    References:
        https://schema.org/Dentistry
    Note:
        Model Depth 6
    Attributes:
    """


class DentistryAllProperties(
    DentistryInheritedProperties, DentistryProperties, TypedDict
):
    pass


class DentistryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Dentistry", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DentistryProperties, DentistryInheritedProperties, DentistryAllProperties
    ] = DentistryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Dentistry"
    return model


Dentistry = create_schema_org_model()


def create_dentistry_model(
    model: Union[
        DentistryProperties, DentistryInheritedProperties, DentistryAllProperties
    ]
):
    _type = deepcopy(DentistryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Dentistry. Please see: https://schema.org/Dentistry"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DentistryAllProperties):
    pydantic_type = create_dentistry_model(model=model)
    return pydantic_type(model).schema_json()
