# ClipTake
Tool for video production professionals to automatically get clip information using speech recognition, computer vision

Background
----------
Like many video creators, having proper clip, scene and take information is essential to organizing video clips for editing. Therefore, I imagined and have started to develop a python based script (eventually to be pushed to a GUI release) that asks for a clip(s) to be analyzed for their clip information based on speech recognition analysis of the video file. Additional speech to text information (such as spoken notes in documentary settings, dialogue in narrative clips, etc) is useful to the editor to quickly find, so that text would be helpful in a separate text file, or saved to the metadata of the video clip. To make this information even more accurate, computer vision could be used to parse clip information from the slate.

Initial Project Goals:
----------

1.) Script allows for single or multiple file inputs to be anaylzed using several cloud based speech recognition services to determine:

* clip, scene, camera (call letter), take information
  
* actual transcript of speech from scene, separated in text file accompanying clip (at timecode of when it is said)
  
2.) Add information to metadata of clip file, and/or video clip file name


Stretch Goals
---------

* Utilize OpenCV for python to analyze video to find slate and automatically read clip, scene, camera, and take information.

* Compare speech recognition with OpenCV information to refine best guess of clip information. 


Other Software/Requirements
----------

* Uses FFMPEG to split audio from video files, as of now, you must have it installed on your system. 

* Uses `SpeechRecognition <https://github.com/Uberi/speech_recognition/>`__ (see speech-recognition-license.txt) 
