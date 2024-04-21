import time
import pyautogui

def upgrade_wall():

	time.sleep(0.1)
	pyautogui.moveTo(544, 764)
	pyautogui.mouseDown()
	pyautogui.moveTo(544, 764)
	pyautogui.mouseUp()


if __name__ == "__main__":
	upgrade_wall()
