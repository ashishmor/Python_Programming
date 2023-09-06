import pyautogui
import time

while True:
    # Get the current mouse cursor position
    x, y = pyautogui.position()

    # Simulate typing 'a' at the current cursor position
    pyautogui.click(x, y)  # Click at the current position (to focus the input)
    pyautogui.typewrite('a', interval=0.1)  # Type 'a' with a slight delay between keypresses

    # Sleep for 5 seconds before the next 'a'
    time.sleep(5)