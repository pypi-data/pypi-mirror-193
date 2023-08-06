"""
Studies carried out on pre-existing data (usually from 'snapshot' surveys), such as that collected by the Census Bureau. Sometimes called Prevalence Studies.

https://schema.org/CrossSectional
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class CrossSectionalAllProperties(
    CrossSectionalInheritedProperties, CrossSectionalProperties, TypedDict
):
    pass


class CrossSectionalBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CrossSectional", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CrossSectionalProperties,
        CrossSectionalInheritedProperties,
        CrossSectionalAllProperties,
    ] = CrossSectionalAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CrossSectional"
    return model


CrossSectional = create_schema_org_model()


def create_crosssectional_model(
    model: Union[
        CrossSectionalProperties,
        CrossSectionalInheritedProperties,
        CrossSectionalAllProperties,
    ]
):
    _type = deepcopy(CrossSectionalAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of CrossSectional. Please see: https://schema.org/CrossSectional"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CrossSectionalAllProperties):
    pydantic_type = create_crosssectional_model(model=model)
    return pydantic_type(model).schema_json()
