from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Success"}

@app.post("/users")
async def users(users: User):
    return {"users": users}

@app.post("/rooms")
async def rooms(rooms: Room):
    return {"rooms": rooms}

@app.post("/bookings")
async def bookings(bookings: Booking):
    return {"bookings": bookings}