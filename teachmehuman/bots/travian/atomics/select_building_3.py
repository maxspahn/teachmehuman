import time
import pyautogui

def select_building_3():

	time.sleep(0.1)
	pyautogui.moveTo(830, 542)
	pyautogui.mouseDown()
	pyautogui.moveTo(830, 542)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_building_3()
