# Hand Gesture Controller for Web Apps

A real-time hand gesture recognition system that allows users to control browser actions using intuitive hand gestures detected through a webcam.

## Features

- Real-time hand gesture detection using MediaPipe
- Control browser actions with natural hand gestures:
  - ✋ Open palm: Scroll down
  - ✊ Fist: Scroll up
  - 👍 Thumbs up: Mute/Unmute YouTube
  - ✌️ Peace/Victory: Play/Pause YouTube
- Smooth, responsive feedback
- Toggle gesture control mode with 'g' key

## Requirements

- Python 3.8+
- Webcam
- Required Python packages (see requirements.txt)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/SiriNadig/hand-gesture-controller.git
cd hand-gesture-controller
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the main script:
```bash
python main.py
```

2. Press 'g' to toggle gesture control mode
3. Perform hand gestures in front of your webcam to control browser actions
4. Press 'q' to quit the application

## Project Structure

- `main.py`: Main application entry point
- `gesture_recognition.py`: Hand gesture detection and classification
- `actions.py`: Browser control actions using PyAutoGUI
- `utils.py`: Utility functions and constants

## Technical Details

The system uses:
- MediaPipe Hands for real-time hand detection and 21-point landmarks
- OpenCV for webcam video feed capture
- PyAutoGUI for simulating keyboard and mouse events
- NumPy for gesture logic based on landmark coordinates

## Contributing

Feel free to submit issues and enhancement requests!
