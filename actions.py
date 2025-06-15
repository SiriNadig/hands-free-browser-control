import pyautogui
import keyboard
import time

class BrowserController:
    def __init__(self):
        self.last_action_time = 0
        self.action_cooldown = 0.5  # Cooldown between actions in seconds
        self.is_enabled = False

    def toggle_control(self):
        """Toggle gesture control mode."""
        self.is_enabled = not self.is_enabled
        return self.is_enabled

    def can_perform_action(self):
        """Check if enough time has passed since the last action."""
        current_time = time.time()
        if current_time - self.last_action_time >= self.action_cooldown:
            self.last_action_time = current_time
            return True
        return False

    def scroll_down(self):
        """Scroll down the page."""
        if self.is_enabled and self.can_perform_action():
            pyautogui.scroll(-100)  # Negative value scrolls down

    def scroll_up(self):
        """Scroll up the page."""
        if self.is_enabled and self.can_perform_action():
            pyautogui.scroll(100)  # Positive value scrolls up

    def next_tab(self):
        """Switch to the next tab."""
        if self.is_enabled and self.can_perform_action():
            pyautogui.hotkey('ctrl', 'tab')

    def previous_tab(self):
        """Switch to the previous tab."""
        if self.is_enabled and self.can_perform_action():
            pyautogui.hotkey('ctrl', 'shift', 'tab')

    def toggle_mute(self):
        """Toggle mute/unmute on YouTube."""
        if self.is_enabled and self.can_perform_action():
            pyautogui.press('m')

    def toggle_play_pause(self):
        """Toggle play/pause on YouTube."""
        if self.is_enabled and self.can_perform_action():
            pyautogui.press('k')

    def handle_gesture(self, gesture):
        """Handle the detected gesture."""
        if not self.is_enabled:
            return

        gesture_actions = {
            'open_palm': self.scroll_down,
            'fist': self.scroll_up,
            'point_right': self.next_tab,
            'point_left': self.previous_tab,
            'thumb_up': self.toggle_mute,
            'peace': self.toggle_play_pause
        }

        action = gesture_actions.get(gesture)
        if action:
            action()
