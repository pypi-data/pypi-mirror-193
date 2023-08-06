"""
The act of inserting at the beginning if an ordered collection.

https://schema.org/PrependAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PrependActionInheritedProperties(TypedDict):
    """The act of inserting at the beginning if an ordered collection.

    References:
        https://schema.org/PrependAction
    Note:
        Model Depth 6
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class PrependActionProperties(TypedDict):
    """The act of inserting at the beginning if an ordered collection.

    References:
        https://schema.org/PrependAction
    Note:
        Model Depth 6
    Attributes:
    """


class PrependActionAllProperties(
    PrependActionInheritedProperties, PrependActionProperties, TypedDict
):
    pass


class PrependActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PrependAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"toLocation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PrependActionProperties,
        PrependActionInheritedProperties,
        PrependActionAllProperties,
    ] = PrependActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PrependAction"
    return model


PrependAction = create_schema_org_model()


def create_prependaction_model(
    model: Union[
        PrependActionProperties,
        PrependActionInheritedProperties,
        PrependActionAllProperties,
    ]
):
    _type = deepcopy(PrependActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PrependActionAllProperties):
    pydantic_type = create_prependaction_model(model=model)
    return pydantic_type(model).schema_json()
