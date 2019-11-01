from EmoPy.src.fermodel import FERModel
from EmoPy.src.ph import SmartLight
from pkg_resources import resource_filename
import cv2
import time
import random


target_emotions = ['fear', 'calm', 'anger', 'happiness', 'disgust', 'sadness', 'surprise']
model = FERModel(target_emotions, verbose=True)

#cap = cv2.VideoCapture(0)

sm_light = SmartLight()

sm_light.turn_on(1)

fontFace = cv2.FONT_HERSHEY_SIMPLEX;
fontScale = 1;
thickness = 2;

#Specify the camera which you want to use. The default argument is '0'
video_capture = cv2.VideoCapture(0)
#Capturing a smaller image fçor speed purposes
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 80)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 80)
#video_capture.set(cv2.CAP_PROP_FPS, 15)



'''
while True:
    ret, frame1 = cap.read()
    filename =  'own_training_data/surprise/%d.jpg' %(random.randint(1,1000000))
    print(filename)
    cv2.imwrite(resource_filename('EmoPy.examples', filename), frame1)
    time.sleep(1)
'''

while True:
    ret, frame = video_capture.read()
    #to_save = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(resource_filename('EmoPy.examples', '1.jpg'), frame)
    print('Predicting on image...')
    frameString = model.predict(resource_filename('EmoPy.examples','1.jpg'))
    print(frameString)
    time.sleep(1)
    if frameString == 'anger':
        print("I am not quite happy")
        sm_light.control_intensity(1,100)
        print(frameString)
        time.sleep(1)
    elif frameString == 'calm':
        print("I am rather calm")
        sm_light.control_intensity(1, 140)
        time.sleep(1)
    elif frameString == 'happiness':
        print("I am happy")
        sm_light.control_intensity(1, 100)
        time.sleep(1)
    elif frameString == 'fear':
        print("I am a bit of feared")
        sm_light.control_intensity(1, 40)
        time.sleep(1)
    elif frameString == 'sadness':
        print("I am not very happy")
        sm_light.control_intensity(1, 5)
        time.sleep(1)

    retval, baseline = cv2.getTextSize(frameString, fontFace, fontScale, thickness)
    cv2.rectangle(frame, (0, 0 ), (20 + retval[0], 50 ), (0,0,0), -1 )
    cv2.putText(frame, frameString, (10, 35), fontFace, fontScale, (255, 255, 255), thickness, cv2.LINE_AA)
    cv2.imshow('Video', frame)
    cv2.waitKey(1)
    #Press Esc to exit the window
    if cv2.waitKey(1) & 0xFF == 27:
        break
'''
print('Predicting on disgust image...')
model.predict(resource_filename('EmoPy.examples','image_data/sample_disgust_image.png'))

print('Predicting on anger image...')
model.predict(resource_filename('EmoPy.examples','image_data/sample_anger_image2.png'))

'''
