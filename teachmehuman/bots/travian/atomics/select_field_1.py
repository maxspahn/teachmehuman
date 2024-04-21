import time
import pyautogui

def select_field_1():

	time.sleep(0.1)
	pyautogui.moveTo(550, 380)
	pyautogui.mouseDown()
	pyautogui.moveTo(550, 380)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_field_1()
