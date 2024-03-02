import cv2
import mediapipe as mp
import numpy as np
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Define keyboard keys
keyboard = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
    ['SPACE']
]

# Initialize frame width and height for virtual keyboard
frame_width, frame_height = 800, 600

# Function to draw keyboard on screen
def draw_keyboard():
    key_width, key_height = frame_width // 10, frame_height // 4
    key_padding = 10
    
    for i in range(len(keyboard)):
        for j in range(len(keyboard[i])):
            key_x = j * key_width + key_padding
            key_y = i * key_height + key_padding
            if keyboard[i][j] != 'SPACE':
                cv2.rectangle(frame, (key_x, key_y), (key_x + key_width, key_y + key_height), (255, 255, 255), 2)
                cv2.putText(frame, keyboard[i][j], (key_x + 20, key_y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            else:
                cv2.rectangle(frame, (key_x, key_y), (key_x + 3 * key_width, key_y + key_height), (255, 255, 255), 2)
                cv2.putText(frame, 'SPACE', (key_x + 20, key_y + 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Main loop
cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # If hands are detected, track the hand landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            for idx, landmark in enumerate(hand_landmarks.landmark):
                cx, cy = int(landmark.x * frame_width), int(landmark.y * frame_height)
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

            # Check finger states for keyboard input
            fingers = [0, 0, 0, 0, 0]
            if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y:
                fingers[1] = 1
            if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y:
                fingers[2] = 1
            if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y:
                fingers[3] = 1
            if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x:
                fingers[0] = 1
            
            # Check for key press based on finger position
            for i in range(len(keyboard)):
                for j in range(len(keyboard[i])):
                    key_x = j * (frame_width // 10) + 10
                    key_y = i * (frame_height // 4) + 10
                    if keyboard[i][j] != 'SPACE':
                        if key_x < cx < key_x + (frame_width // 10) and key_y < cy < key_y + (frame_height // 4):
                            if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0:
                                pyautogui.press(keyboard[i][j])
                                cv2.rectangle(frame, (key_x, key_y), (key_x + (frame_width // 10), key_y + (frame_height // 4)), (0, 255, 0), cv2.FILLED)
                    else:
                        if key_x < cx < key_x + 3 * (frame_width // 10) and key_y < cy < key_y + (frame_height // 4):
                            if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0:
                                pyautogui.press(' ')
                                cv2.rectangle(frame, (key_x, key_y), (key_x + 3 * (frame_width // 10), key_y + (frame_height // 4)), (0, 255, 0), cv2.FILLED)

    # Draw the virtual keyboard on the screen
    draw_keyboard()

    # Display the frame
    cv2.imshow('Virtual Keyboard', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
