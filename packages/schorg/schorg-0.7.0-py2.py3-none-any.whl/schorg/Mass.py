"""
Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of measure&gt;'. E.g., '7 kg'.

https://schema.org/Mass
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MassInheritedProperties(TypedDict):
    """Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of measure&gt;'. E.g., '7 kg'.

    References:
        https://schema.org/Mass
    Note:
        Model Depth 4
    Attributes:
    """

    


class MassProperties(TypedDict):
    """Properties that take Mass as values are of the form '&lt;Number&gt; &lt;Mass unit of measure&gt;'. E.g., '7 kg'.

    References:
        https://schema.org/Mass
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(MassInheritedProperties , MassProperties, TypedDict):
    pass


class MassBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Mass",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MassProperties, MassInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Mass"
    return model
    

Mass = create_schema_org_model()


def create_mass_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_mass_model(model=model)
    return pydantic_type(model).schema_json()


