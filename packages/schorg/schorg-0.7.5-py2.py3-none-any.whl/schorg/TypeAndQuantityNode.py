"""
A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer.

https://schema.org/TypeAndQuantityNode
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TypeAndQuantityNodeInheritedProperties(TypedDict):
    """A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer.

    References:
        https://schema.org/TypeAndQuantityNode
    Note:
        Model Depth 4
    Attributes:
    """


class TypeAndQuantityNodeProperties(TypedDict):
    """A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer.

    References:
        https://schema.org/TypeAndQuantityNode
    Note:
        Model Depth 4
    Attributes:
        amountOfThisGood: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The quantity of the goods included in the offer.
        businessFunction: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.
        unitCode: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.
        unitText: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for<a href='unitCode'>unitCode</a>.
        typeOfGood: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The product that this structured value is referring to.
    """

    amountOfThisGood: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    businessFunction: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    unitCode: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    unitText: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    typeOfGood: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class TypeAndQuantityNodeAllProperties(
    TypeAndQuantityNodeInheritedProperties, TypeAndQuantityNodeProperties, TypedDict
):
    pass


class TypeAndQuantityNodeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TypeAndQuantityNode", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"amountOfThisGood": {"exclude": True}}
        fields = {"businessFunction": {"exclude": True}}
        fields = {"unitCode": {"exclude": True}}
        fields = {"unitText": {"exclude": True}}
        fields = {"typeOfGood": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        TypeAndQuantityNodeProperties,
        TypeAndQuantityNodeInheritedProperties,
        TypeAndQuantityNodeAllProperties,
    ] = TypeAndQuantityNodeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TypeAndQuantityNode"
    return model


TypeAndQuantityNode = create_schema_org_model()


def create_typeandquantitynode_model(
    model: Union[
        TypeAndQuantityNodeProperties,
        TypeAndQuantityNodeInheritedProperties,
        TypeAndQuantityNodeAllProperties,
    ]
):
    _type = deepcopy(TypeAndQuantityNodeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TypeAndQuantityNode. Please see: https://schema.org/TypeAndQuantityNode"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TypeAndQuantityNodeAllProperties):
    pydantic_type = create_typeandquantitynode_model(model=model)
    return pydantic_type(model).schema_json()
