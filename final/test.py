import os

model_path = "" #Provide the path of the directory where model files are there
data_path = ""  #Provide the path of the directory where audio files are there

config = {
    'verbose': False,
    'audio_file': os.path.join(data_path, ''), #name of the audio file to be transcribed
    'buffer_size': 2048,
    'no_search': False,
    'full_utt': False,
    'hmm': os.path.join(model_path, ''),  #name of the hmm model
    'lm': os.path.join(model_path, ''),   #name of the language model
    'dict': os.path.join(model_path, '')  #name of the dictionary
}

audio = AudioFile(**config)
for phrase in audio:
    print(phrase)
