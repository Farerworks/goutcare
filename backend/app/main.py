from fastapi import FastAPI

# generated router
from app.generated.api_v1 import router as generated_router

app = FastAPI(title="GoutCare API")

# mount generated routes under /api/v1
app.include_router(generated_router, prefix="/api/v1")
