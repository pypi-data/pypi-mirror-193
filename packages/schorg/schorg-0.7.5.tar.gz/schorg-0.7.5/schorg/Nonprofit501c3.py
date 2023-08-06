"""
Nonprofit501c3: Non-profit type referring to Religious, Educational, Charitable, Scientific, Literary, Testing for Public Safety, Fostering National or International Amateur Sports Competition, or Prevention of Cruelty to Children or Animals Organizations.

https://schema.org/Nonprofit501c3
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class Nonprofit501c3InheritedProperties(TypedDict):
    """Nonprofit501c3: Non-profit type referring to Religious, Educational, Charitable, Scientific, Literary, Testing for Public Safety, Fostering National or International Amateur Sports Competition, or Prevention of Cruelty to Children or Animals Organizations.

    References:
        https://schema.org/Nonprofit501c3
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c3Properties(TypedDict):
    """Nonprofit501c3: Non-profit type referring to Religious, Educational, Charitable, Scientific, Literary, Testing for Public Safety, Fostering National or International Amateur Sports Competition, or Prevention of Cruelty to Children or Animals Organizations.

    References:
        https://schema.org/Nonprofit501c3
    Note:
        Model Depth 6
    Attributes:
    """


class Nonprofit501c3AllProperties(
    Nonprofit501c3InheritedProperties, Nonprofit501c3Properties, TypedDict
):
    pass


class Nonprofit501c3BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Nonprofit501c3", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        Nonprofit501c3Properties,
        Nonprofit501c3InheritedProperties,
        Nonprofit501c3AllProperties,
    ] = Nonprofit501c3AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Nonprofit501c3"
    return model


Nonprofit501c3 = create_schema_org_model()


def create_nonprofit501c3_model(
    model: Union[
        Nonprofit501c3Properties,
        Nonprofit501c3InheritedProperties,
        Nonprofit501c3AllProperties,
    ]
):
    _type = deepcopy(Nonprofit501c3AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Nonprofit501c3. Please see: https://schema.org/Nonprofit501c3"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: Nonprofit501c3AllProperties):
    pydantic_type = create_nonprofit501c3_model(model=model)
    return pydantic_type(model).schema_json()
