from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hellofarah():
    return {"message": "Hello from the Python app 🔥 ya a9wa farah f darkom <3"}
