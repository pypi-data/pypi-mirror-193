"""
A specific branch of medical science that specializes in the care of women during the prenatal and postnatal care and with the delivery of the child.

https://schema.org/Obstetric
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ObstetricInheritedProperties(TypedDict):
    """A specific branch of medical science that specializes in the care of women during the prenatal and postnatal care and with the delivery of the child.

    References:
        https://schema.org/Obstetric
    Note:
        Model Depth 5
    Attributes:
    """


class ObstetricProperties(TypedDict):
    """A specific branch of medical science that specializes in the care of women during the prenatal and postnatal care and with the delivery of the child.

    References:
        https://schema.org/Obstetric
    Note:
        Model Depth 5
    Attributes:
    """


class ObstetricAllProperties(
    ObstetricInheritedProperties, ObstetricProperties, TypedDict
):
    pass


class ObstetricBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Obstetric", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ObstetricProperties, ObstetricInheritedProperties, ObstetricAllProperties
    ] = ObstetricAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Obstetric"
    return model


Obstetric = create_schema_org_model()


def create_obstetric_model(
    model: Union[
        ObstetricProperties, ObstetricInheritedProperties, ObstetricAllProperties
    ]
):
    _type = deepcopy(ObstetricAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ObstetricAllProperties):
    pydantic_type = create_obstetric_model(model=model)
    return pydantic_type(model).schema_json()
