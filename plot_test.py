import librosa
import matplotlib.pyplot as plt
import numpy as np

# 音声ファイルを読み込む
y, sr = librosa.load('test.mp3')

# ピッチ抽出
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# ピッチの平均値を計算
pitches = [np.mean(pitch) for pitch in pitches]

# プロットする
plt.figure(figsize=(10, 4))
plt.plot(pitches)
plt.title('Pitch over time')
plt.ylabel('Pitch')
plt.xlabel('Time')
plt.show()
