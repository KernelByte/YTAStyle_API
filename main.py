from fastapi import FastAPI
from fastapi.responses import HTMLResponse

movies = [{
    "id":1,
    "Titulo": "hombres de negro",
    "año": 2021
},
{
    "id":2,
    "Titulo": "avion gris",
    "año": 2021
}]


app = FastAPI()
app.title = "API - YTA Style"
app.version = "1.0"

@app.get("/", tags=['home'])
def message():
    return HTMLResponse('<h1>Hola Mundo</h1>')


@app.get("/movies", tags=['movies'])
def get_movies():
    return movies
