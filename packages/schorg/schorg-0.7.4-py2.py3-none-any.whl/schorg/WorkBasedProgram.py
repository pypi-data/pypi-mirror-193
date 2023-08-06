"""
A program with both an educational and employment component. Typically based at a workplace and structured around work-based learning, with the aim of instilling competencies related to an occupation. WorkBasedProgram is used to distinguish programs such as apprenticeships from school, college or other classroom based educational programs.

https://schema.org/WorkBasedProgram
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WorkBasedProgramInheritedProperties(TypedDict):
    """A program with both an educational and employment component. Typically based at a workplace and structured around work-based learning, with the aim of instilling competencies related to an occupation. WorkBasedProgram is used to distinguish programs such as apprenticeships from school, college or other classroom based educational programs.

    References:
        https://schema.org/WorkBasedProgram
    Note:
        Model Depth 4
    Attributes:
        applicationDeadline: (Optional[Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]]): The date at which the program stops collecting applications for the next enrollment cycle.
        timeToComplete: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The expected length of time to complete the program if attending full-time.
        timeOfDay: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The time of day the program normally runs. For example, "evenings".
        provider: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        termsPerYear: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The number of times terms of study are offered per year. Semesters and quarters are common units for term. For example, if the student can only take 2 semesters for the program in one year, then termsPerYear should be 2.
        termDuration: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The amount of time in a term as defined by the institution. A term is a length of time where students take one or more classes. Semesters and quarters are common units for term.
        occupationalCredentialAwarded: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A description of the qualification, award, certificate, diploma or other occupational credential awarded as a consequence of successful completion of this course or program.
        financialAidEligible: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A financial aid type or program which students may use to pay for tuition or fees associated with the program.
        salaryUponCompletion: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The expected salary upon completing the training.
        hasCourse: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A course or class that is one of the learning opportunities that constitute an educational / occupational program. No information is implied about whether the course is mandatory or optional; no guarantee is implied about whether the course will be available to everyone on the program.
        educationalCredentialAwarded: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A description of the qualification, award, certificate, diploma or other educational credential awarded as a consequence of successful completion of this course or program.
        typicalCreditsPerTerm: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of credits or units a full-time student would be expected to take in 1 term however 'term' is defined by the institution.
        maximumEnrollment: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The maximum number of students who may be enrolled in the program.
        programType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The type of educational or occupational program. For example, classroom, internship, alternance, etc.
        programPrerequisites: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Prerequisites for enrolling in the program.
        educationalProgramMode: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Similar to courseMode, the medium or means of delivery of the program as a whole. The value may either be a text label (e.g. "online", "onsite" or "blended"; "synchronous" or "asynchronous"; "full-time" or "part-time") or a URL reference to a term from a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous ).
        dayOfWeek: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The day of the week for which these opening hours are valid.
        occupationalCategory: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.
        startDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        numberOfCredits: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.
        offers: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
        trainingSalary: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The estimated salary earned while in the program.
        endDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        applicationStartDate: (Optional[Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]]): The date at which the program begins collecting applications for the next enrollment cycle.
    """

    applicationDeadline: NotRequired[
        Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]
    ]
    timeToComplete: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    timeOfDay: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    provider: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    termsPerYear: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    termDuration: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    occupationalCredentialAwarded: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    financialAidEligible: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    salaryUponCompletion: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    hasCourse: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    educationalCredentialAwarded: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    typicalCreditsPerTerm: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    maximumEnrollment: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    programType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    programPrerequisites: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    educationalProgramMode: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    dayOfWeek: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    occupationalCategory: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    startDate: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    numberOfCredits: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    offers: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    trainingSalary: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    endDate: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    applicationStartDate: NotRequired[
        Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]
    ]


class WorkBasedProgramProperties(TypedDict):
    """A program with both an educational and employment component. Typically based at a workplace and structured around work-based learning, with the aim of instilling competencies related to an occupation. WorkBasedProgram is used to distinguish programs such as apprenticeships from school, college or other classroom based educational programs.

    References:
        https://schema.org/WorkBasedProgram
    Note:
        Model Depth 4
    Attributes:
        occupationalCategory: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.
        trainingSalary: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The estimated salary earned while in the program.
    """

    occupationalCategory: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    trainingSalary: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class WorkBasedProgramAllProperties(
    WorkBasedProgramInheritedProperties, WorkBasedProgramProperties, TypedDict
):
    pass


class WorkBasedProgramBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WorkBasedProgram", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"applicationDeadline": {"exclude": True}}
        fields = {"timeToComplete": {"exclude": True}}
        fields = {"timeOfDay": {"exclude": True}}
        fields = {"provider": {"exclude": True}}
        fields = {"termsPerYear": {"exclude": True}}
        fields = {"termDuration": {"exclude": True}}
        fields = {"occupationalCredentialAwarded": {"exclude": True}}
        fields = {"financialAidEligible": {"exclude": True}}
        fields = {"salaryUponCompletion": {"exclude": True}}
        fields = {"hasCourse": {"exclude": True}}
        fields = {"educationalCredentialAwarded": {"exclude": True}}
        fields = {"typicalCreditsPerTerm": {"exclude": True}}
        fields = {"maximumEnrollment": {"exclude": True}}
        fields = {"programType": {"exclude": True}}
        fields = {"programPrerequisites": {"exclude": True}}
        fields = {"educationalProgramMode": {"exclude": True}}
        fields = {"dayOfWeek": {"exclude": True}}
        fields = {"occupationalCategory": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"numberOfCredits": {"exclude": True}}
        fields = {"offers": {"exclude": True}}
        fields = {"trainingSalary": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}
        fields = {"applicationStartDate": {"exclude": True}}
        fields = {"occupationalCategory": {"exclude": True}}
        fields = {"trainingSalary": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        WorkBasedProgramProperties,
        WorkBasedProgramInheritedProperties,
        WorkBasedProgramAllProperties,
    ] = WorkBasedProgramAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WorkBasedProgram"
    return model


WorkBasedProgram = create_schema_org_model()


def create_workbasedprogram_model(
    model: Union[
        WorkBasedProgramProperties,
        WorkBasedProgramInheritedProperties,
        WorkBasedProgramAllProperties,
    ]
):
    _type = deepcopy(WorkBasedProgramAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WorkBasedProgramAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WorkBasedProgramAllProperties):
    pydantic_type = create_workbasedprogram_model(model=model)
    return pydantic_type(model).schema_json()
