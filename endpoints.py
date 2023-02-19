from aiohttp import web

from db import async_session
from db_selectors import select_person_recursive


async def get_structure(request):
    ...
    # async with Session() as session
    #     return web.Response(text="Hello, world")
    async with async_session() as session:
        return select_person_recursive(session)