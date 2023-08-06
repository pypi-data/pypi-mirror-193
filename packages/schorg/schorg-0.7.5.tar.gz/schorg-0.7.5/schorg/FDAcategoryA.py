"""
A designation by the US FDA signifying that adequate and well-controlled studies have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of risk in later trimesters).

https://schema.org/FDAcategoryA
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FDAcategoryAInheritedProperties(TypedDict):
    """A designation by the US FDA signifying that adequate and well-controlled studies have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of risk in later trimesters).

    References:
        https://schema.org/FDAcategoryA
    Note:
        Model Depth 6
    Attributes:
    """


class FDAcategoryAProperties(TypedDict):
    """A designation by the US FDA signifying that adequate and well-controlled studies have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of risk in later trimesters).

    References:
        https://schema.org/FDAcategoryA
    Note:
        Model Depth 6
    Attributes:
    """


class FDAcategoryAAllProperties(
    FDAcategoryAInheritedProperties, FDAcategoryAProperties, TypedDict
):
    pass


class FDAcategoryABaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FDAcategoryA", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FDAcategoryAProperties,
        FDAcategoryAInheritedProperties,
        FDAcategoryAAllProperties,
    ] = FDAcategoryAAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FDAcategoryA"
    return model


FDAcategoryA = create_schema_org_model()


def create_fdacategorya_model(
    model: Union[
        FDAcategoryAProperties,
        FDAcategoryAInheritedProperties,
        FDAcategoryAAllProperties,
    ]
):
    _type = deepcopy(FDAcategoryAAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of FDAcategoryA. Please see: https://schema.org/FDAcategoryA"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: FDAcategoryAAllProperties):
    pydantic_type = create_fdacategorya_model(model=model)
    return pydantic_type(model).schema_json()
