import datetime
from pydantic import BaseModel, Field

class Booking(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime

    class Config:
        orm_mode = True

class User(BaseModel):
    user_id: int
    username: str = Field(max_rength=12)

    class Config:
        orm_mode = True

class Room(BaseModel):
    room_id: int
    room_name: str = Field(max_length=12)
    capacity: int

    class Config:
        orm_mode = True
