from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from wonderwords import RandomWord


class Thumbnail(BaseModel):
    url: str
    filename: Optional[str] = None

app = FastAPI()

@app.post('/thumbnail', response_model=Thumbnail)
def create_thumbnail(thumbnail: Thumbnail):
    rw = RandomWord()
    filename = '_'.join(rw.random_words(3, include_parts_of_speech=['nouns', 'adjectives']))
    thumbnail.filename = filename
    return thumbnail
