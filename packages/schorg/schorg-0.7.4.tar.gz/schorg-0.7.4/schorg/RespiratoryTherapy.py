"""
The therapy that is concerned with the maintenance or improvement of respiratory function (as in patients with pulmonary disease).

https://schema.org/RespiratoryTherapy
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RespiratoryTherapyInheritedProperties(TypedDict):
    """The therapy that is concerned with the maintenance or improvement of respiratory function (as in patients with pulmonary disease).

    References:
        https://schema.org/RespiratoryTherapy
    Note:
        Model Depth 6
    Attributes:
        seriousAdverseOutcome: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.
        duplicateTherapy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A therapy that duplicates or overlaps this one.
        contraindication: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A contraindication for this therapy.
    """

    seriousAdverseOutcome: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    duplicateTherapy: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    contraindication: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class RespiratoryTherapyProperties(TypedDict):
    """The therapy that is concerned with the maintenance or improvement of respiratory function (as in patients with pulmonary disease).

    References:
        https://schema.org/RespiratoryTherapy
    Note:
        Model Depth 6
    Attributes:
    """


class RespiratoryTherapyAllProperties(
    RespiratoryTherapyInheritedProperties, RespiratoryTherapyProperties, TypedDict
):
    pass


class RespiratoryTherapyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RespiratoryTherapy", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"seriousAdverseOutcome": {"exclude": True}}
        fields = {"duplicateTherapy": {"exclude": True}}
        fields = {"contraindication": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RespiratoryTherapyProperties,
        RespiratoryTherapyInheritedProperties,
        RespiratoryTherapyAllProperties,
    ] = RespiratoryTherapyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RespiratoryTherapy"
    return model


RespiratoryTherapy = create_schema_org_model()


def create_respiratorytherapy_model(
    model: Union[
        RespiratoryTherapyProperties,
        RespiratoryTherapyInheritedProperties,
        RespiratoryTherapyAllProperties,
    ]
):
    _type = deepcopy(RespiratoryTherapyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of RespiratoryTherapyAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RespiratoryTherapyAllProperties):
    pydantic_type = create_respiratorytherapy_model(model=model)
    return pydantic_type(model).schema_json()
