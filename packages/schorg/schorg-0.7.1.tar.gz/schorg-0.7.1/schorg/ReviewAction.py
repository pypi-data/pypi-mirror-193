"""
The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review.

https://schema.org/ReviewAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReviewActionInheritedProperties(TypedDict):
    """The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review.

    References:
        https://schema.org/ReviewAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class ReviewActionProperties(TypedDict):
    """The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review.

    References:
        https://schema.org/ReviewAction
    Note:
        Model Depth 4
    Attributes:
        resultReview: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of result. The review that resulted in the performing of the action.
    """

    resultReview: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(ReviewActionInheritedProperties , ReviewActionProperties, TypedDict):
    pass


class ReviewActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReviewAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'resultReview': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ReviewActionProperties, ReviewActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReviewAction"
    return model
    

ReviewAction = create_schema_org_model()


def create_reviewaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_reviewaction_model(model=model)
    return pydantic_type(model).schema_json()


