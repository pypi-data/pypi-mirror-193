"""
A permission for a particular person or group to access a particular file.

https://schema.org/DigitalDocumentPermission
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DigitalDocumentPermissionInheritedProperties(TypedDict):
    """A permission for a particular person or group to access a particular file.

    References:
        https://schema.org/DigitalDocumentPermission
    Note:
        Model Depth 3
    Attributes:
    """

    


class DigitalDocumentPermissionProperties(TypedDict):
    """A permission for a particular person or group to access a particular file.

    References:
        https://schema.org/DigitalDocumentPermission
    Note:
        Model Depth 3
    Attributes:
        grantee: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The person, organization, contact point, or audience that has been granted this permission.
        permissionType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The type of permission granted the person, organization, or audience.
    """

    grantee: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    permissionType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(DigitalDocumentPermissionInheritedProperties , DigitalDocumentPermissionProperties, TypedDict):
    pass


class DigitalDocumentPermissionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DigitalDocumentPermission",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'grantee': {'exclude': True}}
        fields = {'permissionType': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DigitalDocumentPermissionProperties, DigitalDocumentPermissionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DigitalDocumentPermission"
    return model
    

DigitalDocumentPermission = create_schema_org_model()


def create_digitaldocumentpermission_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_digitaldocumentpermission_model(model=model)
    return pydantic_type(model).schema_json()


