import pyautogui
import time
#while True:
#    print(pyautogui.position())
    
    
    #274, 1060  #
    
pyautogui.moveTo(274,1060, duration = 1 )

time.sleep(2)

pyautogui.click(interval=1)


pyautogui.write("cmd", interval=1)

pyautogui.press("enter")

time.sleep(3)

pyautogui.write("exit()", interval=1)


pyautogui.press("enter")


