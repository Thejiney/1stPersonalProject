import librosa
import numpy as np

def make_vector_wav(filename):
  # Load the example clip
  y, sr = librosa.load(filename)

  # Set the hop length; at 22050 Hz, 512 samples ~= 23ms
  hop_length = 512
  print(1)
  # Separate harmonics and percussives into two waveforms
  y_harmonic, y_percussive = librosa.effects.hpss(y)
  print(2)
  # Beat track on the percussive signal
  tempo, beat_frames = librosa.beat.beat_track(y=y_percussive,
                                               sr=sr)
  print(3)
  # Compute MFCC features from the raw signal
  mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop_length, n_mfcc=13)
  print(4)
  # And the first-order differences (delta features)
  mfcc_delta = librosa.feature.delta(mfcc)
  print(5)
  # Stack and synchronize between beat events
  # This time, we'll use the mean value (default) instead of median
  beat_mfcc_delta = librosa.util.sync(np.vstack([mfcc, mfcc_delta]),
                                      beat_frames)
  print(6)
  # Compute chroma features from the harmonic signal
  chromagram = librosa.feature.chroma_cqt(y=y_harmonic,
                                          sr=sr)
  print(7)
  # Aggregate chroma features between beat events
  # We'll use the median value of each feature between beat frames
  beat_chroma = librosa.util.sync(chromagram,
                                  beat_frames,
                                  aggregate=np.median)
  print(8)
  # Finally, stack all beat-synchronous features together
  return np.vstack([beat_chroma, beat_mfcc_delta])

def make_three_demension(X_data):
  max_beats = 1138
  feature_dim = X_data[0].shape[0]
  num_songs = len(X_data)
  X_data_array = np.zeros((num_songs, feature_dim, max_beats))

  for i, X in enumerate(X_data):
    X_data_array[i, :, :X.shape[1]] = X
  return X_data_array