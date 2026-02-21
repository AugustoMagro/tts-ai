from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from llm.audio_generator import audio_generator
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

title = "teste"

class Audio(BaseModel):
    texto: str
    voice: str

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/api/audio")
async def root(audio: Audio):
    resp = audio_generator(audio.texto, audio.voice)
    print(resp)
    return FileResponse("audio.wav")

@app.get("/app/", include_in_schema=False, name="home")
async def read_app(request: Request):
    return templates.TemplateResponse(request, "home.html", {"title":title})
