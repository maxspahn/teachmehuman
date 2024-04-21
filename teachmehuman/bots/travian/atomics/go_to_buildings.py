import time
import pyautogui

def go_to_buildings():

	time.sleep(0.1)
	pyautogui.moveTo(430, 179)
	pyautogui.mouseDown()
	pyautogui.moveTo(430, 179)
	pyautogui.mouseUp()


if __name__ == "__main__":
	go_to_buildings()
