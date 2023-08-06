"""
A designation by the US FDA signifying that studies in animals or humans have demonstrated fetal abnormalities and/or there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience, and the risks involved in use of the drug in pregnant women clearly outweigh potential benefits.

https://schema.org/FDAcategoryX
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FDAcategoryXInheritedProperties(TypedDict):
    """A designation by the US FDA signifying that studies in animals or humans have demonstrated fetal abnormalities and/or there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience, and the risks involved in use of the drug in pregnant women clearly outweigh potential benefits.

    References:
        https://schema.org/FDAcategoryX
    Note:
        Model Depth 6
    Attributes:
    """


class FDAcategoryXProperties(TypedDict):
    """A designation by the US FDA signifying that studies in animals or humans have demonstrated fetal abnormalities and/or there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience, and the risks involved in use of the drug in pregnant women clearly outweigh potential benefits.

    References:
        https://schema.org/FDAcategoryX
    Note:
        Model Depth 6
    Attributes:
    """


class FDAcategoryXAllProperties(
    FDAcategoryXInheritedProperties, FDAcategoryXProperties, TypedDict
):
    pass


class FDAcategoryXBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FDAcategoryX", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FDAcategoryXProperties,
        FDAcategoryXInheritedProperties,
        FDAcategoryXAllProperties,
    ] = FDAcategoryXAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FDAcategoryX"
    return model


FDAcategoryX = create_schema_org_model()


def create_fdacategoryx_model(
    model: Union[
        FDAcategoryXProperties,
        FDAcategoryXInheritedProperties,
        FDAcategoryXAllProperties,
    ]
):
    _type = deepcopy(FDAcategoryXAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of FDAcategoryXAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FDAcategoryXAllProperties):
    pydantic_type = create_fdacategoryx_model(model=model)
    return pydantic_type(model).schema_json()
