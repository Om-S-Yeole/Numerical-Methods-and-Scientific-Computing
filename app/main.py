from fastapi import FastAPI
from app.api.v1 import router as v1_router

app = FastAPI(title="Numerical Methods and Scientific Computing", version="0.1.0")

# Include routers
app.include_router(v1_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Numerical Methods and Scientific Computing"}
