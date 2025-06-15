import cv2
import mediapipe as mp
from utils import (
    mp_hands, draw_landmarks,
    is_thumb_up, is_peace, is_open_palm,
    is_fist, is_pointing_right, is_pointing_left
)

class GestureRecognizer:
    def __init__(self):
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )

    def recognize_gesture(self, frame):
        """Process frame and recognize hand gestures."""
        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame and detect hands
        results = self.hands.process(rgb_frame)
        
        gesture = None
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks on the frame
                draw_landmarks(frame, hand_landmarks)
                
                # Recognize gesture
                if is_thumb_up(hand_landmarks):
                    gesture = 'thumb_up'
                elif is_peace(hand_landmarks):
                    gesture = 'peace'
                elif is_open_palm(hand_landmarks):
                    gesture = 'open_palm'
                elif is_fist(hand_landmarks):
                    gesture = 'fist'
                elif is_pointing_right(hand_landmarks):
                    gesture = 'point_right'
                elif is_pointing_left(hand_landmarks):
                    gesture = 'point_left'
                
                # Only process the first detected hand
                break
        
        return frame, gesture

    def __del__(self):
        """Clean up resources."""
        self.hands.close()
