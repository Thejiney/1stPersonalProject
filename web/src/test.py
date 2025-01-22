import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
graphs = os.listdir(os.path.join(BASE_DIR, '../static/apt'))
musics = os.listdir(os.path.join(BASE_DIR, '../static/music'))
print(graphs)
print(musics)
