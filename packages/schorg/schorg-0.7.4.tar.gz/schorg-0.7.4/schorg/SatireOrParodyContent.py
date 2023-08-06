"""
Content coded 'satire or parody content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'satire or parody content': A video that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)For an [[ImageObject]] to be 'satire or parody content': An image that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)For an [[ImageObject]] with embedded text to be 'satire or parody content': An image that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)For an [[AudioObject]] to be 'satire or parody content': Audio that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)

https://schema.org/SatireOrParodyContent
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SatireOrParodyContentInheritedProperties(TypedDict):
    """Content coded 'satire or parody content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'satire or parody content': A video that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)For an [[ImageObject]] to be 'satire or parody content': An image that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)For an [[ImageObject]] with embedded text to be 'satire or parody content': An image that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)For an [[AudioObject]] to be 'satire or parody content': Audio that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)

    References:
        https://schema.org/SatireOrParodyContent
    Note:
        Model Depth 5
    Attributes:
    """


class SatireOrParodyContentProperties(TypedDict):
    """Content coded 'satire or parody content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'satire or parody content': A video that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)For an [[ImageObject]] to be 'satire or parody content': An image that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)For an [[ImageObject]] with embedded text to be 'satire or parody content': An image that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)For an [[AudioObject]] to be 'satire or parody content': Audio that was created as political or humorous commentary and is presented in that context. (Reshares of satire/parody content that do not include relevant context are more likely to fall under the “missing context” rating.)

    References:
        https://schema.org/SatireOrParodyContent
    Note:
        Model Depth 5
    Attributes:
    """


class SatireOrParodyContentAllProperties(
    SatireOrParodyContentInheritedProperties, SatireOrParodyContentProperties, TypedDict
):
    pass


class SatireOrParodyContentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SatireOrParodyContent", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SatireOrParodyContentProperties,
        SatireOrParodyContentInheritedProperties,
        SatireOrParodyContentAllProperties,
    ] = SatireOrParodyContentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SatireOrParodyContent"
    return model


SatireOrParodyContent = create_schema_org_model()


def create_satireorparodycontent_model(
    model: Union[
        SatireOrParodyContentProperties,
        SatireOrParodyContentInheritedProperties,
        SatireOrParodyContentAllProperties,
    ]
):
    _type = deepcopy(SatireOrParodyContentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SatireOrParodyContentAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SatireOrParodyContentAllProperties):
    pydantic_type = create_satireorparodycontent_model(model=model)
    return pydantic_type(model).schema_json()
