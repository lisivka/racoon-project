from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class ProfileSchema(BaseModel):
    name: Optional[str]  # noqa: UP007
    surname: Optional[str]  # noqa: UP007
    avatar: str


class UserSchema(BaseModel):
    email: str
    profile: ProfileSchema


class BidSchema(BaseModel):
    id: int
    user_id: int
    user: UserSchema
    auction_id: int
    bet: int
    created_at: datetime = None


class BidWSSchema(BidSchema):
    class Config:
        json_encoders = {
            datetime: lambda dt: dt.isoformat()
        }
