"""
 A point value or interval for product characteristics and other purposes.

https://schema.org/QuantitativeValue
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class QuantitativeValueInheritedProperties(TypedDict):
    """A point value or interval for product characteristics and other purposes.

    References:
        https://schema.org/QuantitativeValue
    Note:
        Model Depth 4
    Attributes:
    """


class QuantitativeValueProperties(TypedDict):
    """A point value or interval for product characteristics and other purposes.

    References:
        https://schema.org/QuantitativeValue
    Note:
        Model Depth 4
    Attributes:
        value: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, StrictInt, StrictFloat, str]], StrictBool, SchemaOrgObj, StrictInt, StrictFloat, str]]): The value of the quantitative value or property value node.* For [[QuantitativeValue]] and [[MonetaryAmount]], the recommended type for values is 'Number'.* For [[PropertyValue]], it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'.* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        additionalProperty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
        valueReference: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A secondary value that provides additional information on the original value, e.g. a reference temperature or a type of measurement.
        unitCode: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.
        maxValue: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The upper value of some characteristic or property.
        unitText: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for<a href='unitCode'>unitCode</a>.
        minValue: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The lower value of some characteristic or property.
    """

    value: NotRequired[
        Union[
            List[Union[StrictBool, SchemaOrgObj, StrictInt, StrictFloat, str]],
            StrictBool,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
            str,
        ]
    ]
    additionalProperty: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    valueReference: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    unitCode: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    maxValue: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    unitText: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    minValue: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class QuantitativeValueAllProperties(
    QuantitativeValueInheritedProperties, QuantitativeValueProperties, TypedDict
):
    pass


class QuantitativeValueBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="QuantitativeValue", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"value": {"exclude": True}}
        fields = {"additionalProperty": {"exclude": True}}
        fields = {"valueReference": {"exclude": True}}
        fields = {"unitCode": {"exclude": True}}
        fields = {"maxValue": {"exclude": True}}
        fields = {"unitText": {"exclude": True}}
        fields = {"minValue": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        QuantitativeValueProperties,
        QuantitativeValueInheritedProperties,
        QuantitativeValueAllProperties,
    ] = QuantitativeValueAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "QuantitativeValue"
    return model


QuantitativeValue = create_schema_org_model()


def create_quantitativevalue_model(
    model: Union[
        QuantitativeValueProperties,
        QuantitativeValueInheritedProperties,
        QuantitativeValueAllProperties,
    ]
):
    _type = deepcopy(QuantitativeValueAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of QuantitativeValue. Please see: https://schema.org/QuantitativeValue"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: QuantitativeValueAllProperties):
    pydantic_type = create_quantitativevalue_model(model=model)
    return pydantic_type(model).schema_json()
