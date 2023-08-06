"""
Book format: Paperback.

https://schema.org/Paperback
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaperbackInheritedProperties(TypedDict):
    """Book format: Paperback.

    References:
        https://schema.org/Paperback
    Note:
        Model Depth 5
    Attributes:
    """

    


class PaperbackProperties(TypedDict):
    """Book format: Paperback.

    References:
        https://schema.org/Paperback
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PaperbackInheritedProperties , PaperbackProperties, TypedDict):
    pass


class PaperbackBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Paperback",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PaperbackProperties, PaperbackInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Paperback"
    return model
    

Paperback = create_schema_org_model()


def create_paperback_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_paperback_model(model=model)
    return pydantic_type(model).schema_json()


