import httpx

async def get_joke():
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get("https://official-joke-api.appspot.com/random_joke")
            data = res.json()
            return f"{data['setup']} - {data['punchline']}"
    except:
        return "Error fetching joke."


async def get_user():
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get("https://randomuser.me/api/")
            data = res.json()

            user = data["results"][0]
            return f"{user['name']['first']} {user['name']['last']}"

    except Exception as e:
        return "Error fetching user. Try again."
    
async def get_advice():
    try:
        async with httpx.AsyncClient() as client:
            res = await client.get("https://api.adviceslip.com/advice")
            data = res.json()
            return data["slip"]["advice"]
    except:
        return "Error fetching advice."  

