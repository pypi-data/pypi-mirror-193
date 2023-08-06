"""
Data classes for API requests.
"""
from datetime import datetime
from typing import List, Optional, Dict

from pydantic import Field

from algora.api.service.datasets.v2.model import TimeseriesFilter
from algora.common.base import Base
from algora.common.enum import Order
from algora.common.type import Datetime


class TimeseriesQueryRequest(Base):
    id: Optional[str] = Field(default=None)
    dataset_id: Optional[str] = Field(default=None)
    asset_id: Optional[str] = Field(default=None)
    date: Optional[Datetime] = Field(default=None)
    start_date: Optional[datetime] = Field(default=None)
    end_date: Optional[datetime] = Field(default=None)
    as_of: Optional[datetime] = Field(default=None)
    page: Optional[int] = Field(default=None)
    limit: Optional[int] = Field(default=None)
    fields: Optional[List[str]] = Field(default=None)
    sort: Dict[str, Order] = Field(default=Order.DESC)
    where: Optional[List[TimeseriesFilter]] = Field(default=None)
