import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
hands = mp_hands.Hands()

while True:
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    if id == 8:
        cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
        index_x = screen_width / frame_width * x
        index_y = screen_height / frame_height * y
        pyautogui.moveTo(x, y)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('test', image)
    key = cv2.waitKey(3)
    if key == 27:
        print("Exiting..")
        break




