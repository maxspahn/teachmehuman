import time
import pyautogui

def select_building_4():

	time.sleep(0.1)
	pyautogui.moveTo(727, 627)
	pyautogui.mouseDown()
	pyautogui.moveTo(727, 627)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_building_4()
