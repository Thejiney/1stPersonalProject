from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
import os
from tensorflow.keras.models import load_model
import vector

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount('/static',
          StaticFiles(directory=os.path.join(BASE_DIR, '../static')),
          name='static')
templates = Jinja2Templates(directory=os.path.join(BASE_DIR,'../templates'))
graphs = os.listdir(os.path.join(BASE_DIR, '../static/apt'))
answer = []

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

@app.get('/music/progress')
async def abstract(request:Request):
  return templates.TemplateResponse('progress.html', {'request':request})

@app.patch('/music/progress')
async def abstract(request:Request):
  global answer
  musics = os.listdir(os.path.join(BASE_DIR, '../static/music'))
  model = load_model(os.path.join(BASE_DIR, '../static/model/music_model.h5'))
  X_data = []
  for music in musics:
    X_data.append(vector.make_vector_wav(os.path.join(BASE_DIR, '../static/music') + '/' + music))
  X_data_array = vector.make_three_demension(X_data)
  print(X_data_array.shape)
  X_data_array = X_data_array.reshape(-1, 38 * X_data_array.shape[2])
  Y = model.predict(X_data_array)
  answer = [filename for filename, y in zip(musics, Y) if y >= 0.5]

@app.get('/music/done')
async def abstract(request:Request):
  return templates.TemplateResponse('music.html', {'request':request, 'musics':answer})