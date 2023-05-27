from fastapi import FastAPI
import uvicorn
from routes import auth

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1",
)

@app.get("/health")
def health():
    return {"healthy"}

app.include_router(auth.router_auth)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9532)