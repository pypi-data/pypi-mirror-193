"""
EnergyConsumptionDetails represents information related to the energy efficiency of a product that consumes energy. The information that can be provided is based on international regulations such as for example [EU directive 2017/1369](https://eur-lex.europa.eu/eli/reg/2017/1369/oj) for energy labeling and the [Energy labeling rule](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/energy-water-use-labeling-consumer) under the Energy Policy and Conservation Act (EPCA) in the US.

https://schema.org/EnergyConsumptionDetails
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EnergyConsumptionDetailsInheritedProperties(TypedDict):
    """EnergyConsumptionDetails represents information related to the energy efficiency of a product that consumes energy. The information that can be provided is based on international regulations such as for example [EU directive 2017/1369](https://eur-lex.europa.eu/eli/reg/2017/1369/oj) for energy labeling and the [Energy labeling rule](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/energy-water-use-labeling-consumer) under the Energy Policy and Conservation Act (EPCA) in the US.

    References:
        https://schema.org/EnergyConsumptionDetails
    Note:
        Model Depth 3
    Attributes:
    """

    


class EnergyConsumptionDetailsProperties(TypedDict):
    """EnergyConsumptionDetails represents information related to the energy efficiency of a product that consumes energy. The information that can be provided is based on international regulations such as for example [EU directive 2017/1369](https://eur-lex.europa.eu/eli/reg/2017/1369/oj) for energy labeling and the [Energy labeling rule](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/energy-water-use-labeling-consumer) under the Energy Policy and Conservation Act (EPCA) in the US.

    References:
        https://schema.org/EnergyConsumptionDetails
    Note:
        Model Depth 3
    Attributes:
        hasEnergyEfficiencyCategory: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Defines the energy efficiency Category (which could be either a rating out of range of values or a yes/no certification) for a product according to an international energy efficiency standard.
        energyEfficiencyScaleMin: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifies the least energy efficient class on the regulated EU energy consumption scale for the product category a product belongs to. For example, energy consumption for televisions placed on the market after January 1, 2020 is scaled from D to A+++.
        energyEfficiencyScaleMax: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifies the most energy efficient class on the regulated EU energy consumption scale for the product category a product belongs to. For example, energy consumption for televisions placed on the market after January 1, 2020 is scaled from D to A+++.
    """

    hasEnergyEfficiencyCategory: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    energyEfficiencyScaleMin: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    energyEfficiencyScaleMax: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(EnergyConsumptionDetailsInheritedProperties , EnergyConsumptionDetailsProperties, TypedDict):
    pass


class EnergyConsumptionDetailsBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EnergyConsumptionDetails",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'hasEnergyEfficiencyCategory': {'exclude': True}}
        fields = {'energyEfficiencyScaleMin': {'exclude': True}}
        fields = {'energyEfficiencyScaleMax': {'exclude': True}}
        


def create_schema_org_model(type_: Union[EnergyConsumptionDetailsProperties, EnergyConsumptionDetailsInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EnergyConsumptionDetails"
    return model
    

EnergyConsumptionDetails = create_schema_org_model()


def create_energyconsumptiondetails_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_energyconsumptiondetails_model(model=model)
    return pydantic_type(model).schema_json()


