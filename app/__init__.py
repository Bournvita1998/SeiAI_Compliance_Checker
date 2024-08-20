from fastapi import FastAPI

app = FastAPI()

from app import routes
app.include_router(routes.router)
