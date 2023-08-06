"""
Specifies that product returns must be done by mail.

https://schema.org/ReturnByMail
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(ReturnByMailInheritedProperties , ReturnByMailProperties, TypedDict):
    pass


class ReturnByMailBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReturnByMail",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReturnByMailProperties, ReturnByMailInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnByMail"
    return model
    

ReturnByMail = create_schema_org_model()


def create_returnbymail_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_returnbymail_model(model=model)
    return pydantic_type(model).schema_json()


