"""
A specific branch of medical science that pertains to diagnosis and treatment of disorders of endocrine glands and their secretions.

https://schema.org/Endocrine
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EndocrineInheritedProperties(TypedDict):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of endocrine glands and their secretions.

    References:
        https://schema.org/Endocrine
    Note:
        Model Depth 6
    Attributes:
    """

    


class EndocrineProperties(TypedDict):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of endocrine glands and their secretions.

    References:
        https://schema.org/Endocrine
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(EndocrineInheritedProperties , EndocrineProperties, TypedDict):
    pass


class EndocrineBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Endocrine",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EndocrineProperties, EndocrineInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Endocrine"
    return model
    

Endocrine = create_schema_org_model()


def create_endocrine_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_endocrine_model(model=model)
    return pydantic_type(model).schema_json()


