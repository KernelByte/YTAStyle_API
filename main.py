from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional


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


class Movie(BaseModel):
    id:int 
    title: str
    description: Optional[str] = 'Descripcion'


@app.get("/", tags=['home'])
def message():
    return HTMLResponse('<h1>Hola Mundo</h1>')


@app.get("/movies", tags=['movies'])
def get_movies():
    return movies

@app.post('/movies',tags=['movies'])
def crear(movie: Movie):
        movies.append({
            "id":3,
            "Titulo": "Tiburon",
            "año": 2023
        })