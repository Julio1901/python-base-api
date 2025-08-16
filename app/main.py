from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import beaches

app = FastAPI(title="Minha API Base")

# Registrando router
app.include_router(beaches.router)

# Servindo arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/ping")
def ping():
    return {"status": "ok"}
