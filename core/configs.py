from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    """Configurações gerais utilizadas na aplicação"""
    API_V1_STR: str = '/api/v1' # não precisar inserir via hard coding
    DB_URL: str = 'mysql+asyncmy://root@127.0.0.1:3306/etscursos'# ideal user:pasword
    DBBaseModel = declarative_base() # serve para que os models herdem todos os recursos do sqlAlchemy!
    
settings = Settings()
    
    