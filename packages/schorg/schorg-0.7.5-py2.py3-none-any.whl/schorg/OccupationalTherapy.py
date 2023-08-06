"""
A treatment of people with physical, emotional, or social problems, using purposeful activity to help them overcome or learn to deal with their problems.

https://schema.org/OccupationalTherapy
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OccupationalTherapyInheritedProperties(TypedDict):
    """A treatment of people with physical, emotional, or social problems, using purposeful activity to help them overcome or learn to deal with their problems.

    References:
        https://schema.org/OccupationalTherapy
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


class OccupationalTherapyProperties(TypedDict):
    """A treatment of people with physical, emotional, or social problems, using purposeful activity to help them overcome or learn to deal with their problems.

    References:
        https://schema.org/OccupationalTherapy
    Note:
        Model Depth 6
    Attributes:
    """


class OccupationalTherapyAllProperties(
    OccupationalTherapyInheritedProperties, OccupationalTherapyProperties, TypedDict
):
    pass


class OccupationalTherapyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OccupationalTherapy", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"seriousAdverseOutcome": {"exclude": True}}
        fields = {"duplicateTherapy": {"exclude": True}}
        fields = {"contraindication": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        OccupationalTherapyProperties,
        OccupationalTherapyInheritedProperties,
        OccupationalTherapyAllProperties,
    ] = OccupationalTherapyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OccupationalTherapy"
    return model


OccupationalTherapy = create_schema_org_model()


def create_occupationaltherapy_model(
    model: Union[
        OccupationalTherapyProperties,
        OccupationalTherapyInheritedProperties,
        OccupationalTherapyAllProperties,
    ]
):
    _type = deepcopy(OccupationalTherapyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of OccupationalTherapy. Please see: https://schema.org/OccupationalTherapy"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: OccupationalTherapyAllProperties):
    pydantic_type = create_occupationaltherapy_model(model=model)
    return pydantic_type(model).schema_json()
