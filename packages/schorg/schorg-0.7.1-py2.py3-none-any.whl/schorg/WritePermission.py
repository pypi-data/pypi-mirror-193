"""
Permission to write or edit the document.

https://schema.org/WritePermission
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WritePermissionInheritedProperties(TypedDict):
    """Permission to write or edit the document.

    References:
        https://schema.org/WritePermission
    Note:
        Model Depth 5
    Attributes:
    """

    


class WritePermissionProperties(TypedDict):
    """Permission to write or edit the document.

    References:
        https://schema.org/WritePermission
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(WritePermissionInheritedProperties , WritePermissionProperties, TypedDict):
    pass


class WritePermissionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WritePermission",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WritePermissionProperties, WritePermissionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WritePermission"
    return model
    

WritePermission = create_schema_org_model()


def create_writepermission_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_writepermission_model(model=model)
    return pydantic_type(model).schema_json()


