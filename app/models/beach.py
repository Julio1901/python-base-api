from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/beaches", tags=["beaches"])

# Modelo de entrada (serve para validar dados de post e put)
class Beach(BaseModel):
    name: str
    state: str