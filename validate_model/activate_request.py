from pydantic import BaseModel

class ActivateRequest(BaseModel):
    activate_token: str