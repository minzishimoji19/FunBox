import random
import requests
from typing import Dict, Any

# Sample data lists
FUNFACTS = [
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "A day on Venus is longer than its year. Venus takes 243 Earth days to rotate on its axis but only 225 Earth days to orbit the Sun.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after just 38 minutes.",
    "The first oranges weren't orange. The original oranges from Southeast Asia were actually green.",
    "A group of flamingos is called a 'flamboyance'."
]

CHALLENGES = [
    "Thử thách: Hãy học một từ mới mỗi ngày trong một tuần!",
    "Thử thách: Tập thể dục 30 phút mỗi ngày trong 7 ngày liên tiếp.",
    "Thử thách: Viết nhật ký về 3 điều bạn biết ơn mỗi ngày.",
    "Thử thách: Thử một món ăn mới mà bạn chưa từng ăn.",
    "Thử thách: Dành 1 giờ mỗi ngày để đọc sách."
]

LUCKY_MESSAGES = [
    "Hôm nay là ngày may mắn của bạn! Hãy nắm bắt cơ hội.",
    "Một điều bất ngờ tốt đẹp đang chờ đợi bạn phía trước.",
    "Vận may đang mỉm cười với bạn. Hãy tin vào bản thân!",
    "Hôm nay bạn sẽ gặp được người có thể thay đổi cuộc đời bạn.",
    "Một cơ hội vàng đang đến với bạn. Hãy sẵn sàng!"
]

async def get_random_quote() -> Dict[str, str]:
    """Get a random quote from type.fit API"""
    try:
        response = requests.get("https://type.fit/api/quotes")
        response.raise_for_status()
        quotes = response.json()
        quote = random.choice(quotes)
        return {
            "text": quote["text"],
            "author": quote["author"] if quote["author"] else "Vô danh"
        }
    except Exception as e:
        return {"text": "Không thể lấy quote lúc này.", "author": "System"}

async def get_random_joke() -> str:
    """Get a random joke from icanhazdadjoke API"""
    try:
        response = requests.get(
            "https://icanhazdadjoke.com/",
            headers={'Accept': 'application/json'}
        )
        response.raise_for_status()
        return response.json()["joke"]
    except Exception as e:
        return "Xin lỗi, không thể lấy joke lúc này."

def get_random_funfact() -> str:
    """Get a random fun fact from the predefined list"""
    return random.choice(FUNFACTS)

def get_random_challenge() -> str:
    """Get a random challenge from the predefined list"""
    return random.choice(CHALLENGES)

def get_random_lucky_message() -> str:
    """Get a random lucky message from the predefined list"""
    return random.choice(LUCKY_MESSAGES) 