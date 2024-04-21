import time
import pyautogui

def select_building_5():

	time.sleep(0.1)
	pyautogui.moveTo(589, 640)
	pyautogui.mouseDown()
	pyautogui.moveTo(589, 640)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_building_5()
