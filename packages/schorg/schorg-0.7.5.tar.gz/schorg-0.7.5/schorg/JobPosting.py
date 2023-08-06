"""
A listing that describes a job opening in a certain organization.

https://schema.org/JobPosting
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class JobPostingInheritedProperties(TypedDict):
    """A listing that describes a job opening in a certain organization.

    References:
        https://schema.org/JobPosting
    Note:
        Model Depth 3
    Attributes:
    """


class JobPostingProperties(TypedDict):
    """A listing that describes a job opening in a certain organization.

    References:
        https://schema.org/JobPosting
    Note:
        Model Depth 3
    Attributes:
        incentiveCompensation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Description of bonus and commission compensation aspects of the job.
        securityClearanceRequirement: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A description of any security clearance requirements of the job.
        hiringOrganization: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Organization or Person offering the job position.
        baseSalary: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The base salary of the job or of an employee in an EmployeeRole.
        workHours: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm).
        jobImmediateStart: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]]): An indicator as to whether a position is available for an immediate start.
        employerOverview: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A description of the employer, career opportunities and work environment for this position.
        skills: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A statement of knowledge, skill, ability, task or any other assertion expressing a competency that is desired or required to fulfill this role or to work in this occupation.
        physicalRequirement: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A description of the types of physical activity associated with the job. Defined terms such as those in O*net may be used, but note that there is no way to specify the level of ability as well as its nature when using a defined term.
        experienceRequirements: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Description of skills and experience needed for the position or Occupation.
        qualifications: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specific qualifications required for this role or Occupation.
        specialCommitments: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Any special commitments associated with this job posting. Valid entries include VeteranCommit, MilitarySpouseCommit, etc.
        jobStartDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): The date on which a successful applicant for this job would be expected to start work. Choose a specific date in the future or use the jobImmediateStart property to indicate the position is to be filled as soon as possible.
        title: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The title of the job.
        relevantOccupation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Occupation for the JobPosting.
        jobLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A (typically single) geographic location associated with the job position.
        educationRequirements: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Educational background needed for the position or Occupation.
        eligibilityToWorkRequirement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The legal requirements such as citizenship, visa and other documentation required for an applicant to this job.
        estimatedSalary: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): An estimated salary for a job posting or occupation, based on a variety of variables including, but not limited to industry, job title, and location. Estimated salaries  are often computed by outside organizations rather than the hiring organization, who may not have committed to the estimated value.
        validThrough: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        sensoryRequirement: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A description of any sensory requirements and levels necessary to function on the job, including hearing and vision. Defined terms such as those in O*net may be used, but note that there is no way to specify the level of ability as well as its nature when using a defined term.
        employmentType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).
        totalJobOpenings: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of positions open for this job posting. Use a positive integer. Do not use if the number of positions is unclear or not known.
        salaryCurrency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217)) used for the main salary information in this job posting or for this employee.
        applicationContact: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Contact details for further information relevant to this job posting.
        experienceInPlaceOfEducation: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]]): Indicates whether a [[JobPosting]] will accept experience (as indicated by [[OccupationalExperienceRequirements]]) in place of its formal educational qualifications (as indicated by [[educationRequirements]]). If true, indicates that satisfying one of these requirements is sufficient.
        datePosted: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): Publication date of an online listing.
        jobBenefits: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Description of benefits associated with the job.
        applicantLocationRequirements: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The location(s) applicants can apply from. This is usually used for telecommuting jobs where the applicant does not need to be in a physical office. Note: This should not be used for citizenship or work visa requirements.
        occupationalCategory: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.
        industry: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The industry associated with the job position.
        employmentUnit: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the department, unit and/or facility where the employee reports and/or in which the job is to be performed.
        benefits: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Description of benefits associated with the job.
        jobLocationType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A description of the job location (e.g. TELECOMMUTE for telecommute jobs).
        responsibilities: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Responsibilities associated with this role or Occupation.
        directApply: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]]): Indicates whether an [[url]] that is associated with a [[JobPosting]] enables direct application for the job, via the posting website. A job posting is considered to have directApply of [[True]] if an application process for the specified job can be directly initiated via the url(s) given (noting that e.g. multiple internet domains might nevertheless be involved at an implementation level). A value of [[False]] is appropriate if there is no clear path to applying directly online for the specified job, navigating directly from the JobPosting url(s) supplied.
        incentives: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Description of bonus and commission compensation aspects of the job.
    """

    incentiveCompensation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    securityClearanceRequirement: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    hiringOrganization: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    baseSalary: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    workHours: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    jobImmediateStart: NotRequired[
        Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]
    ]
    employerOverview: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    skills: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    physicalRequirement: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    experienceRequirements: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    qualifications: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    specialCommitments: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    jobStartDate: NotRequired[
        Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]
    ]
    title: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    relevantOccupation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    jobLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    educationRequirements: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    eligibilityToWorkRequirement: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    estimatedSalary: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    validThrough: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    sensoryRequirement: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    employmentType: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    totalJobOpenings: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    salaryCurrency: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    applicationContact: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    experienceInPlaceOfEducation: NotRequired[
        Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]
    ]
    datePosted: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    jobBenefits: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    applicantLocationRequirements: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    occupationalCategory: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    industry: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    employmentUnit: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    benefits: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    jobLocationType: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    responsibilities: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    directApply: NotRequired[
        Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]
    ]
    incentives: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class JobPostingAllProperties(
    JobPostingInheritedProperties, JobPostingProperties, TypedDict
):
    pass


class JobPostingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="JobPosting", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"incentiveCompensation": {"exclude": True}}
        fields = {"securityClearanceRequirement": {"exclude": True}}
        fields = {"hiringOrganization": {"exclude": True}}
        fields = {"baseSalary": {"exclude": True}}
        fields = {"workHours": {"exclude": True}}
        fields = {"jobImmediateStart": {"exclude": True}}
        fields = {"employerOverview": {"exclude": True}}
        fields = {"skills": {"exclude": True}}
        fields = {"physicalRequirement": {"exclude": True}}
        fields = {"experienceRequirements": {"exclude": True}}
        fields = {"qualifications": {"exclude": True}}
        fields = {"specialCommitments": {"exclude": True}}
        fields = {"jobStartDate": {"exclude": True}}
        fields = {"title": {"exclude": True}}
        fields = {"relevantOccupation": {"exclude": True}}
        fields = {"jobLocation": {"exclude": True}}
        fields = {"educationRequirements": {"exclude": True}}
        fields = {"eligibilityToWorkRequirement": {"exclude": True}}
        fields = {"estimatedSalary": {"exclude": True}}
        fields = {"validThrough": {"exclude": True}}
        fields = {"sensoryRequirement": {"exclude": True}}
        fields = {"employmentType": {"exclude": True}}
        fields = {"totalJobOpenings": {"exclude": True}}
        fields = {"salaryCurrency": {"exclude": True}}
        fields = {"applicationContact": {"exclude": True}}
        fields = {"experienceInPlaceOfEducation": {"exclude": True}}
        fields = {"datePosted": {"exclude": True}}
        fields = {"jobBenefits": {"exclude": True}}
        fields = {"applicantLocationRequirements": {"exclude": True}}
        fields = {"occupationalCategory": {"exclude": True}}
        fields = {"industry": {"exclude": True}}
        fields = {"employmentUnit": {"exclude": True}}
        fields = {"benefits": {"exclude": True}}
        fields = {"jobLocationType": {"exclude": True}}
        fields = {"responsibilities": {"exclude": True}}
        fields = {"directApply": {"exclude": True}}
        fields = {"incentives": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        JobPostingProperties, JobPostingInheritedProperties, JobPostingAllProperties
    ] = JobPostingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "JobPosting"
    return model


JobPosting = create_schema_org_model()


def create_jobposting_model(
    model: Union[
        JobPostingProperties, JobPostingInheritedProperties, JobPostingAllProperties
    ]
):
    _type = deepcopy(JobPostingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of JobPosting. Please see: https://schema.org/JobPosting"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: JobPostingAllProperties):
    pydantic_type = create_jobposting_model(model=model)
    return pydantic_type(model).schema_json()
