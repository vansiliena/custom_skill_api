from fastapi import FastAPI
from app.api.routes import matress_map_condition

app = FastAPI()
app.include_router(matress_map_condition.router, prefix="/api/custom-skill", tags=["custom skill"])