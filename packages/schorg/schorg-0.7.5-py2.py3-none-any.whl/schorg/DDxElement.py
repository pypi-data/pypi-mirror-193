"""
An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.

https://schema.org/DDxElement
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DDxElementInheritedProperties(TypedDict):
    """An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.

    References:
        https://schema.org/DDxElement
    Note:
        Model Depth 4
    Attributes:
    """


class DDxElementProperties(TypedDict):
    """An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.

    References:
        https://schema.org/DDxElement
    Note:
        Model Depth 4
    Attributes:
        distinguishingSign: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): One of a set of signs and symptoms that can be used to distinguish this diagnosis from others in the differential diagnosis.
        diagnosis: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): One or more alternative conditions considered in the differential diagnosis process as output of a diagnosis process.
    """

    distinguishingSign: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    diagnosis: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class DDxElementAllProperties(
    DDxElementInheritedProperties, DDxElementProperties, TypedDict
):
    pass


class DDxElementBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DDxElement", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"distinguishingSign": {"exclude": True}}
        fields = {"diagnosis": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DDxElementProperties, DDxElementInheritedProperties, DDxElementAllProperties
    ] = DDxElementAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DDxElement"
    return model


DDxElement = create_schema_org_model()


def create_ddxelement_model(
    model: Union[
        DDxElementProperties, DDxElementInheritedProperties, DDxElementAllProperties
    ]
):
    _type = deepcopy(DDxElementAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DDxElement. Please see: https://schema.org/DDxElement"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DDxElementAllProperties):
    pydantic_type = create_ddxelement_model(model=model)
    return pydantic_type(model).schema_json()
