from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title= "Interactive Story Generator API",
    description= "API for creating dynamic, user-driven adventure stories",
    version="1.0.1",
    docs_url="/docs",
    redoc_url="redoc",
)   

