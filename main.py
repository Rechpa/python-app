from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello from the Python app 🔥 ya a9wa farah f darkom <3"}
