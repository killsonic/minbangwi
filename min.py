import pyautogui as pgi
import time
import keyboard
# print(pgi.position())

# pgi.screenshot('1.png', region=(554, 859, 200, 200))
print('F4 10초 누르면 종료')

while True:
    time.sleep(3)
    if keyboard.is_pressed('F4'): #F4 중지
        break
    else:
        i = pgi.locateCenterOnScreen('1.png')
        print(i)
        if i == None:
            pass
        else:
            pgi.click(i)
            

    