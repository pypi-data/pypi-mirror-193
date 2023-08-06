"""
Design models for medical trials. Enumerated type.

https://schema.org/MedicalTrialDesign
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalTrialDesignInheritedProperties(TypedDict):
    """Design models for medical trials. Enumerated type.

    References:
        https://schema.org/MedicalTrialDesign
    Note:
        Model Depth 5
    Attributes:
    """


class MedicalTrialDesignProperties(TypedDict):
    """Design models for medical trials. Enumerated type.

    References:
        https://schema.org/MedicalTrialDesign
    Note:
        Model Depth 5
    Attributes:
    """


class MedicalTrialDesignAllProperties(
    MedicalTrialDesignInheritedProperties, MedicalTrialDesignProperties, TypedDict
):
    pass


class MedicalTrialDesignBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalTrialDesign", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MedicalTrialDesignProperties,
        MedicalTrialDesignInheritedProperties,
        MedicalTrialDesignAllProperties,
    ] = MedicalTrialDesignAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalTrialDesign"
    return model


MedicalTrialDesign = create_schema_org_model()


def create_medicaltrialdesign_model(
    model: Union[
        MedicalTrialDesignProperties,
        MedicalTrialDesignInheritedProperties,
        MedicalTrialDesignAllProperties,
    ]
):
    _type = deepcopy(MedicalTrialDesignAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MedicalTrialDesign. Please see: https://schema.org/MedicalTrialDesign"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MedicalTrialDesignAllProperties):
    pydantic_type = create_medicaltrialdesign_model(model=model)
    return pydantic_type(model).schema_json()
