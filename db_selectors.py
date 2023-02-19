from sqlalchemy import text, bindparam, Integer
from sqlalchemy.ext.asyncio import AsyncSession


async def select_person_recursive(
    session: AsyncSession,
):
    raw_sql = text("""
        
    """)   # .bindparams(bindparam("constraint_name", String))

    return session.execute(raw_sql)
