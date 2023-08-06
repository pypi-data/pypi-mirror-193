"""
A case series (also known as a clinical series) is a medical research study that tracks patients with a known exposure given similar treatment or examines their medical records for exposure and outcome. A case series can be retrospective or prospective and usually involves a smaller number of patients than the more powerful case-control studies or randomized controlled trials. Case series may be consecutive or non-consecutive, depending on whether all cases presenting to the reporting authors over a period of time were included, or only a selection.

https://schema.org/CaseSeries
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CaseSeriesInheritedProperties(TypedDict):
    """A case series (also known as a clinical series) is a medical research study that tracks patients with a known exposure given similar treatment or examines their medical records for exposure and outcome. A case series can be retrospective or prospective and usually involves a smaller number of patients than the more powerful case-control studies or randomized controlled trials. Case series may be consecutive or non-consecutive, depending on whether all cases presenting to the reporting authors over a period of time were included, or only a selection.

    References:
        https://schema.org/CaseSeries
    Note:
        Model Depth 6
    Attributes:
    """


class CaseSeriesProperties(TypedDict):
    """A case series (also known as a clinical series) is a medical research study that tracks patients with a known exposure given similar treatment or examines their medical records for exposure and outcome. A case series can be retrospective or prospective and usually involves a smaller number of patients than the more powerful case-control studies or randomized controlled trials. Case series may be consecutive or non-consecutive, depending on whether all cases presenting to the reporting authors over a period of time were included, or only a selection.

    References:
        https://schema.org/CaseSeries
    Note:
        Model Depth 6
    Attributes:
    """


class CaseSeriesAllProperties(
    CaseSeriesInheritedProperties, CaseSeriesProperties, TypedDict
):
    pass


class CaseSeriesBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CaseSeries", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CaseSeriesProperties, CaseSeriesInheritedProperties, CaseSeriesAllProperties
    ] = CaseSeriesAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CaseSeries"
    return model


CaseSeries = create_schema_org_model()


def create_caseseries_model(
    model: Union[
        CaseSeriesProperties, CaseSeriesInheritedProperties, CaseSeriesAllProperties
    ]
):
    _type = deepcopy(CaseSeriesAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CaseSeriesAllProperties):
    pydantic_type = create_caseseries_model(model=model)
    return pydantic_type(model).schema_json()
