"""

Step1: Import Package
Step2: Implement Functionality
Step3: Output
"""
import gtts
from gtts import gTTS
import os

mytext  = "Welcome to this Session on Python Packages  "
mySpeech = gtts.gTTS(text = mytext,lang='en',slow=False)
mySpeech.save("MyVoice2.mp3")
os.system("MyVoice2.mp3")
print("Coverting my text into Speech")
