import cv2
import numpy as np
import pytesseract
import requests
from PIL import Image
import io
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
os.environ['GLOG_minloglevel'] = '2'
import time
from cvzone.HandTrackingModule import HandDetector
from gtts import gTTS
from playsound3 import playsound
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import msvcrt

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\linbe\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, element):
    self.queue.append(element)

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue.pop(0)

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.queue[0]

  def isEmpty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)

check_gest = False
tts = ""
myQueue = Queue()

while True:
    while not check_gest:
        print("i am looking for gestures")
        url = "http://100.66.14.18/capture"

        r = requests.get(url)
        img = Image.open(io.BytesIO(r.content))
        # img.show()
        save_path = r'C:\Users\linbe\VS CODE\UTEK 2026\pytesseract-0.3.13\pytesseract\capture.jpg'
        img.save(save_path)

        base_options = python.BaseOptions(model_asset_path=r'C:\Users\linbe\VS CODE\UTEK 2026\pytesseract-0.3.13\pytesseract\gesture_recognizer.task')
        options = vision.GestureRecognizerOptions(base_options=base_options)
        recognizer = vision.GestureRecognizer.create_from_options(options)

        image = mp.Image.create_from_file(save_path)
        # STEP 4: Recognize gestures in the input image.
        recognition_result = recognizer.recognize(image)
        time.sleep(0.5)

        # STEP 5: Process the result. In this case, visualize it.
        if recognition_result.gestures:
            top_gesture = recognition_result.gestures[0][0]

            if top_gesture.category_name == 'Pointing_Up':
                print('Replay')
                print(myQueue)
                if myQueue.size() != 0:
                    for item in myQueue.queue:
                        myobj = gTTS(text=item, lang='en', slow=False)
                        myobj.save("tts.mp3")
                        playsound("tts.mp3")

            elif top_gesture.category_name == 'Open_Palm':
                print('turn off')
                exit()

            elif top_gesture.category_name == 'Closed_Fist':
                print('read')
                check_gest = True

        if msvcrt.kbhit():
           key = msvcrt.getch().decode('utf-8').lower()
           if key == 'b':
                print("Bypass key detected!")
                check_gest = True
 
    while not tts:
        print("i am looking for words")
        url = "http://100.66.14.18/capture"
        r = requests.get(url)
        img = Image.open(io.BytesIO(r.content))
        # img.show()
        
        img_np = np.frombuffer(r.content, np.uint8)
        img_bgr = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
        # img = cv2.imdecode(img_np, cv2.IMREAD_GRAYSCALE)
        img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        tts = pytesseract.image_to_string(img)
        
    print("words detected")
    print(tts)

    myobj = gTTS(text=tts, lang='en', slow=False)
    myobj.save("tts.mp3")
    playsound("tts.mp3")

    myQueue.enqueue(tts)
    if myQueue.size() >= 4:
        myQueue.dequeue()
    
    tts = ""
    check_gest = False
    time.sleep(0.5)
    print("looping")