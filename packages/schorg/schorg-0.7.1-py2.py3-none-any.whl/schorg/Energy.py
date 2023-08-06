"""
Properties that take Energy as values are of the form '&lt;Number&gt; &lt;Energy unit of measure&gt;'.

https://schema.org/Energy
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EnergyInheritedProperties(TypedDict):
    """Properties that take Energy as values are of the form '&lt;Number&gt; &lt;Energy unit of measure&gt;'.

    References:
        https://schema.org/Energy
    Note:
        Model Depth 4
    Attributes:
    """

    


class EnergyProperties(TypedDict):
    """Properties that take Energy as values are of the form '&lt;Number&gt; &lt;Energy unit of measure&gt;'.

    References:
        https://schema.org/Energy
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(EnergyInheritedProperties , EnergyProperties, TypedDict):
    pass


class EnergyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Energy",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EnergyProperties, EnergyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Energy"
    return model
    

Energy = create_schema_org_model()


def create_energy_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_energy_model(model=model)
    return pydantic_type(model).schema_json()


