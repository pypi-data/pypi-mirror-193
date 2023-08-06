"""
A grant, typically financial or otherwise quantifiable, of resources. Typically a [[funder]] sponsors some [[MonetaryAmount]] to an [[Organization]] or [[Person]],    sometimes not necessarily via a dedicated or long-lived [[Project]], resulting in one or more outputs, or [[fundedItem]]s. For financial sponsorship, indicate the [[funder]] of a [[MonetaryGrant]]. For non-financial support, indicate [[sponsor]] of [[Grant]]s of resources (e.g. office space).Grants support  activities directed towards some agreed collective goals, often but not always organized as [[Project]]s. Long-lived projects are sometimes sponsored by a variety of grants over time, but it is also common for a project to be associated with a single grant.The amount of a [[Grant]] is represented using [[amount]] as a [[MonetaryAmount]].    

https://schema.org/Grant
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GrantInheritedProperties(TypedDict):
    """A grant, typically financial or otherwise quantifiable, of resources. Typically a [[funder]] sponsors some [[MonetaryAmount]] to an [[Organization]] or [[Person]],    sometimes not necessarily via a dedicated or long-lived [[Project]], resulting in one or more outputs, or [[fundedItem]]s. For financial sponsorship, indicate the [[funder]] of a [[MonetaryGrant]]. For non-financial support, indicate [[sponsor]] of [[Grant]]s of resources (e.g. office space).Grants support  activities directed towards some agreed collective goals, often but not always organized as [[Project]]s. Long-lived projects are sometimes sponsored by a variety of grants over time, but it is also common for a project to be associated with a single grant.The amount of a [[Grant]] is represented using [[amount]] as a [[MonetaryAmount]].

    References:
        https://schema.org/Grant
    Note:
        Model Depth 3
    Attributes:
    """


class GrantProperties(TypedDict):
    """A grant, typically financial or otherwise quantifiable, of resources. Typically a [[funder]] sponsors some [[MonetaryAmount]] to an [[Organization]] or [[Person]],    sometimes not necessarily via a dedicated or long-lived [[Project]], resulting in one or more outputs, or [[fundedItem]]s. For financial sponsorship, indicate the [[funder]] of a [[MonetaryGrant]]. For non-financial support, indicate [[sponsor]] of [[Grant]]s of resources (e.g. office space).Grants support  activities directed towards some agreed collective goals, often but not always organized as [[Project]]s. Long-lived projects are sometimes sponsored by a variety of grants over time, but it is also common for a project to be associated with a single grant.The amount of a [[Grant]] is represented using [[amount]] as a [[MonetaryAmount]].

    References:
        https://schema.org/Grant
    Note:
        Model Depth 3
    Attributes:
        fundedItem: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates something directly or indirectly funded or sponsored through a [[Grant]]. See also [[ownershipFundingInfo]].
        funder: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A person or organization that supports (sponsors) something through some kind of financial contribution.
        sponsor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
    """

    fundedItem: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    funder: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sponsor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class GrantAllProperties(GrantInheritedProperties, GrantProperties, TypedDict):
    pass


class GrantBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Grant", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"fundedItem": {"exclude": True}}
        fields = {"funder": {"exclude": True}}
        fields = {"sponsor": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        GrantProperties, GrantInheritedProperties, GrantAllProperties
    ] = GrantAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Grant"
    return model


Grant = create_schema_org_model()


def create_grant_model(
    model: Union[GrantProperties, GrantInheritedProperties, GrantAllProperties]
):
    _type = deepcopy(GrantAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of GrantAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GrantAllProperties):
    pydantic_type = create_grant_model(model=model)
    return pydantic_type(model).schema_json()
