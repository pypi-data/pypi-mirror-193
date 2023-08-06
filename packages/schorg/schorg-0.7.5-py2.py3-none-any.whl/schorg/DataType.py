"""
The basic data types such as Integers, Strings, etc.

https://schema.org/DataType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DataTypeInheritedProperties(TypedDict):
    """The basic data types such as Integers, Strings, etc.

    References:
        https://schema.org/DataType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class DataTypeProperties(TypedDict):
    """The basic data types such as Integers, Strings, etc.

    References:
        https://schema.org/DataType
    Note:
        Model Depth 4
    Attributes:
    """


class DataTypeAllProperties(DataTypeInheritedProperties, DataTypeProperties, TypedDict):
    pass


class DataTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DataType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DataTypeProperties, DataTypeInheritedProperties, DataTypeAllProperties
    ] = DataTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DataType"
    return model


DataType = create_schema_org_model()


def create_datatype_model(
    model: Union[DataTypeProperties, DataTypeInheritedProperties, DataTypeAllProperties]
):
    _type = deepcopy(DataTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DataType. Please see: https://schema.org/DataType"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DataTypeAllProperties):
    pydantic_type = create_datatype_model(model=model)
    return pydantic_type(model).schema_json()
