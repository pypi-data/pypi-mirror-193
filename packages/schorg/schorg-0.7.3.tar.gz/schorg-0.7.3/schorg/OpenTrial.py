"""
A trial design in which the researcher knows the full details of the treatment, and so does the patient.

https://schema.org/OpenTrial
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OpenTrialInheritedProperties(TypedDict):
    """A trial design in which the researcher knows the full details of the treatment, and so does the patient.

    References:
        https://schema.org/OpenTrial
    Note:
        Model Depth 6
    Attributes:
    """


class OpenTrialProperties(TypedDict):
    """A trial design in which the researcher knows the full details of the treatment, and so does the patient.

    References:
        https://schema.org/OpenTrial
    Note:
        Model Depth 6
    Attributes:
    """


class OpenTrialAllProperties(
    OpenTrialInheritedProperties, OpenTrialProperties, TypedDict
):
    pass


class OpenTrialBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OpenTrial", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OpenTrialProperties, OpenTrialInheritedProperties, OpenTrialAllProperties
    ] = OpenTrialAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OpenTrial"
    return model


OpenTrial = create_schema_org_model()


def create_opentrial_model(
    model: Union[
        OpenTrialProperties, OpenTrialInheritedProperties, OpenTrialAllProperties
    ]
):
    _type = deepcopy(OpenTrialAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OpenTrialAllProperties):
    pydantic_type = create_opentrial_model(model=model)
    return pydantic_type(model).schema_json()
