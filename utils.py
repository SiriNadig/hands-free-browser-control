import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Constants for gesture recognition
SCROLL_THRESHOLD = 0.1
POINT_THRESHOLD = 0.2
THUMB_UP_THRESHOLD = 0.3
PEACE_THRESHOLD = 0.2

def initialize_camera():
    """Initialize and return the webcam capture object."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Could not open webcam")
    return cap

def draw_landmarks(image, hand_landmarks):
    """Draw hand landmarks on the image."""
    mp_drawing.draw_landmarks(
        image,
        hand_landmarks,
        mp_hands.HAND_CONNECTIONS,
        mp_drawing_styles.get_default_hand_landmarks_style(),
        mp_drawing_styles.get_default_hand_connections_style()
    )

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return np.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def is_thumb_up(landmarks):
    """Check if the gesture is a thumbs up."""
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    index_mcp = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    
    return (thumb_tip.y < thumb_ip.y and 
            thumb_tip.y < index_mcp.y and
            abs(thumb_tip.x - thumb_ip.x) < THUMB_UP_THRESHOLD)

def is_peace(landmarks):
    """Check if the gesture is a peace sign."""
    index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    
    # Check if index and middle fingers are up while others are down
    return (index_tip.y < ring_tip.y and 
            middle_tip.y < ring_tip.y and
            ring_tip.y < pinky_tip.y)

def is_open_palm(landmarks):
    """Check if the gesture is an open palm."""
    finger_tips = [
        landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
        landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
        landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
        landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    ]
    finger_mcps = [
        landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP],
        landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP],
        landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP],
        landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]
    ]
    
    # Check if all fingers are extended
    return all(tip.y < mcp.y for tip, mcp in zip(finger_tips, finger_mcps))

def is_fist(landmarks):
    """Check if the gesture is a fist."""
    finger_tips = [
        landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP],
        landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
        landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP],
        landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    ]
    finger_mcps = [
        landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP],
        landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP],
        landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP],
        landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]
    ]
    
    # Check if all fingers are curled
    return all(tip.y > mcp.y for tip, mcp in zip(finger_tips, finger_mcps))

def is_pointing_right(landmarks):
    """Check if the gesture is pointing right."""
    index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    index_mcp = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    
    return (index_tip.x > index_mcp.x and 
            index_tip.y < middle_tip.y and
            abs(index_tip.x - index_mcp.x) > POINT_THRESHOLD)

def is_pointing_left(landmarks):
    """Check if the gesture is pointing left."""
    index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    index_mcp = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    
    return (index_tip.x < index_mcp.x and 
            index_tip.y < middle_tip.y and
            abs(index_tip.x - index_mcp.x) > POINT_THRESHOLD)
