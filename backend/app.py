from fastapi import FastAPI
from backend.chatbot.chatbot import router as chatbot_router  # Import chatbot API

app = FastAPI()

# ✅ Include chatbot routes
app.include_router(chatbot_router)

@app.get("/")
def home():
    return {"message": "Healthcare Chatbot API is running!"}
