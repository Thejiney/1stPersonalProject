from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
import os
from tensorflow.keras.models import load_model

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount('/static',
          StaticFiles(directory=os.path.join(BASE_DIR, '../static')),
          name='static')
templates = Jinja2Templates(directory=os.path.join(BASE_DIR,'../templates'))
graphs = os.listdir(os.path.join(BASE_DIR, '../static/apt'))

@app.get('/')
async def index(request:Request):
  return templates.TemplateResponse('home.html', {'request':request})

@app.get('/apt')
async def apt(request:Request):
  return templates.TemplateResponse('apt.html', {'request':request,'graphs':graphs})

@app.get('/graph/{graph}')
async def graph(request:Request, graph:str):
  return templates.TemplateResponse('graph.html', {'request':request, 'graph':graph})

@app.get('/music')
async def music(request:Request):
  musics = os.listdir(os.path.join(BASE_DIR, '../static/music'))
  return templates.TemplateResponse('music.html', {'request':request, 'musics':musics})

@app.get('/music/done')
async def abstract(request:Request):
  musics = os.listdir(os.path.join(BASE_DIR, '../static/music'))
  model = load_model(os.path.join(BASE_DIR, '../static/model/music_model.h5'))
  return templates.TemplateResponse('music.html', {'request':request, 'musics':musics})