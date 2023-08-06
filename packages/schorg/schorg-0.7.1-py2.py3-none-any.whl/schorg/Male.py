"""
The male gender.

https://schema.org/Male
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MaleInheritedProperties(TypedDict):
    """The male gender.

    References:
        https://schema.org/Male
    Note:
        Model Depth 5
    Attributes:
    """

    


class MaleProperties(TypedDict):
    """The male gender.

    References:
        https://schema.org/Male
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MaleInheritedProperties , MaleProperties, TypedDict):
    pass


class MaleBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Male",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MaleProperties, MaleInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Male"
    return model
    

Male = create_schema_org_model()


def create_male_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_male_model(model=model)
    return pydantic_type(model).schema_json()


