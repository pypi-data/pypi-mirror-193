"""
A spreadsheet file.

https://schema.org/SpreadsheetDigitalDocument
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SpreadsheetDigitalDocumentInheritedProperties(TypedDict):
    """A spreadsheet file.

    References:
        https://schema.org/SpreadsheetDigitalDocument
    Note:
        Model Depth 4
    Attributes:
        hasDigitalDocumentPermission: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A permission related to the access to this document (e.g. permission to read or write an electronic document). For a public document, specify a grantee with an Audience with audienceType equal to "public".
    """

    hasDigitalDocumentPermission: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class SpreadsheetDigitalDocumentProperties(TypedDict):
    """A spreadsheet file.

    References:
        https://schema.org/SpreadsheetDigitalDocument
    Note:
        Model Depth 4
    Attributes:
    """


class SpreadsheetDigitalDocumentAllProperties(
    SpreadsheetDigitalDocumentInheritedProperties,
    SpreadsheetDigitalDocumentProperties,
    TypedDict,
):
    pass


class SpreadsheetDigitalDocumentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SpreadsheetDigitalDocument", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"hasDigitalDocumentPermission": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        SpreadsheetDigitalDocumentProperties,
        SpreadsheetDigitalDocumentInheritedProperties,
        SpreadsheetDigitalDocumentAllProperties,
    ] = SpreadsheetDigitalDocumentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SpreadsheetDigitalDocument"
    return model


SpreadsheetDigitalDocument = create_schema_org_model()


def create_spreadsheetdigitaldocument_model(
    model: Union[
        SpreadsheetDigitalDocumentProperties,
        SpreadsheetDigitalDocumentInheritedProperties,
        SpreadsheetDigitalDocumentAllProperties,
    ]
):
    _type = deepcopy(SpreadsheetDigitalDocumentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of SpreadsheetDigitalDocument. Please see: https://schema.org/SpreadsheetDigitalDocument"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: SpreadsheetDigitalDocumentAllProperties):
    pydantic_type = create_spreadsheetdigitaldocument_model(model=model)
    return pydantic_type(model).schema_json()
