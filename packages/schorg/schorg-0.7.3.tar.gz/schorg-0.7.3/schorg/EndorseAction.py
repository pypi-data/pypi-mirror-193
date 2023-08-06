"""
An agent approves/certifies/likes/supports/sanctions an object.

https://schema.org/EndorseAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EndorseActionInheritedProperties(TypedDict):
    """An agent approves/certifies/likes/supports/sanctions an object.

    References:
        https://schema.org/EndorseAction
    Note:
        Model Depth 5
    Attributes:
    """


class EndorseActionProperties(TypedDict):
    """An agent approves/certifies/likes/supports/sanctions an object.

    References:
        https://schema.org/EndorseAction
    Note:
        Model Depth 5
    Attributes:
        endorsee: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The person/organization being supported.
    """

    endorsee: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class EndorseActionAllProperties(
    EndorseActionInheritedProperties, EndorseActionProperties, TypedDict
):
    pass


class EndorseActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EndorseAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"endorsee": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        EndorseActionProperties,
        EndorseActionInheritedProperties,
        EndorseActionAllProperties,
    ] = EndorseActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EndorseAction"
    return model


EndorseAction = create_schema_org_model()


def create_endorseaction_model(
    model: Union[
        EndorseActionProperties,
        EndorseActionInheritedProperties,
        EndorseActionAllProperties,
    ]
):
    _type = deepcopy(EndorseActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EndorseActionAllProperties):
    pydantic_type = create_endorseaction_model(model=model)
    return pydantic_type(model).schema_json()
