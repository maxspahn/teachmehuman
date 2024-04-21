import time
import pyautogui

def select_building_1():

	time.sleep(0.1)
	pyautogui.moveTo(509, 502)
	pyautogui.mouseDown()
	pyautogui.moveTo(509, 502)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_building_1()
