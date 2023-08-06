"""
Instances of the class [[Observation]] are used to specify observations about an entity (which may or may not be an instance of a [[StatisticalPopulation]]), at a particular time. The principal properties of an [[Observation]] are [[observedNode]], [[measuredProperty]], [[measuredValue]] (or [[median]], etc.) and [[observationDate]] ([[measuredProperty]] properties can, but need not always, be W3C RDF Data Cube "measure properties", as in the [lifeExpectancy example](https://www.w3.org/TR/vocab-data-cube/#dsd-example)).See also [[StatisticalPopulation]], and the [data and datasets](/docs/data-and-datasets.html) overview for more details.  

https://schema.org/Observation
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ObservationInheritedProperties(TypedDict):
    """Instances of the class [[Observation]] are used to specify observations about an entity (which may or may not be an instance of a [[StatisticalPopulation]]), at a particular time. The principal properties of an [[Observation]] are [[observedNode]], [[measuredProperty]], [[measuredValue]] (or [[median]], etc.) and [[observationDate]] ([[measuredProperty]] properties can, but need not always, be W3C RDF Data Cube "measure properties", as in the [lifeExpectancy example](https://www.w3.org/TR/vocab-data-cube/#dsd-example)).See also [[StatisticalPopulation]], and the [data and datasets](/docs/data-and-datasets.html) overview for more details.

    References:
        https://schema.org/Observation
    Note:
        Model Depth 3
    Attributes:
    """


class ObservationProperties(TypedDict):
    """Instances of the class [[Observation]] are used to specify observations about an entity (which may or may not be an instance of a [[StatisticalPopulation]]), at a particular time. The principal properties of an [[Observation]] are [[observedNode]], [[measuredProperty]], [[measuredValue]] (or [[median]], etc.) and [[observationDate]] ([[measuredProperty]] properties can, but need not always, be W3C RDF Data Cube "measure properties", as in the [lifeExpectancy example](https://www.w3.org/TR/vocab-data-cube/#dsd-example)).See also [[StatisticalPopulation]], and the [data and datasets](/docs/data-and-datasets.html) overview for more details.

    References:
        https://schema.org/Observation
    Note:
        Model Depth 3
    Attributes:
        observedNode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The observedNode of an [[Observation]], often a [[StatisticalPopulation]].
        marginOfError: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A marginOfError for an [[Observation]].
        measuredValue: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The measuredValue of an [[Observation]].
        observationDate: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The observationDate of an [[Observation]].
        measuredProperty: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The measuredProperty of an [[Observation]], either a schema.org property, a property from other RDF-compatible systems, e.g. W3C RDF Data Cube, or schema.org extensions such as [GS1's](https://www.gs1.org/voc/?show=properties).
    """

    observedNode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    marginOfError: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    measuredValue: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    observationDate: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    measuredProperty: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class ObservationAllProperties(
    ObservationInheritedProperties, ObservationProperties, TypedDict
):
    pass


class ObservationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Observation", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"observedNode": {"exclude": True}}
        fields = {"marginOfError": {"exclude": True}}
        fields = {"measuredValue": {"exclude": True}}
        fields = {"observationDate": {"exclude": True}}
        fields = {"measuredProperty": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ObservationProperties, ObservationInheritedProperties, ObservationAllProperties
    ] = ObservationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Observation"
    return model


Observation = create_schema_org_model()


def create_observation_model(
    model: Union[
        ObservationProperties, ObservationInheritedProperties, ObservationAllProperties
    ]
):
    _type = deepcopy(ObservationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ObservationAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ObservationAllProperties):
    pydantic_type = create_observation_model(model=model)
    return pydantic_type(model).schema_json()
