"""
A type of medical procedure that involves percutaneous techniques, where access to organs or tissue is achieved via needle-puncture of the skin. For example, catheter-based procedures like stent delivery.

https://schema.org/PercutaneousProcedure
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PercutaneousProcedureInheritedProperties(TypedDict):
    """A type of medical procedure that involves percutaneous techniques, where access to organs or tissue is achieved via needle-puncture of the skin. For example, catheter-based procedures like stent delivery.

    References:
        https://schema.org/PercutaneousProcedure
    Note:
        Model Depth 6
    Attributes:
    """

    


class PercutaneousProcedureProperties(TypedDict):
    """A type of medical procedure that involves percutaneous techniques, where access to organs or tissue is achieved via needle-puncture of the skin. For example, catheter-based procedures like stent delivery.

    References:
        https://schema.org/PercutaneousProcedure
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(PercutaneousProcedureInheritedProperties , PercutaneousProcedureProperties, TypedDict):
    pass


class PercutaneousProcedureBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PercutaneousProcedure",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PercutaneousProcedureProperties, PercutaneousProcedureInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PercutaneousProcedure"
    return model
    

PercutaneousProcedure = create_schema_org_model()


def create_percutaneousprocedure_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_percutaneousprocedure_model(model=model)
    return pydantic_type(model).schema_json()


