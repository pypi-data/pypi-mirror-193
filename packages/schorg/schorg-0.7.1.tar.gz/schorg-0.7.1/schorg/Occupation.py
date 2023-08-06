"""
A profession, may involve prolonged training and/or a formal qualification.

https://schema.org/Occupation
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OccupationInheritedProperties(TypedDict):
    """A profession, may involve prolonged training and/or a formal qualification.

    References:
        https://schema.org/Occupation
    Note:
        Model Depth 3
    Attributes:
    """

    


class OccupationProperties(TypedDict):
    """A profession, may involve prolonged training and/or a formal qualification.

    References:
        https://schema.org/Occupation
    Note:
        Model Depth 3
    Attributes:
        occupationLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]):  The region/country for which this occupational description is appropriate. Note that educational requirements and qualifications can vary between jurisdictions.
        skills: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A statement of knowledge, skill, ability, task or any other assertion expressing a competency that is desired or required to fulfill this role or to work in this occupation.
        experienceRequirements: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Description of skills and experience needed for the position or Occupation.
        qualifications: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specific qualifications required for this role or Occupation.
        educationRequirements: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Educational background needed for the position or Occupation.
        estimatedSalary: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): An estimated salary for a job posting or occupation, based on a variety of variables including, but not limited to industry, job title, and location. Estimated salaries  are often computed by outside organizations rather than the hiring organization, who may not have committed to the estimated value.
        occupationalCategory: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html), [ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or similar, with the property repeated for each applicable value. Ideally the taxonomy should be identified, and both the textual label and formal code for the category should be provided.Note: for historical reasons, any textual label and formal code provided as a literal may be assumed to be from O*NET-SOC.
        responsibilities: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Responsibilities associated with this role or Occupation.
    """

    occupationLocation: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    skills: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    experienceRequirements: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    qualifications: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    educationRequirements: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    estimatedSalary: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    occupationalCategory: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    responsibilities: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(OccupationInheritedProperties , OccupationProperties, TypedDict):
    pass


class OccupationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Occupation",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'occupationLocation': {'exclude': True}}
        fields = {'skills': {'exclude': True}}
        fields = {'experienceRequirements': {'exclude': True}}
        fields = {'qualifications': {'exclude': True}}
        fields = {'educationRequirements': {'exclude': True}}
        fields = {'estimatedSalary': {'exclude': True}}
        fields = {'occupationalCategory': {'exclude': True}}
        fields = {'responsibilities': {'exclude': True}}
        


def create_schema_org_model(type_: Union[OccupationProperties, OccupationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Occupation"
    return model
    

Occupation = create_schema_org_model()


def create_occupation_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_occupation_model(model=model)
    return pydantic_type(model).schema_json()


