"""
A StatisticalPopulation is a set of instances of a certain given type that satisfy some set of constraints. The property [[populationType]] is used to specify the type. Any property that can be used on instances of that type can appear on the statistical population. For example, a [[StatisticalPopulation]] representing all [[Person]]s with a [[homeLocation]] of East Podunk California would be described by applying the appropriate [[homeLocation]] and [[populationType]] properties to a [[StatisticalPopulation]] item that stands for that set of people.The properties [[numConstraints]] and [[constrainingProperty]] are used to specify which of the populations properties are used to specify the population. Note that the sense of "population" used here is the general sense of a statisticalpopulation, and does not imply that the population consists of people. For example, a [[populationType]] of [[Event]] or [[NewsArticle]] could be used. See also [[Observation]], and the [data and datasets](/docs/data-and-datasets.html) overview for more details.  

https://schema.org/StatisticalPopulation
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class StatisticalPopulationInheritedProperties(TypedDict):
    """A StatisticalPopulation is a set of instances of a certain given type that satisfy some set of constraints. The property [[populationType]] is used to specify the type. Any property that can be used on instances of that type can appear on the statistical population. For example, a [[StatisticalPopulation]] representing all [[Person]]s with a [[homeLocation]] of East Podunk California would be described by applying the appropriate [[homeLocation]] and [[populationType]] properties to a [[StatisticalPopulation]] item that stands for that set of people.The properties [[numConstraints]] and [[constrainingProperty]] are used to specify which of the populations properties are used to specify the population. Note that the sense of "population" used here is the general sense of a statisticalpopulation, and does not imply that the population consists of people. For example, a [[populationType]] of [[Event]] or [[NewsArticle]] could be used. See also [[Observation]], and the [data and datasets](/docs/data-and-datasets.html) overview for more details.  

    References:
        https://schema.org/StatisticalPopulation
    Note:
        Model Depth 3
    Attributes:
    """

    


class StatisticalPopulationProperties(TypedDict):
    """A StatisticalPopulation is a set of instances of a certain given type that satisfy some set of constraints. The property [[populationType]] is used to specify the type. Any property that can be used on instances of that type can appear on the statistical population. For example, a [[StatisticalPopulation]] representing all [[Person]]s with a [[homeLocation]] of East Podunk California would be described by applying the appropriate [[homeLocation]] and [[populationType]] properties to a [[StatisticalPopulation]] item that stands for that set of people.The properties [[numConstraints]] and [[constrainingProperty]] are used to specify which of the populations properties are used to specify the population. Note that the sense of "population" used here is the general sense of a statisticalpopulation, and does not imply that the population consists of people. For example, a [[populationType]] of [[Event]] or [[NewsArticle]] could be used. See also [[Observation]], and the [data and datasets](/docs/data-and-datasets.html) overview for more details.  

    References:
        https://schema.org/StatisticalPopulation
    Note:
        Model Depth 3
    Attributes:
        constrainingProperty: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): Indicates a property used as a constraint to define a [[StatisticalPopulation]] with respect to the set of entities  corresponding to an indicated type (via [[populationType]]).
        populationType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the populationType common to all members of a [[StatisticalPopulation]].
        numConstraints: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): Indicates the number of constraints (not counting [[populationType]]) defined for a particular [[StatisticalPopulation]]. This helps applications understand if they have access to a sufficiently complete description of a [[StatisticalPopulation]].
    """

    constrainingProperty: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    populationType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numConstraints: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    


class AllProperties(StatisticalPopulationInheritedProperties , StatisticalPopulationProperties, TypedDict):
    pass


class StatisticalPopulationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="StatisticalPopulation",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'constrainingProperty': {'exclude': True}}
        fields = {'populationType': {'exclude': True}}
        fields = {'numConstraints': {'exclude': True}}
        


def create_schema_org_model(type_: Union[StatisticalPopulationProperties, StatisticalPopulationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "StatisticalPopulation"
    return model
    

StatisticalPopulation = create_schema_org_model()


def create_statisticalpopulation_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_statisticalpopulation_model(model=model)
    return pydantic_type(model).schema_json()


