"""
A file containing a note, primarily for the author.

https://schema.org/NoteDigitalDocument
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NoteDigitalDocumentInheritedProperties(TypedDict):
    """A file containing a note, primarily for the author.

    References:
        https://schema.org/NoteDigitalDocument
    Note:
        Model Depth 4
    Attributes:
        hasDigitalDocumentPermission: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A permission related to the access to this document (e.g. permission to read or write an electronic document). For a public document, specify a grantee with an Audience with audienceType equal to "public".
    """

    hasDigitalDocumentPermission: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class NoteDigitalDocumentProperties(TypedDict):
    """A file containing a note, primarily for the author.

    References:
        https://schema.org/NoteDigitalDocument
    Note:
        Model Depth 4
    Attributes:
    """


class NoteDigitalDocumentAllProperties(
    NoteDigitalDocumentInheritedProperties, NoteDigitalDocumentProperties, TypedDict
):
    pass


class NoteDigitalDocumentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NoteDigitalDocument", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"hasDigitalDocumentPermission": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        NoteDigitalDocumentProperties,
        NoteDigitalDocumentInheritedProperties,
        NoteDigitalDocumentAllProperties,
    ] = NoteDigitalDocumentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NoteDigitalDocument"
    return model


NoteDigitalDocument = create_schema_org_model()


def create_notedigitaldocument_model(
    model: Union[
        NoteDigitalDocumentProperties,
        NoteDigitalDocumentInheritedProperties,
        NoteDigitalDocumentAllProperties,
    ]
):
    _type = deepcopy(NoteDigitalDocumentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of NoteDigitalDocumentAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NoteDigitalDocumentAllProperties):
    pydantic_type = create_notedigitaldocument_model(model=model)
    return pydantic_type(model).schema_json()
