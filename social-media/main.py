# Import necessary things 

from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from routes import post,user,auth,vote
from .config import settings
import logging

# Handle logging

logger=logging.getLogger("uvicorn")
logger.setLevel(os.environ.get("LOG_LEVEL", "DEBUG"))
# Create fastapi instance
app = FastAPI(
    docs_url="/v1/social-media-application/docs",
    title="Social Media Application Backend Design Title",
    openapi_url="/v1/social-media-application/openapi.json",
    description="Social media backend description",
    summary="Summary of the complete design of backend for social media application",
    version='1.0'
)

# Include middleware

origins=['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# include routes
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


