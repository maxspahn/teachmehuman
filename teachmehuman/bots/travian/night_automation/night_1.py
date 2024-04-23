import time
from tqdm import tqdm
from teachmehuman.bots.travian.atomics import *
from teachmehuman.utils.jump_to_window_1 import jump_to_window_1

def night_automation():
    for _ in range(10):
        jump_to_window_1()
        time.sleep(2)
        building = None
        while building is None:
            print("Building not found. Retrying...")
            time.sleep(1)
            building, time_left = build_time_left()
        print(f"Building {building} in process. Time left: {time_left}")
        for _ in tqdm(range(time_left), desc=f"Building {building}"):
            time.sleep(1)
        jump_to_window_1()
        time.sleep(2)
        upgrade_baracks()
        time.sleep(1)
        go_to_resources()

