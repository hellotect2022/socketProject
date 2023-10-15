from pydantic import BaseModel

class SignUpDto(BaseModel):
    id: str
    pw: str
    name: str

class LoginDto(BaseModel):
    id: str
    pw: str