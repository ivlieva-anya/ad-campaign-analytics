from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class SourceBase(BaseModel):
    name: str
    url: str
    source_type: int
    is_active: bool = True
    scan_start_date: Optional[datetime] = None
    scan_end_date: Optional[datetime] = None

class SourceCreate(SourceBase):
    pass

class Source(SourceBase):
    id: int
    last_scan_date: Optional[datetime] = None
    user_id: int

    class Config:
        from_attributes = True