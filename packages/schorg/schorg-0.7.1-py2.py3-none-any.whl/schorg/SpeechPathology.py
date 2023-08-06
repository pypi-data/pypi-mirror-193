"""
The scientific study and treatment of defects, disorders, and malfunctions of speech and voice, as stuttering, lisping, or lalling, and of language disturbances, as aphasia or delayed language acquisition.

https://schema.org/SpeechPathology
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SpeechPathologyInheritedProperties(TypedDict):
    """The scientific study and treatment of defects, disorders, and malfunctions of speech and voice, as stuttering, lisping, or lalling, and of language disturbances, as aphasia or delayed language acquisition.

    References:
        https://schema.org/SpeechPathology
    Note:
        Model Depth 6
    Attributes:
    """

    


class SpeechPathologyProperties(TypedDict):
    """The scientific study and treatment of defects, disorders, and malfunctions of speech and voice, as stuttering, lisping, or lalling, and of language disturbances, as aphasia or delayed language acquisition.

    References:
        https://schema.org/SpeechPathology
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(SpeechPathologyInheritedProperties , SpeechPathologyProperties, TypedDict):
    pass


class SpeechPathologyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SpeechPathology",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SpeechPathologyProperties, SpeechPathologyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SpeechPathology"
    return model
    

SpeechPathology = create_schema_org_model()


def create_speechpathology_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_speechpathology_model(model=model)
    return pydantic_type(model).schema_json()


