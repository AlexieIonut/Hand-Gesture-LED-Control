import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
import pyfirmata2

""""""
board = pyfirmata2.Arduino('COM3')
led1 = board.get_pin('d:2:o')
led2 = board.get_pin('d:3:o')
led3 = board.get_pin('d:4:o')
led4 = board.get_pin('d:5:o')
led5 = board.get_pin('d:6:o')

model_path = 'hand_landmarker.task'

base_options = python.BaseOptions(model_asset_path = model_path)

options = vision.HandLandmarkerOptions(base_options = base_options,running_mode=vision.RunningMode.VIDEO,num_hands = 2,min_hand_detection_confidence=0.8)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame,1)

    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format = mp.ImageFormat.SRGB,data = rgb_frame)

    timestamp = int(time.time()*1000)
    result = detector.detect_for_video(mp_image, timestamp)

    if result.hand_landmarks:
        landmarks = result.hand_landmarks[0]

        label = result.handedness[0][0].category_name
        if label == 'Left':
            real_label = 'Right'
        else:
            real_label = 'Left'

        if real_label == 'Right':
            is_palm = landmarks[5].x < landmarks[17].x
            if is_palm:
                led1.write(1 if landmarks[4].x < landmarks[3].x else 0)
            else:
                led1.write(1 if landmarks[4].x > landmarks[3].x else 0)

        elif real_label == 'Left':
            is_palm = landmarks[17].x < landmarks[5].x
            if is_palm:
                led1.write(1 if landmarks[4].x > landmarks[3].x else 0)
            else:
                led1.write(1 if landmarks[4].x < landmarks[3].x else 0)


        led2.write(1 if landmarks[8].y < landmarks[6].y else 0)
        led3.write(1 if landmarks[12].y < landmarks[10].y else 0)
        led4.write(1 if landmarks[16].y < landmarks[14].y else 0)
        led5.write(1 if landmarks[20].y < landmarks[18].y else 0)

    else:
        led1.write(0)
        led2.write(0)
        led3.write(0)
        led4.write(0)
        led5.write(0)

    cv2.imshow('Hand Detection', frame)
    if cv2.waitKey(1) == ord('q'):
        exit()


detector.close()
cap.release()
cv2.destroyAllWindows()