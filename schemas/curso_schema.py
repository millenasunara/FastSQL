from typing import Optional
from pydantic import BaseModel as SchemaBaseModel
# Como o SQL Alchemy tem o BaseModel dele, não poderemos confundir

class CursoSchema(SchemaBaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: str
    horas: int
    instrutor: int

    class Config: 
        from_atributes = True