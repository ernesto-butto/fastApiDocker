from fastapi import FastAPI
from textblob import TextBlob

app = FastAPI()


@app.get("/")
def read_root():
    blob = TextBlob("Hello my friend, how are you?")
    return {"Hello": blob.translate(to="es")}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
