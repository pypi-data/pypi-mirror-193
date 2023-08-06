"""
The frequency in MHz and the modulation used for a particular BroadcastService.

https://schema.org/BroadcastFrequencySpecification
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BroadcastFrequencySpecificationInheritedProperties(TypedDict):
    """The frequency in MHz and the modulation used for a particular BroadcastService.

    References:
        https://schema.org/BroadcastFrequencySpecification
    Note:
        Model Depth 3
    Attributes:
    """


class BroadcastFrequencySpecificationProperties(TypedDict):
    """The frequency in MHz and the modulation used for a particular BroadcastService.

    References:
        https://schema.org/BroadcastFrequencySpecification
    Note:
        Model Depth 3
    Attributes:
        broadcastSignalModulation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The modulation (e.g. FM, AM, etc) used by a particular broadcast service.
        broadcastSubChannel: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The subchannel used for the broadcast.
        broadcastFrequencyValue: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The frequency in MHz for a particular broadcast.
    """

    broadcastSignalModulation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    broadcastSubChannel: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    broadcastFrequencyValue: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class BroadcastFrequencySpecificationAllProperties(
    BroadcastFrequencySpecificationInheritedProperties,
    BroadcastFrequencySpecificationProperties,
    TypedDict,
):
    pass


class BroadcastFrequencySpecificationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BroadcastFrequencySpecification", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"broadcastSignalModulation": {"exclude": True}}
        fields = {"broadcastSubChannel": {"exclude": True}}
        fields = {"broadcastFrequencyValue": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BroadcastFrequencySpecificationProperties,
        BroadcastFrequencySpecificationInheritedProperties,
        BroadcastFrequencySpecificationAllProperties,
    ] = BroadcastFrequencySpecificationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BroadcastFrequencySpecification"
    return model


BroadcastFrequencySpecification = create_schema_org_model()


def create_broadcastfrequencyspecification_model(
    model: Union[
        BroadcastFrequencySpecificationProperties,
        BroadcastFrequencySpecificationInheritedProperties,
        BroadcastFrequencySpecificationAllProperties,
    ]
):
    _type = deepcopy(BroadcastFrequencySpecificationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BroadcastFrequencySpecification. Please see: https://schema.org/BroadcastFrequencySpecification"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BroadcastFrequencySpecificationAllProperties):
    pydantic_type = create_broadcastfrequencyspecification_model(model=model)
    return pydantic_type(model).schema_json()
