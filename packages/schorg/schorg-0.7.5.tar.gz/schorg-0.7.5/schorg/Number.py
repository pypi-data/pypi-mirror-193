"""
Data type: Number.Usage guidelines:* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

https://schema.org/Number
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NumberInheritedProperties(TypedDict):
    """Data type: Number.Usage guidelines:* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

    References:
        https://schema.org/Number
    Note:
        Model Depth 5
    Attributes:
    """


class NumberProperties(TypedDict):
    """Data type: Number.Usage guidelines:* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.

    References:
        https://schema.org/Number
    Note:
        Model Depth 5
    Attributes:
    """


class NumberAllProperties(NumberInheritedProperties, NumberProperties, TypedDict):
    pass


class NumberBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Number", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NumberProperties, NumberInheritedProperties, NumberAllProperties
    ] = NumberAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Number"
    return model


Number = create_schema_org_model()


def create_number_model(
    model: Union[NumberProperties, NumberInheritedProperties, NumberAllProperties]
):
    _type = deepcopy(NumberAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Number. Please see: https://schema.org/Number"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: NumberAllProperties):
    pydantic_type = create_number_model(model=model)
    return pydantic_type(model).schema_json()
