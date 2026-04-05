import httpx

async def get_joke():
    async with httpx.AsyncClient() as client:
        res = await client.get("https://official-joke-api.appspot.com/random_joke")
        data = res.json()
        return f"{data['setup']} - {data['punchline']}"

async def get_user():
    async with httpx.AsyncClient() as client :
        res = await client.get("https://randomuser.me/api/") 
        data = res.json()
        user = data["results"][0]
        return f"{user['user']['first']} {user['name']['last']}"
    
async def get_advice():
    async with httpx.AsyncClient() as client :
        res = await client.get("https://api.adviceslip.com/advice")
        data = res.json()
        return data["slip"]["advice"]    

