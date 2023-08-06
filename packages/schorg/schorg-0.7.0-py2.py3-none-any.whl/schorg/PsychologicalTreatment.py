"""
A process of care relying upon counseling, dialogue and communication  aimed at improving a mental health condition without use of drugs.

https://schema.org/PsychologicalTreatment
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PsychologicalTreatmentInheritedProperties(TypedDict):
    """A process of care relying upon counseling, dialogue and communication  aimed at improving a mental health condition without use of drugs.

    References:
        https://schema.org/PsychologicalTreatment
    Note:
        Model Depth 5
    Attributes:
        doseSchedule: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.
        drug: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifying a drug or medicine used in a medication procedure.
        adverseOutcome: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or otherwise life-threatening or requiring immediate medical attention), tag it as a seriousAdverseOutcome instead.
    """

    doseSchedule: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    drug: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    adverseOutcome: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class PsychologicalTreatmentProperties(TypedDict):
    """A process of care relying upon counseling, dialogue and communication  aimed at improving a mental health condition without use of drugs.

    References:
        https://schema.org/PsychologicalTreatment
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PsychologicalTreatmentInheritedProperties , PsychologicalTreatmentProperties, TypedDict):
    pass


class PsychologicalTreatmentBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PsychologicalTreatment",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'doseSchedule': {'exclude': True}}
        fields = {'drug': {'exclude': True}}
        fields = {'adverseOutcome': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PsychologicalTreatmentProperties, PsychologicalTreatmentInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PsychologicalTreatment"
    return model
    

PsychologicalTreatment = create_schema_org_model()


def create_psychologicaltreatment_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_psychologicaltreatment_model(model=model)
    return pydantic_type(model).schema_json()


