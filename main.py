from fastapi import FastAPI

app = FastAPI()

@app.post("/api/receives_vacancy")
def receives_vacancy():
    pass
