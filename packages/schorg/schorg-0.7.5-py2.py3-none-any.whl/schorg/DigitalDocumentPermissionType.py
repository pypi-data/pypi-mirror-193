"""
A type of permission which can be granted for accessing a digital document.

https://schema.org/DigitalDocumentPermissionType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DigitalDocumentPermissionTypeInheritedProperties(TypedDict):
    """A type of permission which can be granted for accessing a digital document.

    References:
        https://schema.org/DigitalDocumentPermissionType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class DigitalDocumentPermissionTypeProperties(TypedDict):
    """A type of permission which can be granted for accessing a digital document.

    References:
        https://schema.org/DigitalDocumentPermissionType
    Note:
        Model Depth 4
    Attributes:
    """


class DigitalDocumentPermissionTypeAllProperties(
    DigitalDocumentPermissionTypeInheritedProperties,
    DigitalDocumentPermissionTypeProperties,
    TypedDict,
):
    pass


class DigitalDocumentPermissionTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DigitalDocumentPermissionType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DigitalDocumentPermissionTypeProperties,
        DigitalDocumentPermissionTypeInheritedProperties,
        DigitalDocumentPermissionTypeAllProperties,
    ] = DigitalDocumentPermissionTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DigitalDocumentPermissionType"
    return model


DigitalDocumentPermissionType = create_schema_org_model()


def create_digitaldocumentpermissiontype_model(
    model: Union[
        DigitalDocumentPermissionTypeProperties,
        DigitalDocumentPermissionTypeInheritedProperties,
        DigitalDocumentPermissionTypeAllProperties,
    ]
):
    _type = deepcopy(DigitalDocumentPermissionTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DigitalDocumentPermissionType. Please see: https://schema.org/DigitalDocumentPermissionType"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DigitalDocumentPermissionTypeAllProperties):
    pydantic_type = create_digitaldocumentpermissiontype_model(model=model)
    return pydantic_type(model).schema_json()
