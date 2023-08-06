"""
Any object used in a medical capacity, such as to diagnose or treat a patient.

https://schema.org/MedicalDevice
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalDeviceInheritedProperties(TypedDict):
    """Any object used in a medical capacity, such as to diagnose or treat a patient.

    References:
        https://schema.org/MedicalDevice
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
    


class MedicalDeviceProperties(TypedDict):
    """Any object used in a medical capacity, such as to diagnose or treat a patient.

    References:
        https://schema.org/MedicalDevice
    Note:
        Model Depth 3
    Attributes:
        postOp: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A description of the postoperative procedures, care, and/or followups for this device.
        seriousAdverseOutcome: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.
        preOp: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A description of the workup, testing, and other preparations required before implanting this device.
        adverseOutcome: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or otherwise life-threatening or requiring immediate medical attention), tag it as a seriousAdverseOutcome instead.
        procedure: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A description of the procedure involved in setting up, using, and/or installing the device.
        contraindication: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A contraindication for this therapy.
    """

    postOp: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    seriousAdverseOutcome: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    preOp: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    adverseOutcome: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    procedure: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    contraindication: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(MedicalDeviceInheritedProperties , MedicalDeviceProperties, TypedDict):
    pass


class MedicalDeviceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalDevice",alias='@id')
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
        fields = {'postOp': {'exclude': True}}
        fields = {'seriousAdverseOutcome': {'exclude': True}}
        fields = {'preOp': {'exclude': True}}
        fields = {'adverseOutcome': {'exclude': True}}
        fields = {'procedure': {'exclude': True}}
        fields = {'contraindication': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MedicalDeviceProperties, MedicalDeviceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalDevice"
    return model
    

MedicalDevice = create_schema_org_model()


def create_medicaldevice_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicaldevice_model(model=model)
    return pydantic_type(model).schema_json()


