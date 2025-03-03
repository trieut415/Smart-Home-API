from fastapi import FastAPI
from api.device_api import router as device_router
from api.house_api import router as house_router
from api.room_api import router as room_router
from api.user_api import router as user_router

app = FastAPI(title="Smart Home API", description="API for managing smart home devices")

# Register routers
app.include_router(device_router, prefix="/devices", tags=["Devices"])
app.include_router(house_router, prefix="/houses", tags=["Houses"])
app.include_router(room_router, prefix="/houses", tags=["Rooms"])
app.include_router(user_router, prefix="/users", tags=["Users"])

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Home API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)

