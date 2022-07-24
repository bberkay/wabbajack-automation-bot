import pyautogui
import time
import datetime

counter = 1
wait_page = 5
while True:
    time.sleep(wait_page)
    try:
        pyautogui.scroll(-200)
        time.sleep(2)
        pyautogui.click('button.png')
        print("[{}]New mod is downloading ----> {}".format(datetime.datetime.now(), counter))
        counter += 1
        wait_page = 5
    except:
        print("[{}]Waiting for new mod......".format(datetime.datetime.now()))
        wait_page = 2
        continue
        
