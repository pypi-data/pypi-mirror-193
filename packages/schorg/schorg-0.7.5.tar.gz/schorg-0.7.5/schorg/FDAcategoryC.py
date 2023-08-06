"""
A designation by the US FDA signifying that animal reproduction studies have shown an adverse effect on the fetus and there are no adequate and well-controlled studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.

https://schema.org/FDAcategoryC
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FDAcategoryCInheritedProperties(TypedDict):
    """A designation by the US FDA signifying that animal reproduction studies have shown an adverse effect on the fetus and there are no adequate and well-controlled studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.

    References:
        https://schema.org/FDAcategoryC
    Note:
        Model Depth 6
    Attributes:
    """


class FDAcategoryCProperties(TypedDict):
    """A designation by the US FDA signifying that animal reproduction studies have shown an adverse effect on the fetus and there are no adequate and well-controlled studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.

    References:
        https://schema.org/FDAcategoryC
    Note:
        Model Depth 6
    Attributes:
    """


class FDAcategoryCAllProperties(
    FDAcategoryCInheritedProperties, FDAcategoryCProperties, TypedDict
):
    pass


class FDAcategoryCBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FDAcategoryC", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FDAcategoryCProperties,
        FDAcategoryCInheritedProperties,
        FDAcategoryCAllProperties,
    ] = FDAcategoryCAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FDAcategoryC"
    return model


FDAcategoryC = create_schema_org_model()


def create_fdacategoryc_model(
    model: Union[
        FDAcategoryCProperties,
        FDAcategoryCInheritedProperties,
        FDAcategoryCAllProperties,
    ]
):
    _type = deepcopy(FDAcategoryCAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of FDAcategoryC. Please see: https://schema.org/FDAcategoryC"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: FDAcategoryCAllProperties):
    pydantic_type = create_fdacategoryc_model(model=model)
    return pydantic_type(model).schema_json()
