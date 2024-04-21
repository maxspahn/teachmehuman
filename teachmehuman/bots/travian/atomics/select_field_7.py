import time
import pyautogui

def select_field_7():

	time.sleep(0.1)
	pyautogui.moveTo(537, 629)
	pyautogui.mouseDown()
	pyautogui.moveTo(537, 629)
	pyautogui.mouseUp()


if __name__ == "__main__":
	select_field_7()
