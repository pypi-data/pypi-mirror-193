"""
A system of medicine based on the principle that a disease can be cured by a substance that produces similar symptoms in healthy people.

https://schema.org/Homeopathic
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HomeopathicInheritedProperties(TypedDict):
    """A system of medicine based on the principle that a disease can be cured by a substance that produces similar symptoms in healthy people.

    References:
        https://schema.org/Homeopathic
    Note:
        Model Depth 6
    Attributes:
    """

    


class HomeopathicProperties(TypedDict):
    """A system of medicine based on the principle that a disease can be cured by a substance that produces similar symptoms in healthy people.

    References:
        https://schema.org/Homeopathic
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(HomeopathicInheritedProperties , HomeopathicProperties, TypedDict):
    pass


class HomeopathicBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Homeopathic",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HomeopathicProperties, HomeopathicInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Homeopathic"
    return model
    

Homeopathic = create_schema_org_model()


def create_homeopathic_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_homeopathic_model(model=model)
    return pydantic_type(model).schema_json()


