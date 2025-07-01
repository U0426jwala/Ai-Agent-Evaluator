import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()

async def search_web(query: str) -> str:
    api_key = os.getenv("SERPAPI_KEY")
    if not api_key:
        raise ValueError("SERPAPI_KEY not set")
    
    url = "https://serpapi.com/search"
    params = {"q": query, "api_key": api_key}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("organic_results", [{}])[0].get("snippet", "No results found")
            else:
                raise Exception("Search API request failed")