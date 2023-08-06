"""
Bank or credit union.

https://schema.org/BankOrCreditUnion
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BankOrCreditUnionInheritedProperties(TypedDict):
    """Bank or credit union.

    References:
        https://schema.org/BankOrCreditUnion
    Note:
        Model Depth 5
    Attributes:
        feesAndCommissionsSpecification: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    """

    feesAndCommissionsSpecification: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]


class BankOrCreditUnionProperties(TypedDict):
    """Bank or credit union.

    References:
        https://schema.org/BankOrCreditUnion
    Note:
        Model Depth 5
    Attributes:
    """


class BankOrCreditUnionAllProperties(
    BankOrCreditUnionInheritedProperties, BankOrCreditUnionProperties, TypedDict
):
    pass


class BankOrCreditUnionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BankOrCreditUnion", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"feesAndCommissionsSpecification": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BankOrCreditUnionProperties,
        BankOrCreditUnionInheritedProperties,
        BankOrCreditUnionAllProperties,
    ] = BankOrCreditUnionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BankOrCreditUnion"
    return model


BankOrCreditUnion = create_schema_org_model()


def create_bankorcreditunion_model(
    model: Union[
        BankOrCreditUnionProperties,
        BankOrCreditUnionInheritedProperties,
        BankOrCreditUnionAllProperties,
    ]
):
    _type = deepcopy(BankOrCreditUnionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of BankOrCreditUnionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BankOrCreditUnionAllProperties):
    pydantic_type = create_bankorcreditunion_model(model=model)
    return pydantic_type(model).schema_json()
