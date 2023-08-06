"""
Item shows or promotes violence.

https://schema.org/ViolenceConsideration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ViolenceConsiderationInheritedProperties(TypedDict):
    """Item shows or promotes violence.

    References:
        https://schema.org/ViolenceConsideration
    Note:
        Model Depth 5
    Attributes:
    """

    


class ViolenceConsiderationProperties(TypedDict):
    """Item shows or promotes violence.

    References:
        https://schema.org/ViolenceConsideration
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ViolenceConsiderationInheritedProperties , ViolenceConsiderationProperties, TypedDict):
    pass


class ViolenceConsiderationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ViolenceConsideration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ViolenceConsiderationProperties, ViolenceConsiderationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ViolenceConsideration"
    return model
    

ViolenceConsideration = create_schema_org_model()


def create_violenceconsideration_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_violenceconsideration_model(model=model)
    return pydantic_type(model).schema_json()


