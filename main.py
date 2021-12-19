from fastapi import FastAPI

from modules import customer
from db_manager.init_db import create_db

app = FastAPI(title="Numbers King")

@app.on_event("startup")
async def startup():
    await create_db()

app.include_router(router=customer.route.customer.router, prefix="/v1")
