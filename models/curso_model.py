import sys
default_path = "C:\\Users\\ct67ca\\Desktop\\FastSQL"
sys.path.append(default_path)

from core.configs import settings
from sqlalchemy import Column, Integer, String

class CursoModel(settings.DBBaseModel):
    __tablename__ = "cursos"
    id: int= Column(Integer, primary_key=True, autoincrement=True)
    título: str = Column(String(100))
    horas: int = Column(Integer)
    aulas: int = Column(Integer)
    instrutor: str = Column(String(100))