from fastapi import FastAPI, Request
from pydantic import BaseModel
from utils import (
    get_random_quote,
    get_random_joke,
    get_random_funfact,
    get_random_challenge,
    get_random_lucky_message
)

app = FastAPI(title="Mezon FunBox Bot")

class WebhookRequest(BaseModel):
    message: str

@app.get("/")
async def root():
    return {"message": "Mezon FunBox is running!"}

@app.post("/webhook")
async def webhook(request: WebhookRequest):
    message = request.message.strip().lower()
    
    if message == "/quote":
        quote = await get_random_quote()
        return {"reply": f'"{quote["text"]}"\n- {quote["author"]}'}
    
    elif message == "/joke":
        joke = await get_random_joke()
        return {"reply": joke}
    
    elif message == "/funfact":
        funfact = get_random_funfact()
        return {"reply": funfact}
    
    elif message == "/challenge":
        challenge = get_random_challenge()
        return {"reply": challenge}
    
    elif message == "/lucky":
        lucky_message = get_random_lucky_message()
        return {"reply": lucky_message}
    
    else:
        return {"reply": "Xin lỗi, tôi chưa hiểu lệnh của bạn!"} 