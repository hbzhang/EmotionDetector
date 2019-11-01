from EmoPy.src.fermodel import FERModel
from EmoPy.src.ph import SmartLight
from pkg_resources import resource_filename
import cv2
import time
import random

target_emotions = ['fear', 'calm', 'anger', 'happiness', 'disgust', 'sadness', 'surprise']
model = FERModel(target_emotions, verbose=True)

fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
thickness = 2

video_capture = cv2.VideoCapture(0)
#Capturing a smaller image fçor speed purposes
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 80)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 80)

while True:
    ret, frame = video_capture.read()
    #to_save = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(resource_filename('EmoPy.examples', '1.jpg'), frame)
    print('Predicting on image...')
    frameString = model.predict(resource_filename('EmoPy.examples', '1.jpg'))
    pYes a lot of love talking I took statistics benevolent countermeasures yeah did not a deep enough they going to OR sneezing division rightYeah me yeah exactly saw him ask I got a nice big didn't have his baseball as about away go to deep statisticsI'll get that class sounds impossible had as a business what was it really that is from collar on sentencesI'm almost a whole calculation children in the same classI'm a probably do like a voice a voice that is it what's the distaste 11 lumbar support money point think I'll leastFor any status of the estate within his that it is color Cody SquareYes I'll out of the Decidiste skate didn't session just had Okay on your vacationOkay by Dunaway? I got y'all standings worry on a cervix eight any anything bookkeeperHolly Holly get hereBut I even the deep blue Gold this anything here Essien wordYell work you go to barf on my bootyIs calculus on everything companies, KinoI love your mother of everything okay I mean I  did all the more modern science policies and statistics consisted six okay yes and also in on those images files done and yeah I think some people just want to program beyond slate so I harassed gallon Java file without calculus and all that stuff yet and it's always Jo Jo was good but is off all contributors especially hoping so because despite the specialty.'(1) & 0xFF == 27:
        break






