"""
The item is dangerous and requires careful handling and/or special training of the user. See also the [UN Model Classification](https://unece.org/DAM/trans/danger/publi/unrec/rev17/English/02EREv17_Part2.pdf) defining the 9 classes of dangerous goods such as explosives, gases, flammables, and more.

https://schema.org/DangerousGoodConsideration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DangerousGoodConsiderationInheritedProperties(TypedDict):
    """The item is dangerous and requires careful handling and/or special training of the user. See also the [UN Model Classification](https://unece.org/DAM/trans/danger/publi/unrec/rev17/English/02EREv17_Part2.pdf) defining the 9 classes of dangerous goods such as explosives, gases, flammables, and more.

    References:
        https://schema.org/DangerousGoodConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class DangerousGoodConsiderationProperties(TypedDict):
    """The item is dangerous and requires careful handling and/or special training of the user. See also the [UN Model Classification](https://unece.org/DAM/trans/danger/publi/unrec/rev17/English/02EREv17_Part2.pdf) defining the 9 classes of dangerous goods such as explosives, gases, flammables, and more.

    References:
        https://schema.org/DangerousGoodConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class DangerousGoodConsiderationAllProperties(
    DangerousGoodConsiderationInheritedProperties,
    DangerousGoodConsiderationProperties,
    TypedDict,
):
    pass


class DangerousGoodConsiderationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DangerousGoodConsideration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DangerousGoodConsiderationProperties,
        DangerousGoodConsiderationInheritedProperties,
        DangerousGoodConsiderationAllProperties,
    ] = DangerousGoodConsiderationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DangerousGoodConsideration"
    return model


DangerousGoodConsideration = create_schema_org_model()


def create_dangerousgoodconsideration_model(
    model: Union[
        DangerousGoodConsiderationProperties,
        DangerousGoodConsiderationInheritedProperties,
        DangerousGoodConsiderationAllProperties,
    ]
):
    _type = deepcopy(DangerousGoodConsiderationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DangerousGoodConsiderationAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DangerousGoodConsiderationAllProperties):
    pydantic_type = create_dangerousgoodconsideration_model(model=model)
    return pydantic_type(model).schema_json()
