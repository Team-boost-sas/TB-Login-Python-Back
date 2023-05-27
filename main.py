from fastapi import FastAPI, status
from src.routes import auth

app = FastAPI(
    title="security and authentication",
    description="a REST API using python and mysql",
    version="0.0.1",
    tags=[
        "auth"
    ]
)

@app.get(
        "/health",
        summary="check status API",
        response_model=str,
        status_code=status.HTTP_200_OK,
        tags=[
            "API"
        ]
        )
def health():
    return "healthy"

app.include_router(auth.router_auth)
