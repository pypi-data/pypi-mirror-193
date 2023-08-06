"""
A designation by the US FDA signifying that there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.

https://schema.org/FDAcategoryD
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FDAcategoryDInheritedProperties(TypedDict):
    """A designation by the US FDA signifying that there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.

    References:
        https://schema.org/FDAcategoryD
    Note:
        Model Depth 6
    Attributes:
    """


class FDAcategoryDProperties(TypedDict):
    """A designation by the US FDA signifying that there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.

    References:
        https://schema.org/FDAcategoryD
    Note:
        Model Depth 6
    Attributes:
    """


class FDAcategoryDAllProperties(
    FDAcategoryDInheritedProperties, FDAcategoryDProperties, TypedDict
):
    pass


class FDAcategoryDBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FDAcategoryD", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FDAcategoryDProperties,
        FDAcategoryDInheritedProperties,
        FDAcategoryDAllProperties,
    ] = FDAcategoryDAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FDAcategoryD"
    return model


FDAcategoryD = create_schema_org_model()


def create_fdacategoryd_model(
    model: Union[
        FDAcategoryDProperties,
        FDAcategoryDInheritedProperties,
        FDAcategoryDAllProperties,
    ]
):
    _type = deepcopy(FDAcategoryDAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of FDAcategoryDAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FDAcategoryDAllProperties):
    pydantic_type = create_fdacategoryd_model(model=model)
    return pydantic_type(model).schema_json()
