from typing import Any
import aiohttp
from bot.config import CAT_API_KEY


CAT_API_URL = "https://api.thecatapi.com/v1/images/search"


async def fetch_cats(
    limit: int = 1,
    breed: str | None = None,
    has_breeds: int = 0,
    ) -> list[dict[str, Any]]:
    """Получает фотографии кошек из TheCatAPI"""

    headers = {}

    if CAT_API_KEY:
        headers["x-api-key"] = CAT_API_KEY

    params = {
        "limit": limit,
        "has_breeds": has_breeds,
    }

    if breed:
        params["breed_ids"] = breed

    timeout = aiohttp.ClientTimeout(total=15)

    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get(
            CAT_API_URL,
            headers=headers,
            params=params,
        ) as response:
            response.raise_for_status()
            return await response.json()
