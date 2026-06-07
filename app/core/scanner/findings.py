from pydantic import BaseModel
from typing import Optional

class Finding(BaseModel):
    type: str
    severity: str
    file: str
    line: int
    message: str
    ai_fix: Optional[str] = None

