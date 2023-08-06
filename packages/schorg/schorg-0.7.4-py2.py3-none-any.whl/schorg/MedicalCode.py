"""
A code for a medical entity.

https://schema.org/MedicalCode
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalCodeInheritedProperties(TypedDict):
    """A code for a medical entity.

    References:
        https://schema.org/MedicalCode
    Note:
        Model Depth 4
    Attributes:
        codeValue: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A short textual code that uniquely identifies the value.
        inCodeSet: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A [[CategoryCodeSet]] that contains this category code.
    """

    codeValue: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    inCodeSet: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]


class MedicalCodeProperties(TypedDict):
    """A code for a medical entity.

    References:
        https://schema.org/MedicalCode
    Note:
        Model Depth 4
    Attributes:
        codeValue: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A short textual code that uniquely identifies the value.
        codingSystem: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The coding system, e.g. 'ICD-10'.
    """

    codeValue: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    codingSystem: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class MedicalCodeAllProperties(
    MedicalCodeInheritedProperties, MedicalCodeProperties, TypedDict
):
    pass


class MedicalCodeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MedicalCode", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"codeValue": {"exclude": True}}
        fields = {"inCodeSet": {"exclude": True}}
        fields = {"codeValue": {"exclude": True}}
        fields = {"codingSystem": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MedicalCodeProperties, MedicalCodeInheritedProperties, MedicalCodeAllProperties
    ] = MedicalCodeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalCode"
    return model


MedicalCode = create_schema_org_model()


def create_medicalcode_model(
    model: Union[
        MedicalCodeProperties, MedicalCodeInheritedProperties, MedicalCodeAllProperties
    ]
):
    _type = deepcopy(MedicalCodeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MedicalCodeAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MedicalCodeAllProperties):
    pydantic_type = create_medicalcode_model(model=model)
    return pydantic_type(model).schema_json()
