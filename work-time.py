import pyautogui

# Pause for 20 seconds after each mouse move
pyautogui.PAUSE = 20

# Start the mouse in the top left corner
pyautogui.moveTo(10, 10)

vertical = 1
horizontal = 1

while True:
    for i in range(10):
        pyautogui.moveRel(10 * vertical, 10 * horizontal, duration=0.5)
    vertical *= -1
    horizontal *= -1
