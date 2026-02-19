from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from llm.audio_generator import audio_generator
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    print("teste")
    return {"message": "Hello World"}

@app.get("/audio")
async def root(texto: str, voice: str):
    resp = audio_generator(texto, voice)
    return FileResponse("audio.wav")

@app.get("/app/", include_in_schema=False, name="home")
async def read_app(request: Request):
    return templates.TemplateResponse(request, "home.html")

@app.get("/app/teste", include_in_schema=False, name="teste")
async def read_app(request: Request):
    return templates.TemplateResponse(request, "teste.html")

