import speech_recognition as sr 

AUDIO_FILE = ("example.wav")

# use the audio file as the audio source

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
  	#reads the audio file. Here we use record instead of
  	#listen
  	audio = r.record(source)

try:
	print("The audio file contains: " + r.recognize_google(audio))

except sr.UnknownValueError:
  	print("Google speech Recognition could not understand audio")

except sr.RequestError as e:
 	print("could not request results from Google Speech Recognition service; {0}".forma) 	 	