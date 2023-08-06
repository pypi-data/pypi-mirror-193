"""
ATM/cash machine.

https://schema.org/AutomatedTeller
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AutomatedTellerInheritedProperties(TypedDict):
    """ATM/cash machine.

    References:
        https://schema.org/AutomatedTeller
    Note:
        Model Depth 5
    Attributes:
        feesAndCommissionsSpecification: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    """

    feesAndCommissionsSpecification: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]


class AutomatedTellerProperties(TypedDict):
    """ATM/cash machine.

    References:
        https://schema.org/AutomatedTeller
    Note:
        Model Depth 5
    Attributes:
    """


class AutomatedTellerAllProperties(
    AutomatedTellerInheritedProperties, AutomatedTellerProperties, TypedDict
):
    pass


class AutomatedTellerBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AutomatedTeller", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"feesAndCommissionsSpecification": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        AutomatedTellerProperties,
        AutomatedTellerInheritedProperties,
        AutomatedTellerAllProperties,
    ] = AutomatedTellerAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AutomatedTeller"
    return model


AutomatedTeller = create_schema_org_model()


def create_automatedteller_model(
    model: Union[
        AutomatedTellerProperties,
        AutomatedTellerInheritedProperties,
        AutomatedTellerAllProperties,
    ]
):
    _type = deepcopy(AutomatedTellerAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of AutomatedTeller. Please see: https://schema.org/AutomatedTeller"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: AutomatedTellerAllProperties):
    pydantic_type = create_automatedteller_model(model=model)
    return pydantic_type(model).schema_json()
