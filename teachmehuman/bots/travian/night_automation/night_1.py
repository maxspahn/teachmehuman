import time
from teachmehuman.bots.travian.atomics import *

def night_automation():
    go_to_buildings()
    time.sleep(1)
    select_building_1()
    time.sleep(1)
    upgrade_main_building()
    time.sleep(1)
    go_to_resources()

