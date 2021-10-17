from fastapi import FastAPI, Request, status
from pydantic import BaseModel
import mlconjug3
from fastapi.middleware.cors import CORSMiddleware

import json

app = FastAPI()
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ConjugateItem(BaseModel):
    language: str
    infinitive: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/supported_languages")
def get_supported_languages():
    languages = mlconjug3._TRANSLATED_LANGUAGES
    return {"output": languages}


@app.post("/conjugate")
def get_conjugate(item:ConjugateItem):
    conjugator = mlconjug3.Conjugator(language=item.language)
    conjugate_info = conjugator.conjugate(item.infinitive).conjug_info
    return {"output": conjugate_info}
