"""
A listing that describes a job opening in a certain organization.

https://schema.org/JobPosting
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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
        incentiveCompensation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Description of bonus and commission compensation aspects of the job.
        securityClearanceRequirement: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A description of any security clearance requirements of the job.
        hiringOrganization: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Organization or Person offering the job position.
        baseSalary: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The base salary of the job or of an employee in an EmployeeRole.
        workHours: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm).
        jobImmediateStart: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): An indicator as to whether a position is available for an immediate start.
        employerOverview: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A description of the employer, career opportunities and work environment for this position.
        skills: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A statement of knowledge, skill, ability, task or any other assertion expressing a competency that is desired or required to fulfill this role or to work in this occupation.
        physicalRequirement: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A description of the types of physical activity associated with the job. Defined terms such as those in O*net may be used, but note that there is no way to specify the level of ability as well as its nature when using a defined term.
        experienceRequirements: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Description of skills and experience needed for the position or Occupation.
        qualifications: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specific qualifications required for this role or Occupation.
        specialCommitments: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Any special commitments associated with this job posting. Valid entries include VeteranCommit, MilitarySpouseCommit, etc.
        jobStartDate: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): The date on which a successful applicant for this job would be expected to start work. Choose a specific date in the future or use the jobImmediateStart property to indicate the position is to be filled as soon as possible.
        title: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The title of the job.
        relevantOccupation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The Occupation for the JobPosting.
        jobLocation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A (typically single) geographic location associated with the job position.
        educationRequirements: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Educational background needed for the position or Occupation.
        eligibilityToWorkRequirement: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The legal requirements such as citizenship, visa and other documentation required for an applicant to this job.
        estimatedSalary: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): An estimated salary for a job posting or occupation, based on a variety of variables including, but not limited to industry, job title, and location. Estimated salaries  are often computed by outside organizations rather than the hiring organization, who may not have committed to the estimated value.
        validThrough: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        sensoryRequirement: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A description of any sensory requirements and levels necessary to function on the job, including hearing and vision. Defined terms such as those in O*net may be used, but note that there is no way to specify the level of ability as well as its nature when using a defined term.
        employmentType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).
        totalJobOpenings: (Optional[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]): The number of positions open for this job posting. Use a positive integer. Do not use if the number of positions is unclear or not known.
        salaryCurrency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217)) used for the main salary information in this job posting or for this employee.
        applicationContact: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Contact details for further information relevant to this job posting.
        experienceInPlaceOfEducation: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates whether a [[JobPosting]] will accept experience (as indicated by [[OccupationalExperienceRequirements]]) in place of its formal educational qualifications (as indicated by [[educationRequirements]]). If true, indicates that satisfying one of these requirements is sufficient.
        datePosted: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): Publication date of an online listing.
        jobBenefits: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Description of benefits associated with the job.
        applicantLocationRequirements: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The location(s) applicants can apply from. This is usually used for telecommuting jobs where the applicant does not need to be in a physical office. Note: This should not be used for citizenship or work visa requirements.
        occupationalCategory: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.
        industry: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The industry associated with the job position.
        employmentUnit: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates the department, unit and/or facility where the employee reports and/or in which the job is to be performed.
        benefits: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Description of benefits associated with the job.
        jobLocationType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A description of the job location (e.g. TELECOMMUTE for telecommute jobs).
        responsibilities: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Responsibilities associated with this role or Occupation.
        directApply: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates whether an [[url]] that is associated with a [[JobPosting]] enables direct application for the job, via the posting website. A job posting is considered to have directApply of [[True]] if an application process for the specified job can be directly initiated via the url(s) given (noting that e.g. multiple internet domains might nevertheless be involved at an implementation level). A value of [[False]] is appropriate if there is no clear path to applying directly online for the specified job, navigating directly from the JobPosting url(s) supplied.
        incentives: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Description of bonus and commission compensation aspects of the job.
    """

    incentiveCompensation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    securityClearanceRequirement: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    hiringOrganization: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    baseSalary: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    workHours: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    jobImmediateStart: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    employerOverview: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    skills: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    physicalRequirement: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    experienceRequirements: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    qualifications: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    specialCommitments: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    jobStartDate: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    title: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    relevantOccupation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    jobLocation: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    educationRequirements: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    eligibilityToWorkRequirement: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    estimatedSalary: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    validThrough: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    sensoryRequirement: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    employmentType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    totalJobOpenings: NotRequired[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]
    salaryCurrency: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    applicationContact: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    experienceInPlaceOfEducation: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    datePosted: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    jobBenefits: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    applicantLocationRequirements: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    occupationalCategory: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    industry: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    employmentUnit: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    benefits: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    jobLocationType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    responsibilities: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    directApply: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    incentives: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(JobPostingInheritedProperties , JobPostingProperties, TypedDict):
    pass


class JobPostingBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="JobPosting",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'incentiveCompensation': {'exclude': True}}
        fields = {'securityClearanceRequirement': {'exclude': True}}
        fields = {'hiringOrganization': {'exclude': True}}
        fields = {'baseSalary': {'exclude': True}}
        fields = {'workHours': {'exclude': True}}
        fields = {'jobImmediateStart': {'exclude': True}}
        fields = {'employerOverview': {'exclude': True}}
        fields = {'skills': {'exclude': True}}
        fields = {'physicalRequirement': {'exclude': True}}
        fields = {'experienceRequirements': {'exclude': True}}
        fields = {'qualifications': {'exclude': True}}
        fields = {'specialCommitments': {'exclude': True}}
        fields = {'jobStartDate': {'exclude': True}}
        fields = {'title': {'exclude': True}}
        fields = {'relevantOccupation': {'exclude': True}}
        fields = {'jobLocation': {'exclude': True}}
        fields = {'educationRequirements': {'exclude': True}}
        fields = {'eligibilityToWorkRequirement': {'exclude': True}}
        fields = {'estimatedSalary': {'exclude': True}}
        fields = {'validThrough': {'exclude': True}}
        fields = {'sensoryRequirement': {'exclude': True}}
        fields = {'employmentType': {'exclude': True}}
        fields = {'totalJobOpenings': {'exclude': True}}
        fields = {'salaryCurrency': {'exclude': True}}
        fields = {'applicationContact': {'exclude': True}}
        fields = {'experienceInPlaceOfEducation': {'exclude': True}}
        fields = {'datePosted': {'exclude': True}}
        fields = {'jobBenefits': {'exclude': True}}
        fields = {'applicantLocationRequirements': {'exclude': True}}
        fields = {'occupationalCategory': {'exclude': True}}
        fields = {'industry': {'exclude': True}}
        fields = {'employmentUnit': {'exclude': True}}
        fields = {'benefits': {'exclude': True}}
        fields = {'jobLocationType': {'exclude': True}}
        fields = {'responsibilities': {'exclude': True}}
        fields = {'directApply': {'exclude': True}}
        fields = {'incentives': {'exclude': True}}
        


def create_schema_org_model(type_: Union[JobPostingProperties, JobPostingInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "JobPosting"
    return model
    

JobPosting = create_schema_org_model()


def create_jobposting_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_jobposting_model(model=model)
    return pydantic_type(model).schema_json()


