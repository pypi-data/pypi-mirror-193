"""
The act of committing to/adopting an object.Related actions:* [[RejectAction]]: The antonym of AcceptAction.

https://schema.org/AcceptAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AcceptActionInheritedProperties(TypedDict):
    """The act of committing to/adopting an object.Related actions:* [[RejectAction]]: The antonym of AcceptAction.

    References:
        https://schema.org/AcceptAction
    Note:
        Model Depth 5
    Attributes:
    """


class AcceptActionProperties(TypedDict):
    """The act of committing to/adopting an object.Related actions:* [[RejectAction]]: The antonym of AcceptAction.

    References:
        https://schema.org/AcceptAction
    Note:
        Model Depth 5
    Attributes:
    """


class AcceptActionAllProperties(
    AcceptActionInheritedProperties, AcceptActionProperties, TypedDict
):
    pass


class AcceptActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AcceptAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AcceptActionProperties,
        AcceptActionInheritedProperties,
        AcceptActionAllProperties,
    ] = AcceptActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AcceptAction"
    return model


AcceptAction = create_schema_org_model()


def create_acceptaction_model(
    model: Union[
        AcceptActionProperties,
        AcceptActionInheritedProperties,
        AcceptActionAllProperties,
    ]
):
    _type = deepcopy(AcceptActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AcceptActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AcceptActionAllProperties):
    pydantic_type = create_acceptaction_model(model=model)
    return pydantic_type(model).schema_json()
