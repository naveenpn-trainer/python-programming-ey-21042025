from fastapi import FastAPI
app = FastAPI()

@app.get("/test-api")
def index():
    return {"message":"Hello World"}

# uvicorn simple_get_request:app --reload