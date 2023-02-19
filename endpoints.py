import aiohttp.web

from db import async_session
from db_selectors import select_person_recursive


async def get_employee_structure(request):
    async with async_session() as session:
        res = await select_person_recursive(session)

    return aiohttp.web.json_response(res)
