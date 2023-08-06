"""
A type of permission which can be granted for accessing a digital document.

https://schema.org/DigitalDocumentPermissionType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DigitalDocumentPermissionTypeInheritedProperties(TypedDict):
    """A type of permission which can be granted for accessing a digital document.

    References:
        https://schema.org/DigitalDocumentPermissionType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class DigitalDocumentPermissionTypeProperties(TypedDict):
    """A type of permission which can be granted for accessing a digital document.

    References:
        https://schema.org/DigitalDocumentPermissionType
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(DigitalDocumentPermissionTypeInheritedProperties , DigitalDocumentPermissionTypeProperties, TypedDict):
    pass


class DigitalDocumentPermissionTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DigitalDocumentPermissionType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DigitalDocumentPermissionTypeProperties, DigitalDocumentPermissionTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DigitalDocumentPermissionType"
    return model
    

DigitalDocumentPermissionType = create_schema_org_model()


def create_digitaldocumentpermissiontype_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_digitaldocumentpermissiontype_model(model=model)
    return pydantic_type(model).schema_json()


