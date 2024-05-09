from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings

engine: AsyncEngine = create_async_engine(settings.DB_URL)

#sessionmaker retorna uma classe
#Abre e fecha conexão com o banco de dados
Session: AsyncSession = sessionmaker(
    autocommit=False,
    autosflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
) 

# print(type(Session))
