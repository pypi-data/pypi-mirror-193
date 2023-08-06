"""
A spreadsheet file.

https://schema.org/SpreadsheetDigitalDocument
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SpreadsheetDigitalDocumentInheritedProperties(TypedDict):
    """A spreadsheet file.

    References:
        https://schema.org/SpreadsheetDigitalDocument
    Note:
        Model Depth 4
    Attributes:
        hasDigitalDocumentPermission: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A permission related to the access to this document (e.g. permission to read or write an electronic document). For a public document, specify a grantee with an Audience with audienceType equal to "public".
    """

    hasDigitalDocumentPermission: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class SpreadsheetDigitalDocumentProperties(TypedDict):
    """A spreadsheet file.

    References:
        https://schema.org/SpreadsheetDigitalDocument
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(SpreadsheetDigitalDocumentInheritedProperties , SpreadsheetDigitalDocumentProperties, TypedDict):
    pass


class SpreadsheetDigitalDocumentBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SpreadsheetDigitalDocument",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'hasDigitalDocumentPermission': {'exclude': True}}
        


def create_schema_org_model(type_: Union[SpreadsheetDigitalDocumentProperties, SpreadsheetDigitalDocumentInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SpreadsheetDigitalDocument"
    return model
    

SpreadsheetDigitalDocument = create_schema_org_model()


def create_spreadsheetdigitaldocument_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_spreadsheetdigitaldocument_model(model=model)
    return pydantic_type(model).schema_json()


