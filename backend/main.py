from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title= "Interactive Story Generator API",
    description= "API for creating dynamic, user-driven adventure stories",
    version="1.0.1",
    docs_url="/docs",
    redoc_url="redoc",
)   

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials= True,
    allow_methods= ["*"],
    allow_header= ["*"],
)


if __name__ == "__main__":
    import uvicorn  
    uvicorn.run(
        "main:app",
        host= "0.0.0.0",
        port= 5001,
        reload= True

)