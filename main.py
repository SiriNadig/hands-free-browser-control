import cv2
from utils import initialize_camera
from gesture_recognition import GestureRecognizer
from actions import BrowserController

def main():
    # Initialize components
    cap = initialize_camera()
    recognizer = GestureRecognizer()
    controller = BrowserController()
    
    print("Hand Gesture Controller started!")
    print("Press 'g' to toggle gesture control mode")
    print("Press 'q' to quit")
    
    while True:
        # Read frame from webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
            
        # Flip the frame horizontally for a more natural view
        frame = cv2.flip(frame, 1)
        
        # Recognize gesture
        frame, gesture = recognizer.recognize_gesture(frame)
        
        # Handle gesture if detected
        if gesture:
            controller.handle_gesture(gesture)
            
            # Display current gesture
            cv2.putText(
                frame,
                f"Gesture: {gesture}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )
        
        # Display control mode status
        status = "Enabled" if controller.is_enabled else "Disabled"
        cv2.putText(
            frame,
            f"Control Mode: {status}",
            (10, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0) if controller.is_enabled else (0, 0, 255),
            2
        )
        
        # Show the frame
        cv2.imshow('Hand Gesture Controller', frame)
        
        # Handle keyboard input using OpenCV
        key = cv2.waitKey(1) & 0xFF
        if key == ord('g'):
            status = controller.toggle_control()
            print(f"Gesture control {'enabled' if status else 'disabled'}")
        elif key == ord('q'):
            break
    
    # Clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
