"""
A process of care using radiation aimed at improving a health condition.

https://schema.org/RadiationTherapy
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RadiationTherapyInheritedProperties(TypedDict):
    """A process of care using radiation aimed at improving a health condition.

    References:
        https://schema.org/RadiationTherapy
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


class RadiationTherapyProperties(TypedDict):
    """A process of care using radiation aimed at improving a health condition.

    References:
        https://schema.org/RadiationTherapy
    Note:
        Model Depth 6
    Attributes:
    """


class RadiationTherapyAllProperties(
    RadiationTherapyInheritedProperties, RadiationTherapyProperties, TypedDict
):
    pass


class RadiationTherapyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RadiationTherapy", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"seriousAdverseOutcome": {"exclude": True}}
        fields = {"duplicateTherapy": {"exclude": True}}
        fields = {"contraindication": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RadiationTherapyProperties,
        RadiationTherapyInheritedProperties,
        RadiationTherapyAllProperties,
    ] = RadiationTherapyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RadiationTherapy"
    return model


RadiationTherapy = create_schema_org_model()


def create_radiationtherapy_model(
    model: Union[
        RadiationTherapyProperties,
        RadiationTherapyInheritedProperties,
        RadiationTherapyAllProperties,
    ]
):
    _type = deepcopy(RadiationTherapyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RadiationTherapyAllProperties):
    pydantic_type = create_radiationtherapy_model(model=model)
    return pydantic_type(model).schema_json()
