from fastapi import FastAPI, Request
import random
from content import QUOTES, JOKES, FUNFACTS, CHALLENGES, LUCKY_MESSAGES
from pydantic import BaseModel

app = FastAPI()

class WebhookRequest(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Mezon FunBox is running!"}

@app.post("/webhook")
async def webhook(request: WebhookRequest):
    command = request.text.strip().lower()
    
    if command == "/quote":
        quote = random.choice(QUOTES)
        return {"text": f'"{quote["text"]}"\n- {quote["author"]}'}
    
    elif command == "/joke":
        joke = random.choice(JOKES)
        return {"text": joke}
    
    elif command == "/funfact":
        funfact = random.choice(FUNFACTS)
        return {"text": funfact}
    
    elif command == "/challenge":
        challenge = random.choice(CHALLENGES)
        return {"text": challenge}
    
    elif command == "/lucky":
        lucky_message = random.choice(LUCKY_MESSAGES)
        return {"text": lucky_message}
    
    else:
        return {
            "text": "Lệnh không hợp lệ. Hãy thử các lệnh sau:\n/quote - Câu nói hay\n/joke - Câu đùa vui\n/funfact - Sự thật thú vị\n/challenge - Thử thách\n/lucky - Lời tiên tri may mắn"
        } 