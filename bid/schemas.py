from datetime import datetime

from pydantic import BaseModel


class BidSchema(BaseModel):
    id: int
    user_id: int
    auction_id: int
    bet: int
    created_at: datetime = None


class BidWSSchema(BidSchema):
    class Config:
        json_encoders = {
            datetime: lambda dt: dt.isoformat()
        }
