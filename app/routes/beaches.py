from fastapi import APIRouter
from app.models.beach import Beach
from app.database.fake_database import beaches

router = APIRouter()

# rota GET
@router.get("/beaches")
def get_beaches():
    return beaches

# rota POST
@router.post("/beaches")
def create_beach(beach: Beach):
    new_beach = {
        "id": len(beaches), # id simples baseado no tamanho da lista
        "name": beach.name,
        "state": beach.state,
        "image": "/static/images/default.png"  # imagem padrão
    }
    beaches.append(new_beach)
    return new_beach