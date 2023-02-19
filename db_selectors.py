from sqlalchemy import text, bindparam, Integer
from sqlalchemy.ext.asyncio import AsyncSession


async def select_person_recursive(
    session: AsyncSession,
):
    raw_sql = text("""
    with recursive nodes as (
        select '1' as path, first_name, id
        from person
        where boss_id is null
        
        union all
        
        select concat(path, '->', cast( o.id as text)) as path, o.first_name, o.id
        from person o
        join nodes n on n.id = o.boss_id
    )
    select *
    from nodes
    order by id desc
    ;
    """)   # .bindparams(bindparam("constraint_name", String))

    cur = await session.execute(raw_sql)
    res = cur.fetchall()
    return [r._asdict() for r in res]
