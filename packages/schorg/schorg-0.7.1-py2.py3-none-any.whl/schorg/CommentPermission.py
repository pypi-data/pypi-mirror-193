"""
Permission to add comments to the document.

https://schema.org/CommentPermission
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CommentPermissionInheritedProperties(TypedDict):
    """Permission to add comments to the document.

    References:
        https://schema.org/CommentPermission
    Note:
        Model Depth 5
    Attributes:
    """

    


class CommentPermissionProperties(TypedDict):
    """Permission to add comments to the document.

    References:
        https://schema.org/CommentPermission
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(CommentPermissionInheritedProperties , CommentPermissionProperties, TypedDict):
    pass


class CommentPermissionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CommentPermission",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[CommentPermissionProperties, CommentPermissionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CommentPermission"
    return model
    

CommentPermission = create_schema_org_model()


def create_commentpermission_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_commentpermission_model(model=model)
    return pydantic_type(model).schema_json()


