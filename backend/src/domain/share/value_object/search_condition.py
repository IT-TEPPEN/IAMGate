from pydantic import BaseModel, Field
from enum import Enum


class ESearchConditionOrder(str, Enum):
    昇順 = "asc"
    降順 = "desc"


class VSearchCondition(BaseModel):
    limit: int = Field(
        default=100,
        ge=1,
        description="The maximum number of results to return.",
    )
    offset: int = Field(
        default=0,
        ge=0,
        description="The number of results to skip before returning the results.",
    )
    sort_by: str = Field(
        default="id",
        description="The field to sort the results by.",
    )
    order: ESearchConditionOrder = Field(
        default=ESearchConditionOrder.昇順,
        description="The order to sort the results in. Can be 'asc' or 'desc'.",
    )
