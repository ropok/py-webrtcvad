import librosa
y, s = librosa.load('HAI_001_Tr1.WAV', sr=48000)
librosa.output.write_wav('Tr1.WAV', y, s)
