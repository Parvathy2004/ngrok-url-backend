from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow any frontend to access this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

latest_ngrok_url = ""  # Store current ngrok URL

@app.post("/update-ngrok-url")
def update_url(data: dict):
    global latest_ngrok_url
    latest_ngrok_url = data["url"]
    return {"message": "URL Updated Successfully"}

@app.get("/get-ngrok-url")
def get_url():
    return {"url": latest_ngrok_url}
