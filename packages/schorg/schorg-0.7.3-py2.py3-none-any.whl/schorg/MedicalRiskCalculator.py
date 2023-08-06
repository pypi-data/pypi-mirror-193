"""
A complex mathematical calculation requiring an online calculator, used to assess prognosis. Note: use the url property of Thing to record any URLs for online calculators.

https://schema.org/MedicalRiskCalculator
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalRiskCalculatorInheritedProperties(TypedDict):
    """A complex mathematical calculation requiring an online calculator, used to assess prognosis. Note: use the url property of Thing to record any URLs for online calculators.

    References:
        https://schema.org/MedicalRiskCalculator
    Note:
        Model Depth 4
    Attributes:
        estimatesRiskOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The condition, complication, or symptom whose risk is being estimated.
        includedRiskFactor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A modifiable or non-modifiable risk factor included in the calculation, e.g. age, coexisting condition.
    """

    estimatesRiskOf: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    includedRiskFactor: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class MedicalRiskCalculatorProperties(TypedDict):
    """A complex mathematical calculation requiring an online calculator, used to assess prognosis. Note: use the url property of Thing to record any URLs for online calculators.

    References:
        https://schema.org/MedicalRiskCalculator
    Note:
        Model Depth 4
    Attributes:
    """


class MedicalRiskCalculatorAllProperties(
    MedicalRiskCalculatorInheritedProperties, MedicalRiskCalculatorProperties, TypedDict
):
    pass


class MedicalRiskCalculatorBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalRiskCalculator", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"estimatesRiskOf": {"exclude": True}}
        fields = {"includedRiskFactor": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalRiskCalculatorProperties,
        MedicalRiskCalculatorInheritedProperties,
        MedicalRiskCalculatorAllProperties,
    ] = MedicalRiskCalculatorAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalRiskCalculator"
    return model


MedicalRiskCalculator = create_schema_org_model()


def create_medicalriskcalculator_model(
    model: Union[
        MedicalRiskCalculatorProperties,
        MedicalRiskCalculatorInheritedProperties,
        MedicalRiskCalculatorAllProperties,
    ]
):
    _type = deepcopy(MedicalRiskCalculatorAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalRiskCalculatorAllProperties):
    pydantic_type = create_medicalriskcalculator_model(model=model)
    return pydantic_type(model).schema_json()
