from fastapi import FastAPI
from services.intents import handle_intent
from utils.history import load_history, save_history, clear_history
import datetime

app = FastAPI()

@app.get("/")
async def home():
    return("try some searches")

@app.get("/chat")
async def chat(query: str):
    response_text = await handle_intent(query)

    history = load_history()
    history.append({
        "query":query,
        "response": response_text,
        "time": str(datetime.datetime.now())
    })
    history = history[-10:]
    save_history(history)
    return{
        "query":query,
        "response":response_text
    }

@app.get("/history")
def get_history():
    return load_history()

@app.get("/clear_history")
def clear_history():
    clear_history()
    return{"message":"history cleared"}

@app.get("/status")
def status():
    history = load_history()
    return{
        "total_queries": len(history),
        "last_query": history[-1] if history else None
    }
    