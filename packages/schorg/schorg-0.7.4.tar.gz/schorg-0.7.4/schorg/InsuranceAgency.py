"""
An Insurance agency.

https://schema.org/InsuranceAgency
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InsuranceAgencyInheritedProperties(TypedDict):
    """An Insurance agency.

    References:
        https://schema.org/InsuranceAgency
    Note:
        Model Depth 5
    Attributes:
        feesAndCommissionsSpecification: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    """

    feesAndCommissionsSpecification: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]


class InsuranceAgencyProperties(TypedDict):
    """An Insurance agency.

    References:
        https://schema.org/InsuranceAgency
    Note:
        Model Depth 5
    Attributes:
    """


class InsuranceAgencyAllProperties(
    InsuranceAgencyInheritedProperties, InsuranceAgencyProperties, TypedDict
):
    pass


class InsuranceAgencyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="InsuranceAgency", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"feesAndCommissionsSpecification": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        InsuranceAgencyProperties,
        InsuranceAgencyInheritedProperties,
        InsuranceAgencyAllProperties,
    ] = InsuranceAgencyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InsuranceAgency"
    return model


InsuranceAgency = create_schema_org_model()


def create_insuranceagency_model(
    model: Union[
        InsuranceAgencyProperties,
        InsuranceAgencyInheritedProperties,
        InsuranceAgencyAllProperties,
    ]
):
    _type = deepcopy(InsuranceAgencyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of InsuranceAgencyAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: InsuranceAgencyAllProperties):
    pydantic_type = create_insuranceagency_model(model=model)
    return pydantic_type(model).schema_json()
