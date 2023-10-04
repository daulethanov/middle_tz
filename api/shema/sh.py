from fastapi import HTTPException
from pydantic import BaseModel, validator


class SendMessageRequest(BaseModel):
    to: str
    subject: str
    message: str

    @validator("to")
    def email_format(cls, v):
        if "@" not in v:
            raise HTTPException(status_code=400, detail="error validate email")
        return v