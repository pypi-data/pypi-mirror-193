"""
Indicates that the publisher gives some special status to the publication of the document. ("The Queens Printer" version of a UK Act of Parliament, or the PDF version of a Directive published by the EU Office of Publications.) Something "Authoritative" is considered to be also [[OfficialLegalValue]].

https://schema.org/AuthoritativeLegalValue
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AuthoritativeLegalValueInheritedProperties(TypedDict):
    """Indicates that the publisher gives some special status to the publication of the document. ("The Queens Printer" version of a UK Act of Parliament, or the PDF version of a Directive published by the EU Office of Publications.) Something "Authoritative" is considered to be also [[OfficialLegalValue]].

    References:
        https://schema.org/AuthoritativeLegalValue
    Note:
        Model Depth 5
    Attributes:
    """


class AuthoritativeLegalValueProperties(TypedDict):
    """Indicates that the publisher gives some special status to the publication of the document. ("The Queens Printer" version of a UK Act of Parliament, or the PDF version of a Directive published by the EU Office of Publications.) Something "Authoritative" is considered to be also [[OfficialLegalValue]].

    References:
        https://schema.org/AuthoritativeLegalValue
    Note:
        Model Depth 5
    Attributes:
    """


class AuthoritativeLegalValueAllProperties(
    AuthoritativeLegalValueInheritedProperties,
    AuthoritativeLegalValueProperties,
    TypedDict,
):
    pass


class AuthoritativeLegalValueBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AuthoritativeLegalValue", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AuthoritativeLegalValueProperties,
        AuthoritativeLegalValueInheritedProperties,
        AuthoritativeLegalValueAllProperties,
    ] = AuthoritativeLegalValueAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AuthoritativeLegalValue"
    return model


AuthoritativeLegalValue = create_schema_org_model()


def create_authoritativelegalvalue_model(
    model: Union[
        AuthoritativeLegalValueProperties,
        AuthoritativeLegalValueInheritedProperties,
        AuthoritativeLegalValueAllProperties,
    ]
):
    _type = deepcopy(AuthoritativeLegalValueAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AuthoritativeLegalValueAllProperties):
    pydantic_type = create_authoritativelegalvalue_model(model=model)
    return pydantic_type(model).schema_json()
