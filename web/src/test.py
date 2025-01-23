import vector

from tensorflow.keras.models import load_model
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# graphs = os.listdir(os.path.join(BASE_DIR, '../static/apt'))
# musics = os.listdir(os.path.join(BASE_DIR, '../static/music'))
# print(graphs)
# print(musics)

musics = os.listdir(os.path.join(BASE_DIR, '../static/music'))
model = load_model(os.path.join(BASE_DIR, '../static/model/music_model.h5'))
X_data = []
for i, music in enumerate(musics):
  X_data.append(vector.make_vector_wav(os.path.join(BASE_DIR, '../static/music') + '/' + music))
X_data_array = vector.make_three_demension(X_data)
Y = model.predict(X_data_array)
answer = [filename for filename, y in zip(musics, Y) if y >= 0.7]