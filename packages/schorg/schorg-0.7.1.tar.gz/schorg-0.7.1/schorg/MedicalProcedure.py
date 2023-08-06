"""
A process of care used in either a diagnostic, therapeutic, preventive or palliative capacity that relies on invasive (surgical), non-invasive, or other techniques.

https://schema.org/MedicalProcedure
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalProcedureInheritedProperties(TypedDict):
    """A process of care used in either a diagnostic, therapeutic, preventive or palliative capacity that relies on invasive (surgical), non-invasive, or other techniques.

    References:
        https://schema.org/MedicalProcedure
    Note:
        Model Depth 3
    Attributes:
        recognizingAuthority: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): If applicable, the organization that officially recognizes this entity as part of its endorsed system of medicine.
        relevantSpecialty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): If applicable, a medical specialty in which this entity is relevant.
        medicineSystem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc.
        funding: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        legalStatus: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The drug or supplement's legal status, including any controlled substance schedules that apply.
        study: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical study or trial related to this entity.
        guideline: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical guideline related to this entity.
        code: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.
    """

    recognizingAuthority: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    relevantSpecialty: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    medicineSystem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    funding: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    legalStatus: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    study: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    guideline: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    code: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class MedicalProcedureProperties(TypedDict):
    """A process of care used in either a diagnostic, therapeutic, preventive or palliative capacity that relies on invasive (surgical), non-invasive, or other techniques.

    References:
        https://schema.org/MedicalProcedure
    Note:
        Model Depth 3
    Attributes:
        howPerformed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): How the procedure is performed.
        procedureType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type of procedure, for example Surgical, Noninvasive, or Percutaneous.
        status: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The status of the study (enumerated).
        bodyLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Location in the body of the anatomical structure.
        followup: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Typical or recommended followup care after the procedure is performed.
        preparation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Typical preparation that a patient must undergo before having the procedure performed.
    """

    howPerformed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    procedureType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    status: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    bodyLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    followup: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    preparation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(MedicalProcedureInheritedProperties , MedicalProcedureProperties, TypedDict):
    pass


class MedicalProcedureBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalProcedure",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'recognizingAuthority': {'exclude': True}}
        fields = {'relevantSpecialty': {'exclude': True}}
        fields = {'medicineSystem': {'exclude': True}}
        fields = {'funding': {'exclude': True}}
        fields = {'legalStatus': {'exclude': True}}
        fields = {'study': {'exclude': True}}
        fields = {'guideline': {'exclude': True}}
        fields = {'code': {'exclude': True}}
        fields = {'howPerformed': {'exclude': True}}
        fields = {'procedureType': {'exclude': True}}
        fields = {'status': {'exclude': True}}
        fields = {'bodyLocation': {'exclude': True}}
        fields = {'followup': {'exclude': True}}
        fields = {'preparation': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MedicalProcedureProperties, MedicalProcedureInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalProcedure"
    return model
    

MedicalProcedure = create_schema_org_model()


def create_medicalprocedure_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalprocedure_model(model=model)
    return pydantic_type(model).schema_json()


