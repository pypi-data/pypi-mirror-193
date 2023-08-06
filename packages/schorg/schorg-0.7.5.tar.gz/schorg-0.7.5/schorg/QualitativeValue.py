"""
A predefined value for a product characteristic, e.g. the power cord plug type 'US' or the garment sizes 'S', 'M', 'L', and 'XL'.

https://schema.org/QualitativeValue
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class QualitativeValueInheritedProperties(TypedDict):
    """A predefined value for a product characteristic, e.g. the power cord plug type 'US' or the garment sizes 'S', 'M', 'L', and 'XL'.

    References:
        https://schema.org/QualitativeValue
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class QualitativeValueProperties(TypedDict):
    """A predefined value for a product characteristic, e.g. the power cord plug type 'US' or the garment sizes 'S', 'M', 'L', and 'XL'.

    References:
        https://schema.org/QualitativeValue
    Note:
        Model Depth 4
    Attributes:
        greater: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This ordering relation for qualitative values indicates that the subject is greater than the object.
        additionalProperty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
        valueReference: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A secondary value that provides additional information on the original value, e.g. a reference temperature or a type of measurement.
        equal: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This ordering relation for qualitative values indicates that the subject is equal to the object.
        lesser: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This ordering relation for qualitative values indicates that the subject is lesser than the object.
        greaterOrEqual: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This ordering relation for qualitative values indicates that the subject is greater than or equal to the object.
        lesserOrEqual: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This ordering relation for qualitative values indicates that the subject is lesser than or equal to the object.
        nonEqual: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This ordering relation for qualitative values indicates that the subject is not equal to the object.
    """

    greater: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    additionalProperty: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    valueReference: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    equal: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    lesser: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    greaterOrEqual: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    lesserOrEqual: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    nonEqual: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class QualitativeValueAllProperties(
    QualitativeValueInheritedProperties, QualitativeValueProperties, TypedDict
):
    pass


class QualitativeValueBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="QualitativeValue", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}
        fields = {"greater": {"exclude": True}}
        fields = {"additionalProperty": {"exclude": True}}
        fields = {"valueReference": {"exclude": True}}
        fields = {"equal": {"exclude": True}}
        fields = {"lesser": {"exclude": True}}
        fields = {"greaterOrEqual": {"exclude": True}}
        fields = {"lesserOrEqual": {"exclude": True}}
        fields = {"nonEqual": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        QualitativeValueProperties,
        QualitativeValueInheritedProperties,
        QualitativeValueAllProperties,
    ] = QualitativeValueAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "QualitativeValue"
    return model


QualitativeValue = create_schema_org_model()


def create_qualitativevalue_model(
    model: Union[
        QualitativeValueProperties,
        QualitativeValueInheritedProperties,
        QualitativeValueAllProperties,
    ]
):
    _type = deepcopy(QualitativeValueAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of QualitativeValue. Please see: https://schema.org/QualitativeValue"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: QualitativeValueAllProperties):
    pydantic_type = create_qualitativevalue_model(model=model)
    return pydantic_type(model).schema_json()
