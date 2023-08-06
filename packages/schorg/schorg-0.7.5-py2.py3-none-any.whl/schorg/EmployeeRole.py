"""
A subclass of OrganizationRole used to describe employee relationships.

https://schema.org/EmployeeRole
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EmployeeRoleInheritedProperties(TypedDict):
    """A subclass of OrganizationRole used to describe employee relationships.

    References:
        https://schema.org/EmployeeRole
    Note:
        Model Depth 5
    Attributes:
        numberedPosition: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): A number associated with a role in an organization, for example, the number on an athlete's jersey.
    """

    numberedPosition: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class EmployeeRoleProperties(TypedDict):
    """A subclass of OrganizationRole used to describe employee relationships.

    References:
        https://schema.org/EmployeeRole
    Note:
        Model Depth 5
    Attributes:
        baseSalary: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The base salary of the job or of an employee in an EmployeeRole.
        salaryCurrency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217)) used for the main salary information in this job posting or for this employee.
    """

    baseSalary: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    salaryCurrency: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class EmployeeRoleAllProperties(
    EmployeeRoleInheritedProperties, EmployeeRoleProperties, TypedDict
):
    pass


class EmployeeRoleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EmployeeRole", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"numberedPosition": {"exclude": True}}
        fields = {"baseSalary": {"exclude": True}}
        fields = {"salaryCurrency": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        EmployeeRoleProperties,
        EmployeeRoleInheritedProperties,
        EmployeeRoleAllProperties,
    ] = EmployeeRoleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EmployeeRole"
    return model


EmployeeRole = create_schema_org_model()


def create_employeerole_model(
    model: Union[
        EmployeeRoleProperties,
        EmployeeRoleInheritedProperties,
        EmployeeRoleAllProperties,
    ]
):
    _type = deepcopy(EmployeeRoleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of EmployeeRole. Please see: https://schema.org/EmployeeRole"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: EmployeeRoleAllProperties):
    pydantic_type = create_employeerole_model(model=model)
    return pydantic_type(model).schema_json()
