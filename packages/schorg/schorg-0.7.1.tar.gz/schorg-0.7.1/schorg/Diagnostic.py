"""
A medical device used for diagnostic purposes.

https://schema.org/Diagnostic
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DiagnosticInheritedProperties(TypedDict):
    """A medical device used for diagnostic purposes.

    References:
        https://schema.org/Diagnostic
    Note:
        Model Depth 6
    Attributes:
    """

    


class DiagnosticProperties(TypedDict):
    """A medical device used for diagnostic purposes.

    References:
        https://schema.org/Diagnostic
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(DiagnosticInheritedProperties , DiagnosticProperties, TypedDict):
    pass


class DiagnosticBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Diagnostic",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DiagnosticProperties, DiagnosticInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Diagnostic"
    return model
    

Diagnostic = create_schema_org_model()


def create_diagnostic_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_diagnostic_model(model=model)
    return pydantic_type(model).schema_json()


