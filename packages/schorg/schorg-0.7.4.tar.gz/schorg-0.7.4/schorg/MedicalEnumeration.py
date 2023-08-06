"""
Enumerations related to health and the practice of medicine: A concept that is used to attribute a quality to another concept, as a qualifier, a collection of items or a listing of all of the elements of a set in medicine practice.

https://schema.org/MedicalEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalEnumerationInheritedProperties(TypedDict):
    """Enumerations related to health and the practice of medicine: A concept that is used to attribute a quality to another concept, as a qualifier, a collection of items or a listing of all of the elements of a set in medicine practice.

    References:
        https://schema.org/MedicalEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class MedicalEnumerationProperties(TypedDict):
    """Enumerations related to health and the practice of medicine: A concept that is used to attribute a quality to another concept, as a qualifier, a collection of items or a listing of all of the elements of a set in medicine practice.

    References:
        https://schema.org/MedicalEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class MedicalEnumerationAllProperties(
    MedicalEnumerationInheritedProperties, MedicalEnumerationProperties, TypedDict
):
    pass


class MedicalEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalEnumerationProperties,
        MedicalEnumerationInheritedProperties,
        MedicalEnumerationAllProperties,
    ] = MedicalEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalEnumeration"
    return model


MedicalEnumeration = create_schema_org_model()


def create_medicalenumeration_model(
    model: Union[
        MedicalEnumerationProperties,
        MedicalEnumerationInheritedProperties,
        MedicalEnumerationAllProperties,
    ]
):
    _type = deepcopy(MedicalEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MedicalEnumerationAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalEnumerationAllProperties):
    pydantic_type = create_medicalenumeration_model(model=model)
    return pydantic_type(model).schema_json()
