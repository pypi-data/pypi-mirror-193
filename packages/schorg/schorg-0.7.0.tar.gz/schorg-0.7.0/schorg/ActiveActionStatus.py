"""
An in-progress action (e.g., while watching the movie, or driving to a location).

https://schema.org/ActiveActionStatus
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ActiveActionStatusInheritedProperties(TypedDict):
    """An in-progress action (e.g., while watching the movie, or driving to a location).

    References:
        https://schema.org/ActiveActionStatus
    Note:
        Model Depth 6
    Attributes:
    """

    


class ActiveActionStatusProperties(TypedDict):
    """An in-progress action (e.g., while watching the movie, or driving to a location).

    References:
        https://schema.org/ActiveActionStatus
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(ActiveActionStatusInheritedProperties , ActiveActionStatusProperties, TypedDict):
    pass


class ActiveActionStatusBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ActiveActionStatus",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ActiveActionStatusProperties, ActiveActionStatusInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ActiveActionStatus"
    return model
    

ActiveActionStatus = create_schema_org_model()


def create_activeactionstatus_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_activeactionstatus_model(model=model)
    return pydantic_type(model).schema_json()


