from nanoleafapi import Nanoleaf
import json
import sys
import time

# Nanoleaf IP
# warning: pairing starts on first run
# run script, hold down nanolead power button 5-7 seconds, run script again
nl = Nanoleaf("192.168.69.6")

# panel ids (can be retrieved with print(nl.get_layout()))
panel_ids = ["87", "193", "11", "25", "141", "111", "62", "202", "52"]

# not super bright colors
blue = '10 50 150'  # 30 minutes left
green = '80 150 60'  # 15-29 minutes left
yellow = '200 150 0'  # 10-14 minutes left
orange = '200 80 0'  # 5-9 minutes left
red = '100 0 0'  # 1-4 minutes left
white = '120 120 120'  # 0 minutes left


# set specific color
def set_color(pos, color):
    nl.write_effect(json.loads('{"command": "display", "animType": "static", "animData": "1 ' + panel_ids[
        pos - 1] + ' 1 ' + color + ' 0 1", "loop": false}'))


# show the choosen colors
def show_colors():
    set_color(1, yellow)
    set_color(2, red)
    set_color(3, orange)
    set_color(4, green)
    set_color(5, blue)
    set_color(6, white)


# turn all lights to one color
def turn_all(color):
    for x in range(len(panel_ids)):
        set_color(x, color)

# Timer
def timer(minutes):
    if minutes > 270:
        print("Timer [" + str(minutes) + "] is too high. Maximum is 270 minutes")
    else:
        for t in reversed(range(minutes + 1)):
            print("Minutes:" + str(minutes))
            timer = minutes
            minutes -= 1

            if timer > 135:
                for x in range(len(panel_ids)):
                    if timer >= 30:
                        timer -= 30
                        set_color(x + 1, blue)
                    elif timer >= 15:
                        timer -= 15
                        set_color(x + 1, green)
                    elif timer >= 10:
                        timer -= 10
                        set_color(x + 1, yellow)
                    elif timer >= 5:
                        timer -= 5
                        set_color(x + 1, orange)
                    elif timer >= 1:
                        timer -= timer
                        set_color(x + 1, red)
                    else:
                        set_color(x + 1, white)
            elif timer > 90:
                for x in range(len(panel_ids)):
                    if timer >= 15:
                        timer -= 15
                        set_color(x + 1, green)
                    elif timer >= 10:
                        timer -= 10
                        set_color(x + 1, yellow)
                    elif timer >= 5:
                        timer -= 5
                        set_color(x + 1, orange)
                    elif timer >= 1:
                        timer -= timer
                        set_color(x + 1, red)
                    else:
                        set_color(x + 1, white)
            elif timer > 45:
                for x in range(len(panel_ids)):
                    if timer >= 10:
                        timer -= 10
                        set_color(x + 1, yellow)
                    elif timer >= 5:
                        timer -= 5
                        set_color(x + 1, orange)
                    elif timer >= 1:
                        timer -= timer
                        set_color(x + 1, red)
                    else:
                        set_color(x + 1, white)
            elif timer > 9:
                for x in range(len(panel_ids)):
                    if timer >= 5:
                        timer -= 5
                        set_color(x + 1, orange)
                    elif timer >= 1:
                        timer -= timer
                        set_color(x + 1, red)
                    else:
                        set_color(x + 1, white)
            else:
                for x in range(len(panel_ids)):
                    if timer >= 1:
                        timer -= 1
                        set_color(x + 1, red)
                    else:
                        set_color(x + 1, white)
            if t == 0:
                break
            time.sleep(59) #Cause one second is needed for the update request

# Get panel ids
print(nl.get_layout())

if len(sys.argv) > 1:
    print(sys.argv[1])

    if sys.argv[1] == 0:
        turn_all(white)
    else:
        timer(int(sys.argv[1]))
else:
    print("\nEnter parameter with timer duration (like: python3 nanoleafTimer.py 10)")