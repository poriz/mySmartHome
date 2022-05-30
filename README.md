# MySmartHome

This project is the final submission task for class 'MOBILE SYSTEM CONVERGENCE AND PRACTICE[501]' <br>
It operates LEDs, cameras, and motors through voice recognition.<br>
Raspberry Pi 3 was used and Python was used.<br>
<br>
## Operating Procedures <br>
  1. User Click the Button(Record)<br>
  2. Voice record<br>
  3. The SpeechToText1 class receives the user's voice, converts the voice into a string, and returns it. (Use SpeechRecognition 3.8.1)<br>
  4. The CommandModule.py analyzes the sentence and executes the command.<br>
  5. if you want to another cmd -> press the clear button.<br>
  <br>
  
## A recognizable sentence <br>
  - turn on/off the lamp<br>
  - take a picture<br>
  - open/close the door<br>
 <br>
 <br>
 
## Reference<br>
  - TTS : https://pypi.org/project/SpeechRecognition/<br>
  - STT : https://pypi.org/project/gTTS/<br>
  - GPIO : https://pypi.org/project/RPi.GPIO/<br>
    
