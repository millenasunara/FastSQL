from typing import List 

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel
from schemas.curso_schema import CursoSchema
from core.deps import get_session

# Vou responder um CursoSchema e também receber um CursoSchema!
# API envia JSON e espera recerb JSON
router = APIRouter()
# POST CURSOS
@router.post('/', status_code=status.HTTP_201_CREATED, reponse_model = CursoSchema)
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_session)):
    print("teste")
    novo_curso = CursoModel(titulo= curso.titulo,
                            aulas = curso.aulas,
                            horas = curso.horas,
                            instrutor = curso.instrutor)
    db.add(novo_curso)
    await db.commit()
    return novo_curso