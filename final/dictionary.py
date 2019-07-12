import glob								#importing libraries
from shutil import copyfile
import librosa
import imp
import os
import soundfile as sf



#Converting all the audio files to 16000Hz sample rate , 16bit format and mono channel.
main_path = "C:\\sphinx\\final\\wav"
for i in glob.glob(f"{main_path}\\*\\*.*"):
	path = i
	y,sr = librosa.core.load(path, sr=16000, mono=True, offset=0.0, duration=None, res_type='kaiser_best')		
	out_path = path.split('.')[0] + '.wav'
	librosa.output.write_wav(out_path, y, sr)
	data, samplerate = sf.read(out_path)
	sf.write(out_path, data, samplerate, subtype='PCM_16')	
	path_end = path.split('.')[-1]
	if (path_end != "wav"):
		os.remove(path)
	else:
		pass


#Reading the phonetics from the .dic file and writing them in the .phone file
dic = []
f2 = glob.glob("C:\\sphinx\\final\\etc\\*.dic")
f2 = f2[0]
new = f2.split('.')[0]
f2 = open(f2, "r")
if f2.mode == "r":
	contents = f2.read()
	words = contents.split("\n")
	for w in words:
		w1 = w.split()
		if len(w1) > 0:
			for i in range(1,len(w1)):
				if w1[i] not in dic:
					dic.append(w1[i])	
dic.append("SIL")
dic.sort()

f = open(new + ".phone", "w+")
for d in dic:
	f.write(d + "\n")


#Reading the filenames of all the audio files and writing them in the .fileids file
f= open(new + '_train.fileids',"w+")
dic = []
for i in glob.glob(f"{main_path}\\*\\*.wav"):
 	dic.append(i)
dic1 = []
for l in dic:
	l1 = l.split('\\')
	str1 = l1[-2] + "/" + l1[-1].split(".")[0]
	dic1.append(str1)
	f.write(str1 + '\n')
f.close()

i =0
y = glob.glob("C:\\sphinx\\final\\etc\\*.transcription")
y = y[0]
name = y.split('.')[0]

#Reading the contents of the .fileids file , one line at a time  and appending on each line of the .transcription file.
with open(y, 'r') as istr:
	 with open(name + '_train.transcription', 'w+') as ostr:
	        for line in istr:
	            line = line.rstrip('\n') + " " + "(" + dic1[i] + ")" 
	            ostr.write(line +"\n")
	            i= i+1	

#Creating copy of the .fileids file and .transcription file
copyfile( name+"_train.transcription", name +"_test.transcription")
copyfile(name + "_train.fileids", name+ "_test.fileids")

os.remove(name + '.txt')