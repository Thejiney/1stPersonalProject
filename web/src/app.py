from fastapi import FastAPI
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
import os

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount('/static',
          StaticFiles(directory=os.path.join(BASE_DIR, '../static')),
          name='static')
templates = Jinja2Templates(directory=os.path.join(BASE_DIR,'../templates'))

@app.get('/')
async def index(request:Request):
  return templates.TemplateResponse('home.html', {'request':request})

@app.get('/apt')
async def apt(request:Request):
  return templates.TemplateResponse('apt.html', {'request':request})

@app.get('/music')
async def music(request:Request):
  return templates.TemplateResponse('music.html', {'request':request})