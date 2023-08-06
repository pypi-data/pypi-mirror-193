"""
Indicated that a return label must be downloaded and printed by the customer.

https://schema.org/ReturnLabelDownloadAndPrint
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnLabelDownloadAndPrintInheritedProperties(TypedDict):
    """Indicated that a return label must be downloaded and printed by the customer.

    References:
        https://schema.org/ReturnLabelDownloadAndPrint
    Note:
        Model Depth 5
    Attributes:
    """


class ReturnLabelDownloadAndPrintProperties(TypedDict):
    """Indicated that a return label must be downloaded and printed by the customer.

    References:
        https://schema.org/ReturnLabelDownloadAndPrint
    Note:
        Model Depth 5
    Attributes:
    """


class ReturnLabelDownloadAndPrintAllProperties(
    ReturnLabelDownloadAndPrintInheritedProperties,
    ReturnLabelDownloadAndPrintProperties,
    TypedDict,
):
    pass


class ReturnLabelDownloadAndPrintBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReturnLabelDownloadAndPrint", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReturnLabelDownloadAndPrintProperties,
        ReturnLabelDownloadAndPrintInheritedProperties,
        ReturnLabelDownloadAndPrintAllProperties,
    ] = ReturnLabelDownloadAndPrintAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnLabelDownloadAndPrint"
    return model


ReturnLabelDownloadAndPrint = create_schema_org_model()


def create_returnlabeldownloadandprint_model(
    model: Union[
        ReturnLabelDownloadAndPrintProperties,
        ReturnLabelDownloadAndPrintInheritedProperties,
        ReturnLabelDownloadAndPrintAllProperties,
    ]
):
    _type = deepcopy(ReturnLabelDownloadAndPrintAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ReturnLabelDownloadAndPrintAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReturnLabelDownloadAndPrintAllProperties):
    pydantic_type = create_returnlabeldownloadandprint_model(model=model)
    return pydantic_type(model).schema_json()
