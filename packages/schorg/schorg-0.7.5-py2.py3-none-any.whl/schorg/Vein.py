"""
A type of blood vessel that specifically carries blood to the heart.

https://schema.org/Vein
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VeinInheritedProperties(TypedDict):
    """A type of blood vessel that specifically carries blood to the heart.

    References:
        https://schema.org/Vein
    Note:
        Model Depth 5
    Attributes:
    """


class VeinProperties(TypedDict):
    """A type of blood vessel that specifically carries blood to the heart.

    References:
        https://schema.org/Vein
    Note:
        Model Depth 5
    Attributes:
        tributary: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The anatomical or organ system that the vein flows into; a larger structure that the vein connects to.
        regionDrained: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The anatomical or organ system drained by this vessel; generally refers to a specific part of an organ.
        drainsTo: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The vasculature that the vein drains into.
    """

    tributary: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    regionDrained: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    drainsTo: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class VeinAllProperties(VeinInheritedProperties, VeinProperties, TypedDict):
    pass


class VeinBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Vein", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"tributary": {"exclude": True}}
        fields = {"regionDrained": {"exclude": True}}
        fields = {"drainsTo": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        VeinProperties, VeinInheritedProperties, VeinAllProperties
    ] = VeinAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Vein"
    return model


Vein = create_schema_org_model()


def create_vein_model(
    model: Union[VeinProperties, VeinInheritedProperties, VeinAllProperties]
):
    _type = deepcopy(VeinAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Vein. Please see: https://schema.org/Vein"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: VeinAllProperties):
    pydantic_type = create_vein_model(model=model)
    return pydantic_type(model).schema_json()
