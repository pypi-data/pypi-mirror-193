"""
A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes.

https://schema.org/DiagnosticProcedure
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DiagnosticProcedureInheritedProperties(TypedDict):
    """A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes.

    References:
        https://schema.org/DiagnosticProcedure
    Note:
        Model Depth 4
    Attributes:
        howPerformed: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): How the procedure is performed.
        procedureType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The type of procedure, for example Surgical, Noninvasive, or Percutaneous.
        status: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The status of the study (enumerated).
        bodyLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Location in the body of the anatomical structure.
        followup: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Typical or recommended followup care after the procedure is performed.
        preparation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Typical preparation that a patient must undergo before having the procedure performed.
    """

    howPerformed: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    procedureType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    status: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    bodyLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    followup: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    preparation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class DiagnosticProcedureProperties(TypedDict):
    """A medical procedure intended primarily for diagnostic, as opposed to therapeutic, purposes.

    References:
        https://schema.org/DiagnosticProcedure
    Note:
        Model Depth 4
    Attributes:
    """


class DiagnosticProcedureAllProperties(
    DiagnosticProcedureInheritedProperties, DiagnosticProcedureProperties, TypedDict
):
    pass


class DiagnosticProcedureBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DiagnosticProcedure", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"howPerformed": {"exclude": True}}
        fields = {"procedureType": {"exclude": True}}
        fields = {"status": {"exclude": True}}
        fields = {"bodyLocation": {"exclude": True}}
        fields = {"followup": {"exclude": True}}
        fields = {"preparation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DiagnosticProcedureProperties,
        DiagnosticProcedureInheritedProperties,
        DiagnosticProcedureAllProperties,
    ] = DiagnosticProcedureAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DiagnosticProcedure"
    return model


DiagnosticProcedure = create_schema_org_model()


def create_diagnosticprocedure_model(
    model: Union[
        DiagnosticProcedureProperties,
        DiagnosticProcedureInheritedProperties,
        DiagnosticProcedureAllProperties,
    ]
):
    _type = deepcopy(DiagnosticProcedureAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DiagnosticProcedureAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DiagnosticProcedureAllProperties):
    pydantic_type = create_diagnosticprocedure_model(model=model)
    return pydantic_type(model).schema_json()
