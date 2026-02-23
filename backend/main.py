from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

app = FastAPI(
    title= "Interactive Story Generator API",
    description= "API for creating dynamic, user-driven adventure stories",
    version="1.0.1",
    docs_url="/docs",
    redoc_url="/redoc",
)   

app.add_middleware(
    CORSMiddleware,
    allow_origins= settings.ALLOW_ORIGINS,
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"],
)


if __name__ == "__main__":
    import uvicorn  
    uvicorn.run(
        "main:app",
        host= "127.0.0.1",
        port= 5001,
        reload= True

)