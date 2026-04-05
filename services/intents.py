from services.api_calls import get_joke,get_user,get_advice

async def handle_intent(query: str):
    query_lower = query.lower()

    if "joke" in query_lower:
        return await get_joke()
    
    elif "user" in query_lower:
        return await get_user()
    
    elif "advice" in query_lower:
        return await get_advice()
    
    else:
        return "try :joke/user/advice"
    
