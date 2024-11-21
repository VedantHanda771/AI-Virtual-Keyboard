# Virtual Keyboard Using Hand Gestures

This project demonstrates a virtual keyboard controlled by hand gestures using the webcam. It utilizes MediaPipe's hand tracking model to detect hand landmarks and PyAutoGUI to simulate keyboard presses. The virtual keyboard is displayed on the screen, and each key can be "pressed" by hovering your hand over the corresponding key with a specific gesture.

---

## Features

- Hand gesture recognition to simulate keyboard input.
- Real-time webcam feed displaying a virtual keyboard.
- Compatible with any standard webcam (integrated or external).
- Simple control to press letters, numbers, and space by positioning fingers.

---

## Requirements

Before running this project, make sure you have the following Python libraries installed:

- **OpenCV**: For handling the webcam feed and rendering the keyboard.
- **MediaPipe**: For hand tracking and detecting hand landmarks.
- **PyAutoGUI**: To simulate keypresses on the system.
- **NumPy**: For numerical operations.




You can install the required libraries by running the following command:

```bash
pip install opencv-python mediapipe pyautogui numpy
```
---

## How to Run

1. Clone or download this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Ensure your webcam is connected and not in use by another application.
4. Run the Python script:

```bash
python project.py
```



This will open a window showing the virtual keyboard. Use your hand gestures to simulate pressing keys. 

- **Index Finger**: Hovering your index finger over a key will simulate a key press.
- **Space Bar**: Hover your hand over the space bar area to simulate a space key press.

To exit the program, press the 'q' key.

---

## How It Works

1. **Hand Detection**: MediaPipe processes the webcam feed and detects hand landmarks.
2. **Gesture Recognition**: Based on the hand position and gestures, the program identifies when the user is hovering over a key.
3. **Key Press Simulation**: When a key is detected, PyAutoGUI simulates the corresponding key press on your computer.
4. **Virtual Keyboard**: A virtual keyboard is drawn on the screen with labeled keys. It updates based on the gestures.

---

## Troubleshooting

- **Webcam not detected**: Ensure that the webcam is connected and accessible by the system. If you're using a laptop, ensure the built-in camera is functional.
- **Slow response**: Try closing other applications that might be using the webcam or consuming system resources.
- **Errors during runtime**: Check if all dependencies are installed correctly.

---


