import typing as t

from pydantic import BaseModel


# token schema
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: t.Optional[str] = None
