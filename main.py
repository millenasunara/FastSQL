from fastapi import FastAPI
from core.configs import settings
from api.v1._api import api_router

api = FastAPI(title='API de Cursos da ETS')
api.include_router(api_router, prefix= settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host = '0.0.0.0', port=8000, log_level='info', reload=True)