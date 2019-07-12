# Speech_to_text
Speech To Text

PRE-Requisites
 Refer to this video for the installation of pocketsphinx , sphinxbase and sphinxtrain.
Create model directory
Make etc & wav directories in model directory
In the etc directory, make a model.filler file as below
<s> SIL
</s> SIL
<sil> SIL




Uploading

Recording audio via the created site:
Change the paths accordingly in the upload.php file.
Before recording audio, both the User and the word to be recorded  will be selected  from the dropdown. 
The data to be displayed in the dropdowns will be fetched from the database.
Without which the recording will not start.
The User will be the name of the person recording audio.
The word must be the utterance to be recorded.
Atleast 5 to 10 recordings per user are required for each keyword.

These recordings will be directly stored in the wav directory of the model file.

After Recording, you can listen to the audio  and upload it.
If you want to discard the audio, press the record button again.
For each new user, a new directory will be created in which their audio files will be stored.
Text files will also be created for respective users.


2. Training 
To create a model: 
In wav; folders for each speaker will be created having their audio files
Run append.py which will append all the speaker files and     store it as model.txt 
Run webcrawler.py 
Run dictionary.py
Then run the following commands
You should be in the model directory.
Command 1:
python ../sphinxtrain/scripts/sphinxtrain -t an4 setup // replace an4 with folder name eg in this case 'final'

In sphinxtrain.cfg file:
line 125, 126, 134, 135 : set density = 8
$CFG_CD_TRAIN = 'no'; [165]
 $DEC_CFG_MODEL_NAME = "$CFG_EXPTNAME.ci_cont"; [242]

Train the data:
In the model directory eg. 'final' in this case:
Open command prompt and run
python ../sphinxtrain/scripts/sphinxtrain run

TO Test via command line:

Go to pocketsphinx/bin/Release/Win32/
Open command prompt there and run:
pocketsphinx_continuous -infile "path to audio file" -hmm "path/to/model_parameters/model.ci_cont" -dict "path/to/dic" -lm “path/to/lm.dmp”

Link to Google Docs: https://docs.google.com/document/d/1gRGrNjSh49mexOKiKcZfPisetqOF_xAy6ZW5etqgnNo/edit?usp=sharing
