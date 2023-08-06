"""
A specific branch of medical science that deals with the evaluation and initial treatment of medical conditions caused by trauma or sudden illness.

https://schema.org/Emergency
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EmergencyInheritedProperties(TypedDict):
    """A specific branch of medical science that deals with the evaluation and initial treatment of medical conditions caused by trauma or sudden illness.

    References:
        https://schema.org/Emergency
    Note:
        Model Depth 5
    Attributes:
    """

    


class EmergencyProperties(TypedDict):
    """A specific branch of medical science that deals with the evaluation and initial treatment of medical conditions caused by trauma or sudden illness.

    References:
        https://schema.org/Emergency
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(EmergencyInheritedProperties , EmergencyProperties, TypedDict):
    pass


class EmergencyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Emergency",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EmergencyProperties, EmergencyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Emergency"
    return model
    

Emergency = create_schema_org_model()


def create_emergency_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_emergency_model(model=model)
    return pydantic_type(model).schema_json()


