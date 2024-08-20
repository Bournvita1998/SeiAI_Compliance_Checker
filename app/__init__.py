from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import routes
import logging
import os

# Configure logging
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO").upper())

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)
