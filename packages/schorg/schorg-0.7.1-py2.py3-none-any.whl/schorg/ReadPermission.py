"""
Permission to read or view the document.

https://schema.org/ReadPermission
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReadPermissionInheritedProperties(TypedDict):
    """Permission to read or view the document.

    References:
        https://schema.org/ReadPermission
    Note:
        Model Depth 5
    Attributes:
    """

    


class ReadPermissionProperties(TypedDict):
    """Permission to read or view the document.

    References:
        https://schema.org/ReadPermission
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ReadPermissionInheritedProperties , ReadPermissionProperties, TypedDict):
    pass


class ReadPermissionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReadPermission",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReadPermissionProperties, ReadPermissionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReadPermission"
    return model
    

ReadPermission = create_schema_org_model()


def create_readpermission_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_readpermission_model(model=model)
    return pydantic_type(model).schema_json()


