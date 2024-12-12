import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

index_y = 0  # Initialize index_y outside the loop

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)

            landmarks = hand.landmark
            for ID, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if ID == 8:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    pyautogui.moveTo(index_x, index_y)

                if ID == 4:
                    cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        # pyautogui.alert("Test")
                            pyautogui.click()
                            pyautogui.sleep(1)
                            print(hands)

                # if ID == 16:
                #     cv2.circle(img=frame, center=(x, y), radius=15, color=(0, 255, 255))
                #     ring_x = screen_width / frame_width * x
                #     ring_y = screen_height / frame_height * y
                #     print('outside', abs(ring_y - index_y))
                #     if abs(ring_y - index_y) < 10:
                #         pyautogui.alert("Test")
                #         #pyautogui.click()
                #         pyautogui.sleep(1)
                #         print(hands)

    cv2.imshow('test', frame)
    key = cv2.waitKey(3)
    if key == 27:
        print('Pressed Esc')
        break
