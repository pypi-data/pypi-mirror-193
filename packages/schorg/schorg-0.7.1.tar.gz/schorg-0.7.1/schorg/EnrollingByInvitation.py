"""
Enrolling participants by invitation only.

https://schema.org/EnrollingByInvitation
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EnrollingByInvitationInheritedProperties(TypedDict):
    """Enrolling participants by invitation only.

    References:
        https://schema.org/EnrollingByInvitation
    Note:
        Model Depth 6
    Attributes:
    """

    


class EnrollingByInvitationProperties(TypedDict):
    """Enrolling participants by invitation only.

    References:
        https://schema.org/EnrollingByInvitation
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(EnrollingByInvitationInheritedProperties , EnrollingByInvitationProperties, TypedDict):
    pass


class EnrollingByInvitationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EnrollingByInvitation",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EnrollingByInvitationProperties, EnrollingByInvitationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EnrollingByInvitation"
    return model
    

EnrollingByInvitation = create_schema_org_model()


def create_enrollingbyinvitation_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_enrollingbyinvitation_model(model=model)
    return pydantic_type(model).schema_json()


