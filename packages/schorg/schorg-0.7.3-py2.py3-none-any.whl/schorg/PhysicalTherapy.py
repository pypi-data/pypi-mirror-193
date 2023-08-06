"""
A process of progressive physical care and rehabilitation aimed at improving a health condition.

https://schema.org/PhysicalTherapy
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PhysicalTherapyInheritedProperties(TypedDict):
    """A process of progressive physical care and rehabilitation aimed at improving a health condition.

    References:
        https://schema.org/PhysicalTherapy
    Note:
        Model Depth 6
    Attributes:
        seriousAdverseOutcome: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.
        duplicateTherapy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A therapy that duplicates or overlaps this one.
        contraindication: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A contraindication for this therapy.
    """

    seriousAdverseOutcome: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    duplicateTherapy: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    contraindication: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class PhysicalTherapyProperties(TypedDict):
    """A process of progressive physical care and rehabilitation aimed at improving a health condition.

    References:
        https://schema.org/PhysicalTherapy
    Note:
        Model Depth 6
    Attributes:
    """


class PhysicalTherapyAllProperties(
    PhysicalTherapyInheritedProperties, PhysicalTherapyProperties, TypedDict
):
    pass


class PhysicalTherapyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PhysicalTherapy", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"seriousAdverseOutcome": {"exclude": True}}
        fields = {"duplicateTherapy": {"exclude": True}}
        fields = {"contraindication": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PhysicalTherapyProperties,
        PhysicalTherapyInheritedProperties,
        PhysicalTherapyAllProperties,
    ] = PhysicalTherapyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PhysicalTherapy"
    return model


PhysicalTherapy = create_schema_org_model()


def create_physicaltherapy_model(
    model: Union[
        PhysicalTherapyProperties,
        PhysicalTherapyInheritedProperties,
        PhysicalTherapyAllProperties,
    ]
):
    _type = deepcopy(PhysicalTherapyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PhysicalTherapyAllProperties):
    pydantic_type = create_physicaltherapy_model(model=model)
    return pydantic_type(model).schema_json()
