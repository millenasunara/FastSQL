from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from database import Session 

async def gat_session() -> Generator: # função vai ter retorno um Generator
    session: AsyncSession = Session()
    try:
        yield session # é um return "sem ser return" -> ele devolve a sessão mas mantém a função viva!
    finally:
        await session.close() # após utilizar a sessão com o banco, ai sim, finalizamos ela