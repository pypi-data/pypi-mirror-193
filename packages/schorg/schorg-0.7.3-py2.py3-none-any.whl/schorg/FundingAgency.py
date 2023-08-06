"""
A FundingAgency is an organization that implements one or more [[FundingScheme]]s and manages    the granting process (via [[Grant]]s, typically [[MonetaryGrant]]s).    A funding agency is not always required for grant funding, e.g. philanthropic giving, corporate sponsorship etc.    Examples of funding agencies include ERC, REA, NIH, Bill and Melinda Gates Foundation, ...    

https://schema.org/FundingAgency
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FundingAgencyInheritedProperties(TypedDict):
    """A FundingAgency is an organization that implements one or more [[FundingScheme]]s and manages    the granting process (via [[Grant]]s, typically [[MonetaryGrant]]s).    A funding agency is not always required for grant funding, e.g. philanthropic giving, corporate sponsorship etc.    Examples of funding agencies include ERC, REA, NIH, Bill and Melinda Gates Foundation, ...

    References:
        https://schema.org/FundingAgency
    Note:
        Model Depth 4
    Attributes:
    """


class FundingAgencyProperties(TypedDict):
    """A FundingAgency is an organization that implements one or more [[FundingScheme]]s and manages    the granting process (via [[Grant]]s, typically [[MonetaryGrant]]s).    A funding agency is not always required for grant funding, e.g. philanthropic giving, corporate sponsorship etc.    Examples of funding agencies include ERC, REA, NIH, Bill and Melinda Gates Foundation, ...

    References:
        https://schema.org/FundingAgency
    Note:
        Model Depth 4
    Attributes:
    """


class FundingAgencyAllProperties(
    FundingAgencyInheritedProperties, FundingAgencyProperties, TypedDict
):
    pass


class FundingAgencyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FundingAgency", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FundingAgencyProperties,
        FundingAgencyInheritedProperties,
        FundingAgencyAllProperties,
    ] = FundingAgencyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FundingAgency"
    return model


FundingAgency = create_schema_org_model()


def create_fundingagency_model(
    model: Union[
        FundingAgencyProperties,
        FundingAgencyInheritedProperties,
        FundingAgencyAllProperties,
    ]
):
    _type = deepcopy(FundingAgencyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FundingAgencyAllProperties):
    pydantic_type = create_fundingagency_model(model=model)
    return pydantic_type(model).schema_json()
