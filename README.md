# MySmartHome

This project is the final submission task for class 'MOBILE SYSTEM CONVERGENCE AND PRACTICE[501]'
It operates LEDs, cameras, and motors through voice recognition.
Raspberry Pi 3 was used and Python was used.

<Operating Procedures>
  1. User Click the Button(Record)
  2. Voice record
  3. The SpeechToText1 class receives the user's voice, converts the voice into a string, and returns it. (Use SpeechRecognition 3.8.1)
  4. The CommandModule.py analyzes the sentence and executes the command.
  5. if you want to another cmd -> press the clear button.
  
 <A recognizable sentence>
   - turn on/off the lamp
   - take a picture
   - open/close the door
 
   
  <Reference>
    - TTS : https://pypi.org/project/SpeechRecognition/
    - STT : https://pypi.org/project/gTTS/
    - GPIO : https://pypi.org/project/RPi.GPIO/
    
