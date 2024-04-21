import time
import pyautogui

def go_to_resources():

	time.sleep(0.1)
	pyautogui.moveTo(364, 168)
	pyautogui.mouseDown()
	pyautogui.moveTo(364, 168)
	pyautogui.mouseUp()


if __name__ == "__main__":
	go_to_resources()
