"""
Specifies that product returns must be done by mail.

https://schema.org/ReturnByMail
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnByMailInheritedProperties(TypedDict):
    """Specifies that product returns must be done by mail.

    References:
        https://schema.org/ReturnByMail
    Note:
        Model Depth 5
    Attributes:
    """


class ReturnByMailProperties(TypedDict):
    """Specifies that product returns must be done by mail.

    References:
        https://schema.org/ReturnByMail
    Note:
        Model Depth 5
    Attributes:
    """


class ReturnByMailAllProperties(
    ReturnByMailInheritedProperties, ReturnByMailProperties, TypedDict
):
    pass


class ReturnByMailBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReturnByMail", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReturnByMailProperties,
        ReturnByMailInheritedProperties,
        ReturnByMailAllProperties,
    ] = ReturnByMailAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnByMail"
    return model


ReturnByMail = create_schema_org_model()


def create_returnbymail_model(
    model: Union[
        ReturnByMailProperties,
        ReturnByMailInheritedProperties,
        ReturnByMailAllProperties,
    ]
):
    _type = deepcopy(ReturnByMailAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ReturnByMail. Please see: https://schema.org/ReturnByMail"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ReturnByMailAllProperties):
    pydantic_type = create_returnbymail_model(model=model)
    return pydantic_type(model).schema_json()
