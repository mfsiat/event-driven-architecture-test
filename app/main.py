import os
from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from wonderwords import RandomWord

from .thumbnail_maker import create

STATIC_DIR = os.environ.get("STATIC_DIR", "/tmp/static")


class Thumbnail(BaseModel):
    url: str
    filename: Optional[str] = None


app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.post("/thumbnail", response_model=Thumbnail)
def create_thumbnail(thumbnail: Thumbnail):
    rw = RandomWord()
    filename = "_".join(
        rw.random_words(3, include_parts_of_speech=["nouns", "adjectives"])
    )
    create(thumbnail.url, filename)
    thumbnail.filename = filename
    return thumbnail
