"""
The act of participating in exertive activity for the purposes of improving health and fitness.

https://schema.org/ExerciseAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ExerciseActionInheritedProperties(TypedDict):
    """The act of participating in exertive activity for the purposes of improving health and fitness.

    References:
        https://schema.org/ExerciseAction
    Note:
        Model Depth 4
    Attributes:
        event: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Upcoming or past event associated with this place, organization, or action.
        audience: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An intended audience, i.e. a group for whom something was created.
    """

    event: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    audience: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ExerciseActionProperties(TypedDict):
    """The act of participating in exertive activity for the purposes of improving health and fitness.

    References:
        https://schema.org/ExerciseAction
    Note:
        Model Depth 4
    Attributes:
        toLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The final location of the object or the agent after the action.
        course: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The course where this action was taken.
        fromLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The original location of the object or the agent before the action.
        exerciseRelatedDiet: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of instrument. The diet used in this action.
        exerciseCourse: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The course where this action was taken.
        opponent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The opponent on this action.
        sportsTeam: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of participant. The sports team that participated on this action.
        sportsEvent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The sports event where this action occurred.
        diet: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of instrument. The diet used in this action.
        exercisePlan: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of instrument. The exercise plan used on this action.
        exerciseType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc.
        distance: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The distance travelled, e.g. exercising or travelling.
        sportsActivityLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of location. The sports activity location where this action occurred.
    """

    toLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    course: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fromLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    exerciseRelatedDiet: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    exerciseCourse: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    opponent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sportsTeam: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sportsEvent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    diet: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    exercisePlan: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    exerciseType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    distance: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sportsActivityLocation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class ExerciseActionAllProperties(
    ExerciseActionInheritedProperties, ExerciseActionProperties, TypedDict
):
    pass


class ExerciseActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ExerciseAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"event": {"exclude": True}}
        fields = {"audience": {"exclude": True}}
        fields = {"toLocation": {"exclude": True}}
        fields = {"course": {"exclude": True}}
        fields = {"fromLocation": {"exclude": True}}
        fields = {"exerciseRelatedDiet": {"exclude": True}}
        fields = {"exerciseCourse": {"exclude": True}}
        fields = {"opponent": {"exclude": True}}
        fields = {"sportsTeam": {"exclude": True}}
        fields = {"sportsEvent": {"exclude": True}}
        fields = {"diet": {"exclude": True}}
        fields = {"exercisePlan": {"exclude": True}}
        fields = {"exerciseType": {"exclude": True}}
        fields = {"distance": {"exclude": True}}
        fields = {"sportsActivityLocation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ExerciseActionProperties,
        ExerciseActionInheritedProperties,
        ExerciseActionAllProperties,
    ] = ExerciseActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ExerciseAction"
    return model


ExerciseAction = create_schema_org_model()


def create_exerciseaction_model(
    model: Union[
        ExerciseActionProperties,
        ExerciseActionInheritedProperties,
        ExerciseActionAllProperties,
    ]
):
    _type = deepcopy(ExerciseActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ExerciseActionAllProperties):
    pydantic_type = create_exerciseaction_model(model=model)
    return pydantic_type(model).schema_json()
