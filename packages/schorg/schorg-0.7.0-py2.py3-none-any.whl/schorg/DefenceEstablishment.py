"""
A defence establishment, such as an army or navy base.

https://schema.org/DefenceEstablishment
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DefenceEstablishmentInheritedProperties(TypedDict):
    """A defence establishment, such as an army or navy base.

    References:
        https://schema.org/DefenceEstablishment
    Note:
        Model Depth 5
    Attributes:
    """

    


class DefenceEstablishmentProperties(TypedDict):
    """A defence establishment, such as an army or navy base.

    References:
        https://schema.org/DefenceEstablishment
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(DefenceEstablishmentInheritedProperties , DefenceEstablishmentProperties, TypedDict):
    pass


class DefenceEstablishmentBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DefenceEstablishment",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DefenceEstablishmentProperties, DefenceEstablishmentInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DefenceEstablishment"
    return model
    

DefenceEstablishment = create_schema_org_model()


def create_defenceestablishment_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_defenceestablishment_model(model=model)
    return pydantic_type(model).schema_json()


