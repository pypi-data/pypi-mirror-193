"""
A file containing slides or used for a presentation.

https://schema.org/PresentationDigitalDocument
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PresentationDigitalDocumentInheritedProperties(TypedDict):
    """A file containing slides or used for a presentation.

    References:
        https://schema.org/PresentationDigitalDocument
    Note:
        Model Depth 4
    Attributes:
        hasDigitalDocumentPermission: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A permission related to the access to this document (e.g. permission to read or write an electronic document). For a public document, specify a grantee with an Audience with audienceType equal to "public".
    """

    hasDigitalDocumentPermission: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class PresentationDigitalDocumentProperties(TypedDict):
    """A file containing slides or used for a presentation.

    References:
        https://schema.org/PresentationDigitalDocument
    Note:
        Model Depth 4
    Attributes:
    """


class PresentationDigitalDocumentAllProperties(
    PresentationDigitalDocumentInheritedProperties,
    PresentationDigitalDocumentProperties,
    TypedDict,
):
    pass


class PresentationDigitalDocumentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PresentationDigitalDocument", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"hasDigitalDocumentPermission": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PresentationDigitalDocumentProperties,
        PresentationDigitalDocumentInheritedProperties,
        PresentationDigitalDocumentAllProperties,
    ] = PresentationDigitalDocumentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PresentationDigitalDocument"
    return model


PresentationDigitalDocument = create_schema_org_model()


def create_presentationdigitaldocument_model(
    model: Union[
        PresentationDigitalDocumentProperties,
        PresentationDigitalDocumentInheritedProperties,
        PresentationDigitalDocumentAllProperties,
    ]
):
    _type = deepcopy(PresentationDigitalDocumentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of PresentationDigitalDocument. Please see: https://schema.org/PresentationDigitalDocument"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PresentationDigitalDocumentAllProperties):
    pydantic_type = create_presentationdigitaldocument_model(model=model)
    return pydantic_type(model).schema_json()
