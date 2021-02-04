import speech_recognition as sr
from googletrans import Translator
import sys
import os
import pyttsx3
import playsound
import pydub

#gives us easy access to client root computer
sysroot = os.path.expanduser("~")

#easy file operation 
def save(filename, content):
	with open(filename, "rb")as f:
		f.write(content)


def translate(lang,text):
	#init the translator class
	translator = Translator()
	#translate the text with given arguments
	translation = translator.translate(text, dest= lang)
	translations = f"{translation.origin} --> {translation.text} "
	return translations

#here we'll create the speechrecognition fuction
def recognize(audio, lang="en-US"):
	#init the recognizer class
	r = sr.Recognizer()
	#opens input file
	file_in = sr.AudioFile(audio)
	#records input file as source
	with file_in as source:
		r.adjust_for_ambient_noise(source, duration=0.5)
		audio_record = r.record(source)
	#save result to output variable
	output = r.recognize_google(audio_record, language = lang)
	return output

def read(word):
	#initialize the pyttsx3 init class
	engine = pyttsx3.init()
	engine.say(word)
	engine.runAndWait()
	engine.save_to_file(word, "output.mp3")

#playing audio files using playsound module
def play(audio_file):
	playsound(audio_file)

def convert(audio_input):
	src = audio_input
	dst = f"{audio_input}.wav"
	#convert mp3 files to wav file so speech recognition can work flawlessly
	sound = pydub.AudioSegment.from_mp3(src)
	sound.export(dst, format="wav")
def mic(lang="en-US"):
	r = sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
		r.adjust_for_ambient_noise(source, duration=0.5)
		audio = r.listen(source)
	results = r.recognize_google(audio, language = lang)
	return results




