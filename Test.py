import time
import pyautogui

# The message you want to type
message = "a"

# Delay in seconds between each typing
typing_delay = 1

# Main loop
while True:
    # Sleep for 60 seconds
    time.sleep(60)

    # Type the message
    pyautogui.typewrite(message, interval=typing_delay)
