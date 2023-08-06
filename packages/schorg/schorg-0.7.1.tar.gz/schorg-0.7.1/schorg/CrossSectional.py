"""
Studies carried out on pre-existing data (usually from 'snapshot' surveys), such as that collected by the Census Bureau. Sometimes called Prevalence Studies.

https://schema.org/CrossSectional
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CrossSectionalInheritedProperties(TypedDict):
    """Studies carried out on pre-existing data (usually from 'snapshot' surveys), such as that collected by the Census Bureau. Sometimes called Prevalence Studies.

    References:
        https://schema.org/CrossSectional
    Note:
        Model Depth 6
    Attributes:
    """

    


class CrossSectionalProperties(TypedDict):
    """Studies carried out on pre-existing data (usually from 'snapshot' surveys), such as that collected by the Census Bureau. Sometimes called Prevalence Studies.

    References:
        https://schema.org/CrossSectional
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(CrossSectionalInheritedProperties , CrossSectionalProperties, TypedDict):
    pass


class CrossSectionalBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CrossSectional",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[CrossSectionalProperties, CrossSectionalInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CrossSectional"
    return model
    

CrossSectional = create_schema_org_model()


def create_crosssectional_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_crosssectional_model(model=model)
    return pydantic_type(model).schema_json()


