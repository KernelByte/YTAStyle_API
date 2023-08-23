from fastapi import FastAPI

app = FastAPI()
app.title = "API - YTA Style"
app.version = "1.0"

@app.get("/", tags=['home'])
def message():
    return "Hello World"