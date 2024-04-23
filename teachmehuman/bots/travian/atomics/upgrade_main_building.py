import time
import pyautogui

def upgrade_main_building():

	time.sleep(0.1)
	pyautogui.moveTo(517, 759)
	pyautogui.mouseDown()
	pyautogui.moveTo(517, 759)
	pyautogui.mouseUp()


if __name__ == "__main__":
	upgrade_main_building()
