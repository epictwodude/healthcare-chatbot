import os
import requests
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv

router = APIRouter()
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HF_MODEL = "tiiuae/falcon-7b-instruct"

@router.post("/chatbot")
async def chatbot_query(data: dict):
    user_message = data.get("message", "").strip()
    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    try:
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{HF_MODEL}",
            headers={"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"},
            json={"inputs": f"Human: {user_message}\nAI:"}
        )
        result = response.json()
        print("output: ", result)
        if isinstance(result, list) and "generated_text" in result[0]:
            ai_response = result[0]["generated_text"].split("AI:")[-1].strip()
        else:
            ai_response = "I'm sorry, I couldn't process that request."

        return {"response": ai_response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
