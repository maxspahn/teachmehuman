import time
import pytesseract
from typing import Tuple
import pyautogui
import re

from teachmehuman.bots.travian.atomics.go_to_resources import go_to_resources


def build_time_left() -> Tuple[str, int]:
    go_to_resources()
    time.sleep(1)
    im1 = pyautogui.screenshot(region=(320, 702, 400, 20))
    text = pytesseract.image_to_string(im1,lang='eng')
    # text is something like x bulding_name hh:mm:ss hrs. done at hh:mm [
    time_left_pattern = re.compile(r'(\d{1}:\d{2}:\d{2})')
    # match only characters and spaces for buildng name

    bulding_pattern = re.compile(r'x\s([a-zA-Z\s]+\d)')
    re_match = re.findall(time_left_pattern, text)
    building_match = re.findall(bulding_pattern, text)
    building_name = None
    time_left = 0
    if building_match:
        building_name = building_match[0]
    if re_match:
        time_left_hours = re_match[0].split(':')[0]
        time_left_minutes = re_match[0].split(':')[1]
        time_left_seconds = re_match[0].split(':')[2]
        time_left = int(time_left_hours) * 3600 + int(time_left_minutes) * 60 + int(time_left_seconds)
    return building_name, time_left
