import datetime
from pydantic import BaseModel, Field

class BookingCreate(BaseModel):
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime

class Booking(BookingCreate):
    booking_id: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str = Field(max_rength=12)

class User(UserCreate):
    user_id: int

    class Config:
        orm_mode = True

class RoomCreate(BaseModel):
    room_name: str = Field(max_length=12)
    capacity: int

class Room(RoomCreate):
    room_id: int

    class Config:
        orm_mode = True