#!/usr/bin/env python3
import speech_recognition as sr
import subprocess, os


welcome_note = "ClipTaker (Working Name) Video file analyzer \n"
print(welcome_note)
### improve way of getting file...
### decide if audio or video file

#obtain file
###if audio file, then... if video file...
AUDIO_FILE = input('Enter file to analyze: \n')

#make worker directory
dir_to_use = '/Users/teepeeproco/Desktop/ClipMaking'
os.mkdir(dir_to_use)
os.chdir(dir_to_use)

#Strip for audio file
command = "ffmpeg -i "+ AUDIO_FILE +"  -ab 160k -ac 2 -ar 44100 -vn audioOnly.wav"
print("Extracting audio from video file for speech recognition")
subprocess.call(command, shell=True, stdout=subprocess.PIPE)
striped_audio = '/Users/teepeeproco/Desktop/ClipMaking/audioOnly.wav'


r = sr.Recognizer()
with sr.AudioFile(striped_audio) as source:
    audio = r.record(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    output_string = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said: " + output_string)
    with open("Output.txt", "w") as text_file:
        print(f"Recognition Output: {output_string}", file=text_file)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
