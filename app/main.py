from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.router.categories import categories_router
from app.router.expenses import expenses_router

app = FastAPI(title="Expense Tracker", version="0.0.1")

app.include_router(categories_router)
app.include_router(expenses_router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/scalar")
def scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )