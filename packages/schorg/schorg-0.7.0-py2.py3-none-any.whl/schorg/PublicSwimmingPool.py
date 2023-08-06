"""
A public swimming pool.

https://schema.org/PublicSwimmingPool
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PublicSwimmingPoolInheritedProperties(TypedDict):
    """A public swimming pool.

    References:
        https://schema.org/PublicSwimmingPool
    Note:
        Model Depth 5
    Attributes:
    """

    


class PublicSwimmingPoolProperties(TypedDict):
    """A public swimming pool.

    References:
        https://schema.org/PublicSwimmingPool
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PublicSwimmingPoolInheritedProperties , PublicSwimmingPoolProperties, TypedDict):
    pass


class PublicSwimmingPoolBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PublicSwimmingPool",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PublicSwimmingPoolProperties, PublicSwimmingPoolInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PublicSwimmingPool"
    return model
    

PublicSwimmingPool = create_schema_org_model()


def create_publicswimmingpool_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_publicswimmingpool_model(model=model)
    return pydantic_type(model).schema_json()


