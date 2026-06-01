from pydantic import BaseModel

class Finding(BaseModel):
    type: str
    severity: str
    file: str
    line: int
    message: str