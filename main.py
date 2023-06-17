import time
import pyautogui
from PIL import ImageGrab

time.sleep(2)

jump_x, jump_y = 390, 650
duck_x, duck_y = 390, 420

cactus_color = (255, 255, 255)
pterodactyl_color = (255, 255, 255)  # Assuming the pterodactyls are white

while True:
    screenshot = ImageGrab.grab()

    pixel = screenshot.getpixel((jump_x, jump_y))
    print(pixel)
    pyautogui.moveTo(jump_x, jump_y)
    for pi in pixel:
        if pi > 45:
            print("jump")
            pyautogui.keyDown('space')
            time.sleep(0.001)
            pyautogui.keyUp('space')
            break

        pixel = screenshot.getpixel((duck_x, duck_y))
        if pixel == pterodactyl_color:
            pyautogui.keyDown('down')
            time.sleep(0.2)
            pyautogui.keyUp('down')

    time.sleep(0.001)
