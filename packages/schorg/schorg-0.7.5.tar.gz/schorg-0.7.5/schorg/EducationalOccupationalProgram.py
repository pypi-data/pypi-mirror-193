"""
A program offered by an institution which determines the learning progress to achieve an outcome, usually a credential like a degree or certificate. This would define a discrete set of opportunities (e.g., job, courses) that together constitute a program with a clear start, end, set of requirements, and transition to a new occupational opportunity (e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).

https://schema.org/EducationalOccupationalProgram
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EducationalOccupationalProgramInheritedProperties(TypedDict):
    """A program offered by an institution which determines the learning progress to achieve an outcome, usually a credential like a degree or certificate. This would define a discrete set of opportunities (e.g., job, courses) that together constitute a program with a clear start, end, set of requirements, and transition to a new occupational opportunity (e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).

    References:
        https://schema.org/EducationalOccupationalProgram
    Note:
        Model Depth 3
    Attributes:
    """


class EducationalOccupationalProgramProperties(TypedDict):
    """A program offered by an institution which determines the learning progress to achieve an outcome, usually a credential like a degree or certificate. This would define a discrete set of opportunities (e.g., job, courses) that together constitute a program with a clear start, end, set of requirements, and transition to a new occupational opportunity (e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).

    References:
        https://schema.org/EducationalOccupationalProgram
    Note:
        Model Depth 3
    Attributes:
        applicationDeadline: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): The date at which the program stops collecting applications for the next enrollment cycle.
        timeToComplete: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The expected length of time to complete the program if attending full-time.
        timeOfDay: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The time of day the program normally runs. For example, "evenings".
        provider: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        termsPerYear: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The number of times terms of study are offered per year. Semesters and quarters are common units for term. For example, if the student can only take 2 semesters for the program in one year, then termsPerYear should be 2.
        termDuration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The amount of time in a term as defined by the institution. A term is a length of time where students take one or more classes. Semesters and quarters are common units for term.
        occupationalCredentialAwarded: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A description of the qualification, award, certificate, diploma or other occupational credential awarded as a consequence of successful completion of this course or program.
        financialAidEligible: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A financial aid type or program which students may use to pay for tuition or fees associated with the program.
        salaryUponCompletion: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The expected salary upon completing the training.
        hasCourse: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A course or class that is one of the learning opportunities that constitute an educational / occupational program. No information is implied about whether the course is mandatory or optional; no guarantee is implied about whether the course will be available to everyone on the program.
        educationalCredentialAwarded: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A description of the qualification, award, certificate, diploma or other educational credential awarded as a consequence of successful completion of this course or program.
        typicalCreditsPerTerm: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of credits or units a full-time student would be expected to take in 1 term however 'term' is defined by the institution.
        maximumEnrollment: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The maximum number of students who may be enrolled in the program.
        programType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type of educational or occupational program. For example, classroom, internship, alternance, etc.
        programPrerequisites: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Prerequisites for enrolling in the program.
        educationalProgramMode: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Similar to courseMode, the medium or means of delivery of the program as a whole. The value may either be a text label (e.g. "online", "onsite" or "blended"; "synchronous" or "asynchronous"; "full-time" or "part-time") or a URL reference to a term from a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous ).
        dayOfWeek: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The day of the week for which these opening hours are valid.
        occupationalCategory: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.
        startDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        numberOfCredits: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.
        offers: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
        trainingSalary: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The estimated salary earned while in the program.
        endDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        applicationStartDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): The date at which the program begins collecting applications for the next enrollment cycle.
    """

    applicationDeadline: NotRequired[
        Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]
    ]
    timeToComplete: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    timeOfDay: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    provider: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    termsPerYear: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    termDuration: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    occupationalCredentialAwarded: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    financialAidEligible: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    salaryUponCompletion: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    hasCourse: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    educationalCredentialAwarded: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    typicalCreditsPerTerm: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    maximumEnrollment: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    programType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    programPrerequisites: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    educationalProgramMode: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    dayOfWeek: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    occupationalCategory: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    startDate: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    numberOfCredits: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    offers: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    trainingSalary: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    endDate: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    applicationStartDate: NotRequired[
        Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]
    ]


class EducationalOccupationalProgramAllProperties(
    EducationalOccupationalProgramInheritedProperties,
    EducationalOccupationalProgramProperties,
    TypedDict,
):
    pass


class EducationalOccupationalProgramBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EducationalOccupationalProgram", alias="@id")
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


def create_schema_org_model(
    type_: Union[
        EducationalOccupationalProgramProperties,
        EducationalOccupationalProgramInheritedProperties,
        EducationalOccupationalProgramAllProperties,
    ] = EducationalOccupationalProgramAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EducationalOccupationalProgram"
    return model


EducationalOccupationalProgram = create_schema_org_model()


def create_educationaloccupationalprogram_model(
    model: Union[
        EducationalOccupationalProgramProperties,
        EducationalOccupationalProgramInheritedProperties,
        EducationalOccupationalProgramAllProperties,
    ]
):
    _type = deepcopy(EducationalOccupationalProgramAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of EducationalOccupationalProgram. Please see: https://schema.org/EducationalOccupationalProgram"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: EducationalOccupationalProgramAllProperties):
    pydantic_type = create_educationaloccupationalprogram_model(model=model)
    return pydantic_type(model).schema_json()
